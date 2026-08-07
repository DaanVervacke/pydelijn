"""Typed data models returned by :class:`pydelijn.client.DeLijnClient`."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Stop:
    """A De Lijn stop ("halte")."""

    entity_number: str
    number: str
    name: str
    municipality: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    distance: int | None = None
    """Distance in meters from the search location, for nearby searches."""


@dataclass(frozen=True, slots=True)
class Line:
    """A De Lijn line ("lijn"), including its display colours."""

    entity_number: str
    number: str
    public_number: str | None = None
    description: str | None = None
    transport_type: str | None = None
    colour_front_hex: str | None = None
    colour_front_border_hex: str | None = None
    colour_back_hex: str | None = None
    colour_back_border_hex: str | None = None


@dataclass(frozen=True, slots=True)
class Passage:
    """A single realtime or scheduled passage of a line at a stop."""

    line: Line
    direction: str | None = None
    destination: str | None = None
    vias: str | None = None
    due_at_schedule: datetime | None = None
    due_at_realtime: datetime | None = None
    is_realtime: bool = False
    cancelled: bool = False
    ride_number: str | None = None
    vehicle_number: str | None = None

    @property
    def due_at(self) -> datetime | None:
        """Return the best known due time: realtime if known, else scheduled."""
        return (
            self.due_at_realtime
            if self.due_at_realtime is not None
            else self.due_at_schedule
        )
