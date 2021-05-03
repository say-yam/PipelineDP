"""

"""
from pipeline_dp import ComputedMetrics, Metrics, AggregateParams, DataExtractors, PipelineOperations
from typing import Any, Iterable

class SumBasedAggregator(object):
  """ Computes Sum based metrics.

  """
  def __init__(self, params: AggregateParams, collection: Iterable[Any], ops: PipelineOperations):
    self.params = params
    self.collection = collection
    self.ops = ops

  def compute_metrics(self) -> ComputedMetrics:
    """
    
    :return:
    """

    # Check vals type raise if not Iterable[float]

    # Step 1: Clip the value within bound
    # Step 2: Compute Count, Sum and Sum^2
    # Step 3: Sum per privacy_id, partition_key
    # Step 4: Count privacy_id per partition
    # Step 5: apply cross partition contribution bound
    # Step 6: add noise
    # Step 7: Compute Mean and Variance


