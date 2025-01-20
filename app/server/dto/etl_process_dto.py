from dataclasses import dataclass

@dataclass
class EtlProcessDto:
    championship: str
    job_instance: str
    date_match: str
    appResource: str
    dir_spark: str
    main_spark: str