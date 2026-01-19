from dataclasses import dataclass


@dataclass
class OutgoingOrganizationDTO:
    id: int
    name: str
    building_id: int


@dataclass
class OutgoingOrganizationByActivityDTO:
    organization_id: int
    organization_name: str
    building_id: int
    activity_id: int
    activity_name: str


@dataclass
class OutgoingOrganizationActivityNameDTO:
    organization_id: int
    organization_name: str
    building_id: int
    activity_ids: list
    activity_names: list
