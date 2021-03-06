#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example gets all base rates.
"""

# Import appropriate modules from the client library.
from googleads import ad_manager


def main(client):
  # Initialize appropriate service.
  base_rate_service = client.GetService('BaseRateService', version='v201902')

  # Create a statement to select base rates.
  statement = ad_manager.StatementBuilder(version='v201902')

  # Retrieve a small amount of base rates at a time, paging
  # through until all base rates have been retrieved.
  while True:
    response = base_rate_service.getBaseRatesByStatement(statement.ToStatement(
    ))
    if 'results' in response and len(response['results']):
      for base_rate in response['results']:
        # Print out some information for each base rate.
        print('Base rate with ID "%d", type "%s", and rate card ID "%d" was '
              'found.\n' % (base_rate['id'],
                            ad_manager.AdManagerClassType(base_rate),
                            base_rate['rateCardId']))
      statement.offset += statement.limit
    else:
      break

  print('\nNumber of results found: %s' % response['totalResultSetSize'])


if __name__ == '__main__':
  # Initialize client object.
  ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage()
  main(ad_manager_client)
