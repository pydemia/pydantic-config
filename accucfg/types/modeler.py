from .base import BaseEnum
from typing import Iterator, Optional, Union, List, Tuple, Dict
import pandas as pd


__all__ = [
    "RuntimeSummaryCategory",
    # "summarize_status",
]


class ServiceType(BaseEnum):
    LoadBalancer = "LoadBalancer"
    NodePort = "NodePort"
    ClusterIP = "ClusterIP"


class ServiceStatus(BaseEnum):
    """THIS ORDER IS REFERENCED. DO NOT CHANGE IT.
    """
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    COMPLETED = "COMPLETED"
    DELETED = "DELETED"
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
