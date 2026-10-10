
# routing.py – Department mapping, hierarchy, and escalation
# for HostelCare AI

from typing import Optional
from datetime import datetime


# --------------------------------------------------
# CATEGORY TO DEPARTMENT MAPPING
# --------------------------------------------------

CATEGORY_DEPARTMENT = {
    "Water": "Plumbing",
    "Electrical": "Electrical",
    "Housekeeping": "Housekeeping",
    "Security": "Security",
    "Other": "Housekeeping",
}


# --------------------------------------------------
# AUTHORITY HIERARCHY
# --------------------------------------------------

AUTHORITY_HIERARCHY = [
    {"role": "Technician", "level": 1},
    {"role": "Supervisor", "level": 2},
    {"role": "Warden", "level": 3},
    {"role": "Director", "level": 4},
]


def _next_role(current_role: str) -> Optional[str]:
    """Return the next authority role, or None at the top."""

    for idx, entry in enumerate(AUTHORITY_HIERARCHY):
        if entry["role"].lower() == str(current_role).lower():
            if idx + 1 < len(AUTHORITY_HIERARCHY):
                return AUTHORITY_HIERARCHY[idx + 1]["role"]
            return None

    return None


# --------------------------------------------------
# INITIAL COMPLAINT ROUTING
# --------------------------------------------------

def route_complaint(
    *,
    category: str,
    block: str,
    priority: str,
) -> str:
    """Choose the initial authority for a complaint."""

    if str(priority).strip().lower() == "critical":
        return "Supervisor"

    return "Technician"


# --------------------------------------------------
# MANUAL ESCALATION
# --------------------------------------------------

def manual_escalate(ticket: dict) -> Optional[str]:
    """Return the next authority for a ticket."""

    current_role = ticket.get("assigned_role")

    if not current_role:
        return None

    return _next_role(current_role)


# --------------------------------------------------
# TIMESTAMP PARSING
# --------------------------------------------------

def _parse_created_at(value):
    """Safely parse a stored timestamp into a datetime."""

    if isinstance(value, datetime):
        return value

    if not value:
        return None

    try:
        # Supports ISO timestamps with or without timezone.
        return datetime.fromisoformat(
            str(value).strip().replace("Z", "+00:00")
        )
    except (ValueError, TypeError):
        return None


# --------------------------------------------------
# AUTOMATIC ESCALATION
# --------------------------------------------------


def auto_escalate(database):
    """
    Escalate unresolved complaints after 30 minutes at their
    current authority level. Each escalation starts a new timer.
    """

    tickets = database.get_all_complaints()

    for ticket in tickets:
        status = str(ticket.get("status", "")).strip().lower()

        # Never automatically escalate resolved or closed tickets.
        if status in ("resolved", "closed"):
            continue

        current_role = ticket.get("assigned_role")
        if not current_role:
            continue

        new_role = _next_role(current_role)

        # Do not escalate beyond Director.
        if new_role is None:
            continue

        # Use updated_at to give each authority a fresh 30-minute window.
        reference_time = (
            _parse_created_at(ticket.get("updated_at"))
            or _parse_created_at(ticket.get("created_at"))
        )

        if reference_time is None:
            continue

        if reference_time.tzinfo is not None:
            now = datetime.now(reference_time.tzinfo)
        else:
            now = datetime.now()

        age_minutes = (now - reference_time).total_seconds() / 60

        if age_minutes < 30:
            continue

        timestamp = now.isoformat(timespec="seconds")

        new_level = next(
            (
                entry["level"]
                for entry in AUTHORITY_HIERARCHY
                if entry["role"].lower() == new_role.lower()
            ),
            1,
        )

        database.update_ticket_status(
            ticket_id=ticket["ticket_id"],
            status="Escalated",
            assigned_role=new_role,
            updated_at=timestamp,
            update_note=(
                f"Automatically escalated from {current_role} "
                f"to {new_role} after {age_minutes:.0f} minutes."
            ),
            escalation_level=new_level,
        )

        database.log_action(
            ticket_id=ticket["ticket_id"],
            action="Automatically escalated",
            from_role=current_role,
            to_role=new_role,
            timestamp=timestamp,
        )



# End of routing.py
