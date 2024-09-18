# Lending / MM / CDP

Standard table definitions for lending protocols.

## Version: 1.0.0

### Pools

List of pools in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard id of the chain.                             | number |
| creation_block_number    | The block this pool was created in.                       | number |
| timestamp                | The timestamp of the block that this pool was created in. | number |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| receipt_token_address    | The contract address of the receipt token.                | string |
| receipt_token_symbol     | The symbol of the receipt token.                          | string |
| pool_address             | The contract address of the pool.                         | string |
| pool_type                | The type of the pool (collateral_only, isolated, supply_pool, cdp). | string |

### Position Snapshot

Snapshot of user positions in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | number |
| pool_address             | The contract address of the pool.                         | string |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| user_address             | The address of the user who has the position.             | string |
| supplied_amount          | The amount supplied by the user in the underlying token, decimal normalized. | number |
| supplied_amount_usd      | (Optional) The supplied amount in USD.                    | number |
| borrowed_amount          | The amount borrowed by the user in the underlying token, decimal normalized. | number |
| borrowed_amount_usd      | (Optional) The borrowed amount in USD.                    | number |
| collateral_amount        | (Optional) The amount of collateral-only tokens of this asset, decimal normalized. | number |
| collateral_amount_usd    | (Optional) The amount of collateral-only tokens in USD.   | number |

### Pool Snapshot

Snapshot of the pool's state in the lending protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | The standard id of the chain.                             | number |
| pool_address             | The contract address of the pool.                         | string |
| underlying_token_address | The contract address of the underlying token.             | string |
| underlying_token_symbol  | The symbol of the underlying token.                       | string |
| underlying_token_price_usd | (Optional) The token price of the underlying asset in USD. | number |
| available_amount         | The amount of token's available to borrow (liquidity or net supply or supply - borrow). | number |
| available_amount_usd     | (Optional) The available amount of token's in this pool in USD. | number |
| supplied_amount          | The total amount of the underlying token supplied in this pool, decimal normalized. | number |
| supplied_amount_usd      | (Optional) The supplied amount in USD.                    | number |
| non_recursive_supplied_amount | The amount of non recursive supply in this pool, in the underlying token, decimal normalized. This is an aggregation of all of the user's net supply of this asset. | number |
| collateral_amount        | (Optional) The amount of collateral only tokens in this pool. | number |
| collateral_amount_usd    | (Optional) The amount of collateral only tokens in the pool. | number |
| collateral_factor        | The collateral factor of the pool (defined as a decimal percentage, between 0-100). | number |
| supply_index             | The supply index of the pool.                             | number |
| supply_apr               | The current annual percentage rate for supplied amount, as a decimal percentage. | number |
| borrowed_amount          | The amount of underlying tokens borrowed from this pool in the underlying token, decimal normalized. | number |
| borrowed_amount_usd      | (Optional) The borrowed amount in USD.                    | number |
| borrow_index             | The borrow index of the pool.                             | number |
| borrow_apr               | The current annual percentage rate for borrow, as a decimal percentage. | number |
| total_fees_usd           | (Optional) The total revenue or fees accrued in this pool during the given snapshot period (ie, user_fees_usd + protocol_fees_usd = total_fees_usd). | number |
| user_fees_usd            | (Optional) The portion of total revenue or fees accrued to users of the protocol during the given snapshot period. | number |
| protocol_fees_usd        | (Optional) The portion of total revenue or fees accrued to protocol during the given snapshot period. | number |

### Events

All user events in the lending protocol (ie, Deposit, Withdrawal, Borrow, Repay, Liquidation, Flashloan)

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | number |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (ie, the transaction signer). | string |
| taker_address            | The address that receives the output of the event (ie, account that receives aTokens in an Aave Deposit). | string |
| pool_address             | The contract address of the pool.                         | string |
| token_address            | The address of the underlying token that was interacted with (ie, USDC and not aUSDC in Aave). | string |
| amount                   | The amount of token_address transacted, decimal normalized. | number |
| amount_usd               | The amount of token_address transacted, in USD.           | number |
| event_type               | The type of lending event, corresponds to the action taken by the user (ie, deposit, withdrawal, borrow, repay, liquidation, flashloan). | string |

### Incentive Claim Data

Transactional data on user level incentives claimed data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the claim.                               | number |
| chain_id                 | The standard chain id.                                    | number |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | number |
| user_address             | The address of the user who claimed the incentives.       | string |
| claimed_token_address    | The smart contract address of the claimed token.          | string |
| amount                   | The amount of the token claimed, decimal normalized.      | number |
| amount_usd               | The amount of claimed tokens in USD.                      | number |
| other_incentive_usd      | (Optional) Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | number |

> Note: This markdown file is auto-generated.
