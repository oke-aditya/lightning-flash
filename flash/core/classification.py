from typing import Any

import torch

from flash.core.data import TaskDataPipeline
from flash.core.model import Task


class ClassificationDataPipeline(TaskDataPipeline):

    def before_uncollate(self, batch: torch.Tensor) -> torch.Tensor:
        if isinstance(batch, tuple):
            batch = batch[0]
        return torch.softmax(batch, -1)

    def after_uncollate(self, samples: Any) -> Any:
        return torch.argmax(samples, -1).tolist()


class ClassificationTask(Task):

    @staticmethod
    def default_pipeline() -> ClassificationDataPipeline:
        return ClassificationDataPipeline()
