import pandas as pd

from case_attribute_discovery.config import EventLogIDs


def discover_case_attributes(event_log: pd.DataFrame, log_ids: EventLogIDs, confidence: float) -> list:
    """
    Get the attributes in the event log that could be a case attribute, i.e. those attributes which value is fixed through all the process
    case.

    :param event_log:   event log to analyze.
    :param log_ids:     mapping for the IDs of the columns in the event log.
    :param confidence:  confidence value for an attribute to be considered a case attribute (average percentage of events within a case where
                        the value can be different).

    :return: a list with the IDs of the columns detected as case attributes, their type (discrete/continuous) and the values they take.
    """
    # Initialize case attributes
    case_attributes = []
    # Go over the columns of the event log to check if any attribute is not changing through the traces
    for attribute in event_log.columns:
        if attribute is not log_ids.case:
            # Check
            pass
    # Return list with discovered case attributes
    return case_attributes
