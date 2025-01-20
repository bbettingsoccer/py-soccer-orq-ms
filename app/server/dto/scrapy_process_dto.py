from dataclasses import dataclass

@dataclass
class ScrapyProcessDto:
    crawl: str
    championship: str
    job_instance: str