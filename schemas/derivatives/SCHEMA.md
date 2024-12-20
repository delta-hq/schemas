# Derivatives

OpenBlock Labs standard schema for derivatives protocols (options and perps).

## Version: 1.0.0-alpha

### Pools

Pools in the protocol (one entry for each token).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | Standard chain id.                                        | number |
| timestamp                | The timestamp of the block the pool was created on.       | number |
| creation_block_number    | The block number this pool was created on.                | number |
| pool_address             | The contract address of the pool.                         | string |
| pool_name                | The name of the pool (ie, name() in the smart contract).  | string |
| token_index              | The index of the token in the smart contract (one row for each token in a pool). | number |
| token_address            | The contract address of the token.                        | string |
| token_symbol             | The symbol of the token.                                  | string |

### Pairs (AMM)

Pairs traded in the protocol (one entry for each pair).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | Standard chain id.                                        | number |
| timestamp                | The timestamp of the block the pool was created on.       | number |
| creation_block_number    | The block number this pool was created on.                | number |
| pair_name                | The name of the pool (ie, name() in the smart contract).  | string |
| pair_index               | The index of the token in the smart contract (one row for each pair). | number |
| pair_address             | The contract address of the pair.                         | string |
| pair_symbol              | The symbol of the pair.                                   | string |
| pair_liquidity           | The liquidity available for trading for the pair (24h rolling average, in tokens). | number |
| pair_liquidity_usd       | The liquidity available for trading for the pair (24h rolling average, in USD). | number |
| volume_usd               | The volume of each pair opened and closed in the given snapshot (24h rolling average, in USD). | number |
| open_interest_longs_usd  | The sum of open interest of longs held for each pair, in USD. | number |
| open_interest_shorts_usd | The sum of open interest in shorts held for each pair, in USD. | number |
| liquidation_fees_usd     | The total liquidation fees accrued for each pair (24h rolling average, in USD). | number |
| funding_rate             | The funding rate for each pair at the time of the snapshot, as a percentage. | number |
| open_fees_usd            | The total open fees accrued for each pair (24h rolling average, in USD). | number |
| close_fees_usd           | The total close fees accrued for each pair (24h rolling average, in USD). | number |

### LP Snapshot

Liquidity providers snapshot (one entry for each token in a pool).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | number |
| pool_address             | The address of the pool.                                  | string |
| lp_address               | The address of the liquidity provider.                    | string |
| token_index              | The index of the token in the smart contract.             | number |
| token_address            | The address of the token provided as liquidity.           | string |
| token_symbol             | The symbol of the token.                                  | string |
| deposit_amount           | (Optional, for Order Books) The amount deposited into the pool, decimal normalized. | number |
| deposit_amount_usd       | (Optional, for Order Books) The amount deposited, in USD. | number |
| amount_useful            | (Optional, for LPs) The amount of tokens supplied that are liquid and usable by users of the protocol, decimal normalized. | number |
| amount_useful_usd        | (Optional, for LPs) The amount of liquid tokens supplied in USD. | number |
| liquidated_amount        | The amount of tokens liquidated from the LP, decimal normalized. | number |
| liquidated_amount_usd    | The amount liquidated, in USD.                            | number |
| total_fees_usd           | (Optional) All fees generated by the LP in the given snapshot in USD. | number |
| user_fees_usd            | (Optional) The portion of fees accrued to users of the protocol, in USD. | number |
| protocol_fees_usd        | (Optional) The portion of fees accrued to the protocol, in USD. | number |

### LP Snapshot (AMM)

Liquidity providers snapshot (one entry for each token in a vault).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | number |
| vault_address            | The address of the vault.                                 | string |
| lp_address               | The address of the liquidity provider.                    | string |
| token_index              | The index of the token in the smart contract.             | number |
| token_address            | The address of the token provided as liquidity.           | string |
| token_symbol             | The symbol of the token.                                  | string |
| amount_useful            | The amount of tokens supplied by the LP that are liquid and usable by users in the vault, decimal normalized. | number |
| amount_useful_usd        | The amount of liquid tokens supplied in USD.              | number |
| liquidity_change_amount  | The amount of tokens lost (indicated by negative sign) or gained (indicated by positive sign) by the LP, decimal normalized. | number |
| liquidity_amount_usd     | The amount lost or gained by the LP, in USD.              | number |
| total_lp_fees_usd        | Total fees generated for the LP at the time of snapshot (in USD). | number |

### Pool Snapshot

Snapshot of the pool's metrics.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | number |
| pool_address             | The smart contract address of the pool.                   | string |
| token_index              | The index of the token in the smart contract (one row for each token in a pool). | number |
| funding_rate             | The funding rate in this pool at the time of the snapshot, as a percentage. | number |
| fee_rate                 | he pool's fee rate, as a percentage.                      | number |
| total_value_locked_usd   | The total value locked in USD.                            | number |
| volume_usd               | The volume of positions opened and closed in the given snapshot in USD. | number |
| open_interest_longs_usd  | The sum of open interest of longs held within this pool in USD. | number |
| open_interest_shorts_usd | The sum of open interest in shorts held within this pool in USD. | number |

### Vault Snapshot (AMM)

