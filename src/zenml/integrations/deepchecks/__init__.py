#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Deepchecks integration for ZenML.

The Deepchecks integration provides a way to validate your data in your pipelines.
It includes a way to detect data anomalies and define checks to ensure quality of
data.

The integration includes custom materializers to store Deepchecks `SuiteResults` and
a visualizer to visualize the results in an easy way on a notebook and in your
browser.
"""

from typing import List

from zenml.enums import StackComponentType
from zenml.integrations.constants import DEEPCHECKS
from zenml.integrations.integration import Integration
from zenml.zen_stores.models.flavor_wrapper import FlavorWrapper

DEEPCHECKS_DATA_VALIDATOR_FLAVOR = "deepchecks"


class DeepchecksIntegration(Integration):
    """Definition of [Deepchecks](https://github.com/deepchecks/deepchecks) integration for ZenML."""

    NAME = DEEPCHECKS
    REQUIREMENTS = ["deepchecks>=0.6.3", "torch", "torchvision"]

    @staticmethod
    def activate() -> None:
        """Activate the Deepchecks integration."""
        from zenml.integrations.deepchecks import materializers  # noqa
        from zenml.integrations.deepchecks import visualizers  # noqa

    @classmethod
    def flavors(cls) -> List[FlavorWrapper]:
        """Declare the stack component flavors for the Deepchecks integration.

        Returns:
            List of stack component flavors for this integration.
        """
        return [
            FlavorWrapper(
                name=DEEPCHECKS_DATA_VALIDATOR_FLAVOR,
                source="zenml.integrations.deepchecks.data_validators.DeepchecksDataValidator",
                type=StackComponentType.DATA_VALIDATOR,
                integration=cls.NAME,
            ),
        ]


DeepchecksIntegration.check_installation()
