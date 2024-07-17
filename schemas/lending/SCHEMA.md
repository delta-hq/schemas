# Lending / CDP Schema

This is the OpenBlock Labs standard schema for lending protocols.

## Schema

### Pools

**Description:** List of lending pools in this protocol.

| Property              | Description                                                       | Type   |
|-----------------------|-------------------------------------------------------------------|--------|
| protocolName          | The name of the protocol this table belongs to.                   | string |
| chainId               | The standard id of the chain.                                     | number |
| creationBlockNumber   | The block this pool was created in.                               | number |
| creationTimestamp     | The timestamp of the block that this pool was created in.         | number |
| underlyingTokenAddress| The contract address of the underlying token.                     | string |
| underlyingTokenSymbol | The symbol of the underlying token.                               | string |
| receiptTokenAddress   | The contract address of the receipt token.                        | string |
| receiptTokenSymbol    | The symbol of the receipt token.                                  | string |
| poolAddress           | The contract address of the pool.                                 | string |
| poolType              | The type of the pool (ie, collateral_only, isolated, supply_pool, cdp). | string |

### Position Snapshot

**Description:** Snapshot of user positions in the lending protocol.

| Property               | Description                                                                                  | Type   |
|------------------------|----------------------------------------------------------------------------------------------|--------|
| timestamp              | The timestamp of the snapshot.                                                               | string |
| protocolName           | The name of the protocol this table belongs to.                                              | string |
| chainId                | The standard id of the chain.                                                                | number |
| poolAddress            | The contract address of the pool.                                                            | string |
| underlyingTokenAddress | The contract address of the underlying token.                                                | string |
| underlyingTokenSymbol  | The symbol of the underlying token.                                                          | string |
| userAddress            | The address of the user who has the position.                                                | string |
| suppliedAmount         | The amount supplied by the user in native terms, normalized by underlying decimals.          | number |
| suppliedUsd            | The supplied amount in USD.                                                                  | number |
| borrowedAmount         | The amount borrowed by the user normalized to native terms, using underlying decimals.       | number |
| borrowedUsd            | The borrowed amount in USD.                                                                  | number |
| collateralAmount       | (Optional) The amount of collateral-only tokens of this asset, normalized.                   | number |
| collateralUsd          | (Optional) The amount of collateral-only tokens in USD.                                       | number |

### Pool Snapshot

**Description:** Pool level snapshots.

| Property               | Description                                                                                  | Type   |
|------------------------|----------------------------------------------------------------------------------------------|--------|
| timestamp              | The timestamp of the snapshot.                                                               | string |
| protocolName           | The name of the protocol this table belongs to.                                              | string |
| chainId                | The standard id of the chain.                                                                | number |
| poolAddress            | The contract address of the pool.                                                            | string |
| underlyingTokenAddress | The contract address of the underlying token.                                                | string |
| underlyingTokenSymbol  | The symbol of the underlying token.                                                          | string |
| availableAmount        | The amount of token's available to borrow (ie, liquidity or net supply or supply - borrow).  | number |
| availableTvlUsd        | The available amount of token's in this pool in USD.                                         | number |
| totalSuppliedAmount    | The total amount of the underlying token supplied in this pool normalized.                   | number |
| suppliedUsd            | The supplied amount in USD.                                                                  | number |
| collateralAmount       | (Optional) The amount of collateral only tokens in this pool.                                | number |
| collateralUsd          | (Optional) The amount of collateral only tokens in the pool.                                 | number |
| collateralFactor       | The collateral factor of the pool (defined as a percentage, between 0-100).                  | number |
| supplyIndex            | The supply index of the pool.                                                                | number |
| supplyApr              | The current annual percentage rate for supplied amount.                                      | number |
| supplyIncentiveApr     | The incentive annual percentage rate for supply.                                             | number |
| borrowedAmount         | The amount of underlying tokens borrowed from this pool, normalized to the underlying token. | number |
| borrowedUsd            | The borrowed amount in USD.                                                                  | number |
| borrowIndex            | The borrow index of the pool.                                                                | number |
| borrowApr              | The annual percentage rate for borrow.                                                       | number |
| borrowIncentiveApr     | The incentive annual percentage rate for borrow.                                             | number |
| feesUsd                | The total revenue / fees accrued in this pool during the given snapshot period.              | number |
| incentiveAmount        | The amount of incentives distributed in this pool during the given snapshot period, decimal normalized. | number |
| incentiveUsd           | The amount of incentives distributed, in USD.                                                | number |

### Protocol Snapshot

**Description:** Protocol level snapshot.

| Property               | Description                                                                                  | Type   |
|------------------------|----------------------------------------------------------------------------------------------|--------|
| timestamp              | The timestamp the snapshot was taken.                                                        | string |
| protocolName           | The name of the protocol this table belongs to.                                              | string |
| chainId                | The standard id of the chain.                                                                | number |
| tvlUsd                 | The total value locked in the protocol in USD. (ie, the total deposit or supplied amount).   | number |
| borrowAmountUsd        | The total amount of tokens borrowed in USD.                                                  | number |
| availableAmountUsd     | The amount of tokens available to borrow in this protocol in USD.                            | number |
| collateralUsd          | (Optional) The amount of collateral only assets available in USD.                            | number |
| feesUsd                | The total revenue and fees collected by the protocol in the given snapshot period, in USD.   | number |