Snapshot of the vault's metrics.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| block_date               | The timestamp truncated (ie, YYYY-MM-DD format for daily snapshots and YYYY-MM-DD HH:00:00 for hourly snapshots). | date |
| chain_id                 | Standard chain id.                                        | number |
| vault_address            | The smart contract address of the vault.                  | string |
| token_address            | The smart contract address of the token.                  | string |
| token_index              | The index of the token in the smart contract.             | number |
| token_amount             | Total Value Locked at snapshot, in tokens.                | number |
| token_amount_usd         | Total Value Locked at snapshot (amount for each token, in USD). | number |
| liquidity_available_usd  | The total liquidity available in the vault for trading, in USD. | number |
| open_interest_longs_usd  | The aggregate value of open long positions backed by the vault’s liquidity at snapshot, in USD. | number |
| open_interest_shorts_usd | The aggregate value of open short positions backed by the vault’s liquidity at snapshot, in USD. | number |
| volume_usd               | The volume of trades generated by the vault in the given snapshot (24h rolling average, in USD). | number |
| vault_fees_usd           | The portion of fees accrued by the protocol (24h rolling average, in USD). | number |

### Trades

Trade data, 1 entry for each close, open, or update of a trade.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the trade.                               | number |
| chain_id                 | Standard chain id.                                        | number |
| transaction_hash         | The hash of the transaction this trade was performed in.  | string |
| log_index                | Event log index.                                          | number |
| block_number             | The block number of the trade.                            | number |
| pool_address             | The address of the pool this token was traded in.         | string |
| maker_address            | The address of the maker.                                 | string |
| taker_address            | The address of the taker.                                 | string |
| token_address            | The address of the token.                                 | string |
| amount                   | The value that a trader is putting to open a long or short, decimal normalized. | number |
| amount_usd               | The trade amount in USD.                                  | number |
| notional_value           | The value of the leveraged amount of the trade, decimal normalized. | number |
| notional_value_usd       | The notional value, in USD.                               | number |
| maker_pnl_usd            | (Only applicable on trade close) The total profit and loss of the trade on the maker's side, in USD. | number |
| taker_pnl_usd            | (Only applicable on trade close) The total profit and loss of the trade on the taker's side, in USD. | number |
| trade_action             | The action of trade being recorded in this entry (ie, OPEN, CLOSE, INCREASE, DECREASE, LIQUIDATED). | string |
| trade_type               | The type of the trade being recorded in this entry (ie, LONG, SHORT). | string |

### Trades (AMM)

Trade data, one entry for each close, open, or update of a trade.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the trade.                               | number |
| chain_id                 | Standard chain id.                                        | number |
| transaction_hash         | The hash of the transaction this trade was performed in.  | string |
| log_index                | Event log index.                                          | number |
| block_number             | The block number of the trade.                            | number |
| pool_address             | The address of the pool this token was traded in.         | string |
| taker_address            | The address of the taker.                                 | string |
| pair_index               | The address of the pair that is traded.                   | string |
| amount                   | The value that a trader is putting (and used as collateral) to open a long or a short, decimal normalized. | number |
| amount_usd               | The trade amount in USD (if deposit is only made in stable, amount = amount_usd). | number |
| notional_value           | The value of the leveraged amount of the trade, decimal normalized. | number |
| notional_value_usd       | The notional value, in USD.                               | number |
| open_interest_longs_usd  | The aggregate value of open long positions held by the trader at snapshot, in USD. | number |
| open_interest_shorts_usd | The aggregate value of open short positions held by the trader at snapshot, in USD. | number |
| taker_pnl_usd            | (Only applicable after trade is closed) The total profit and loss of the trade on the taker's side, in USD. | number |
| trade_action             | The action of trade being recorded in this entry (ie, OPEN, CLOSE, INCREASE, DECREASE, LIQUIDATED). | string |
| trade_type               | The type of the trade being recorded in this entry (ie, LONG, SHORT). | string |
| open_fee_rate            | The open fee applied to to the taker trade, as percentage. | number |
| close_fee_rate           | The close fee applied to to the taker trade, as percentage. | number |
| open_fee_usd             | The open fee applied to to the taker trade, in USD.       | number |
| close_fee_usd            | The close fee applied to to the taker trade, in USD.      | number |
| liquidation_fee_rate     | (If applicable, i.e. PnL<0, 0 otherwise) The liquidation fee applied to to the taker trade, as percentage. | number |
| liquidation_fee_usd      | (If applicable, i.e. PnL<0, 0 otherwise) The liquidation fee applied to to the taker trade, in USD. | number |

### Incentive Claim Data

Transactional data on user level incentives claimed data.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the claim.                               | number |
| chain_id                 | The standard chain id.                                    | number |
| transaction_hash         | The hash of the transaction.                              | string |
| log_index                | The event log. For transactions that don't emit event, create arbitrary index starting from 0. | number |
| transaction_signer       | The address of the account that signed the transaction.   | string |
| user_address             | The address of the user who claimed the incentives (could be different from the transaction_signer). | string |
| claimed_token_address    | The smart contract address of the claimed token.          | string |
| amount                   | The amount of the token claimed, decimal normalized.      | number |
| amount_usd               | The amount of claimed tokens in USD.                      | number |
| other_incentive_usd      | (Optional) Any incentives outside of the claimed token, in this transaction, summed up in USD terms. | number |

> Note: This markdown file is auto-generated.
