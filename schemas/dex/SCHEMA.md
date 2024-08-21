# DEX

Standard table definitions for dex protocols.

## Version: 1.0.0

### Pools

List of LP pools in this protocol (one entry per token in a pool).

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard id of the chain.                             | number |
| creation_block_number    | The block this pool was created in.                       | number |
| creation_timestamp       | The timestamp of the block that this pool was created in. | number |
| pool_address             | The contract address of the LP pool.                      | string |
| lp_token_address         | The token address of the LP token for this pool.          | string |
| lp_token_symbol          | The symbol of the LP token.                               | string |
| token_address            | The token address of the pool token at token_index.       | string |
| token_symbol             | The symbol of the pool token.                             | string |
| token_decimals           | The decimals of the pool token.                           | string |
| token_index              | The index in the pool smart contract that this token appears at, default 0 (ie, one entry per token in a pool). | number |
| fee_rate                 | (Optional, if dynamic fee) The fee rate of the pool, as a percentage (ie, 2.3% as 0.023). | number |
| dex_type                 | The type of the DEX (ie, CPMM, CLMM, Orderbook).          | string |

### LP Position Snapshot

Snapshot of LP positions.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| chain_id                 | The standard id of the chain.                             | number |
| pool_address             | The contract address of the pool.                         | string |
| user_address             | The address of the liquidity provider.                    | string |
| token_index              | The token index based on the smart contract.              | number |
| token_address            | The contract address of the token provided as liquidity.  | string |
| token_symbol             | The symbol of the token.                                  | string |
| token_amount             | The amount of the liquidity position in the pool, decimal normalized. | number |
| token_amount_usd         | (Optional) The amount of the token in USD.                | number |

### Pool Snapshot

Snapshot of pool states.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the snapshot.                            | number |
| chain_id                 | The standard id of the chain.                             | number |
| pool_address             | The contract address of the LP pool.                      | string |
| token_index              | The token index in the smart contract.                    | number |
| token_address            | The contract address of the token in the pool.            | string |
| token_symbol             | The symbol of the token.                                  | string |
| token_amount             | The amount of the token in this pool at the snapshot.     | number |
| token_amount_usd         | (Optional) The amount of the token in USD.                | number |
| volume_amount            | The volume of the token transacted in this pool during the given snapshot, decimal normalized. | number |
| volume_usd               | (Optional) The volume transacted in the given snapshot, in USD. | number |
| fee_rate                 | The fee rate of the pool, as a percentage (ie, 2.3% as 0.023). | number |
| total_fees_usd           | (Optional) The total amount of revenue and fees paid in this pool in the given snapshot, in USD. | number |
| user_fees_usd            | (Optional) The amount of total fees accrued to liquidity providers of the protocol, in USD. | number |
| protocol_fees_usd        | (Optional) The amount of total fees accrued to the protocol, in USD. | number |

### Trades (All DEX Types)

All trades across different types of DEXs.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The log index of the event recorded.                      | number |
| transaction_hash         | The hash of the transaction.                              | string |
| user_address             | The address that initiates the transaction (ie, the transaction signer). | string |
| taker_address            | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| pair_name                | The name of the token pair.                               | string |
| pool_address             | The contract address of the LP pool being traded in.      | string |
| input_token_symbol       | The symbol of the input token.                            | string |
| input_token_address      | The contract address of the input token.                  | string |
| input_token_amount       | The amount of the input token, decimal normalized.        | number |
| output_token_symbol      | The symbol of the output token.                           | string |
| output_token_address     | The contract address of the output token.                 | string |
| output_token_amount      | The amount of the output token, decimal normalized.       | number |
| swap_amount_usd          | (Optional) The amount of the swap in USD.                 | number |
| fees_usd                 | (Optional) The fees paid by the user.                     | number |

### User Score Snapshot

Snapshot of user scores.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the record.                           | number |
| user_address             | The address of the user.                                  | string |
| pool_address             | The contract address of the pool.                         | string |
| market_depth_score       | (Ask for supporting documents and formula). The percentage price range market depth derived from a 30-day realized volatility. | number |
| total_value_locked_score | A score calculated based on TVL. Please see the methodology [here](./METHODOLOGY.md). | number |

### V2 Mints

Mint events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the mint.                             | number |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| pool_address             | The contract address of the pool.                         | string |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | number |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | number |
| mint_amount              | The amount of LP token minted by the trader, decimal normalized. | number |
| mint_amount_usd          | (Optional) The amount of the mint in USD.                 | number |

### V2 Burns

Burn events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The log index of the event recorded.                      | number |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| pool_address             | The contract address of the pool.                         | string |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | number |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | number |
| burn_amount              | The amount of LP tokens burned, decimal normalized.       | number |
| burn_amount_usd          | (Optional) The amount of the burn in USD.                 | number |

### V2 Syncs

Sync events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The log index of the event recorded.                      | number |
| transaction_hash         | The hash of the transaction.                              | string |
| pool_address             | The contract address of the pool.                         | string |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | number |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | number |

### V2 Transfers

Transfer events for V2.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The log index of the event recorded.                      | number |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The address that sends the LP token.                      | string |
| to_address               | The address that receives the LP token.                   | string |
| pool_address             | The contract address of the pool.                         | string |
| pool_token_balance       | The balance of the pool token, decimal normalized.        | number |

### V3 Events

Events for V3.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The log index of the event recorded.                      | number |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| event_type               | The action type of the event.                             | string |
| pool_address             | The contract address of the pool.                         | string |
| tick_lower               | The lower tick.                                           | number |
| tick_upper               | The upper tick.                                           | number |
| tick_spacing             | The tick spacing.                                         | number |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | number |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | number |
| token_fees               | The amount of token fees.                                 | number |
| amount_liquidity         | The amount of liquidity.                                  | number |

### V3 Transfers

Transfer events for V3.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the transaction.                         | number |
| chain_id                 | The standard id of the chain.                             | number |
| block_number             | The block number of the trade.                            | number |
| log_index                | The log index of the event recorded.                      | number |
| transaction_hash         | The hash of the transaction.                              | string |
| transaction_from_address | The address that initiates the transaction (ie, the transaction signer). | string |
| from_address             | The from address of the event (ie, the from field in a transfer). | string |
| to_address               | The to address of the event (ie, the to field in a transfer). | string |
| event_type               | The action type of the event.                             | string |
| pool_address             | The contract address of the pool.                         | string |
| tick_lower               | The lower tick.                                           | number |
| tick_upper               | The upper tick.                                           | number |
| tick_spacing             | The tick spacing.                                         | number |
| token0_address           | The contract address of token0.                           | string |
| token0_amount            | The amount of token0.                                     | number |
| token1_address           | The contract address of token1.                           | string |
| token1_amount            | The amount of token1.                                     | number |
| token_fees               | The amount of token fees.                                 | number |
| amount_liquidity         | The amount of liquidity.                                  | number |

> Note: This markdown file is auto-generated.
