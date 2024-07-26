# DEX Schema

This is OpenBlock Labs standard DEX schema.

## Schema

### Pools
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| chain_id              | The standard id of the chain.                                        | number |
| creation_block_number | The block this pool was created in.                                  | number |
| creation_timestamp    | The timestamp of the block that this pool was created in.            | number |
| pool_address          | The contract address of the lp pool.                                 | string |
| lp_token_address      | The token address of the LP token for this pool.                     | string |
| lp_token_symbol       | The symbol of the LP token.                                          | string |
| token_address         | The token address of the pool token at token_index.                  | string |
| token_index           | The index in the pool smart contract that this token appears at (ie, one entry per token in a pool).     | number |
| fee_rate              | The fee rate of the pool, as a percentage.                           | number |
| dex_type              | The type of the DEX (ie, CPMM, CLMM, Orderbook).                   | string |

### LP Position Snapshot
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the snapshot.                                       | number |
| chain_id              | The standard id of the chain.                                        | number |
| pool_address          | The contract address of the pool.                                    | string |
| lp_address            | The address of the liquidity provider.                               | string |
| token_index           | The token index based on the smart contract.                         | number |
| token_address         | The contract address of the token provided as liquidity.             | string |
| token_symbol          | The symbol of the token.                                             | string |
| token_amount          | The amount of the liquidity position in the pool, decimal normalized.| number |
| token_amount_usd      | (Optional) The amount of the token in USD.                                      | number |

### Pool Snapshot
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the snapshot.                                       | number |
| chain_id              | The standard id of the chain.                                        | number |
| pool_address          | The contract address of the LP pool.                                 | string |
| token_index           | The token index in the smart contract.                               | number |
| token_address         | The contract address of the token in the pool.                       | string |
| token_symbol          | The symbol of the token.                                             | string |
| token_amount          | The amount of the token in this pool at the snapshot.                | number |
| token_amount_usd      | (Optional) The amount of the token in USD.                                      | number |
| volume_amount         | The volume of the token transacted in this pool during the given snapshot, decimal normalized. | number |
| volume_usd            | (Optional) The volume transacted in the given snapshot, in USD.                 | number |
| total_fees_usd        | (Optional) The total amount of revenue and fees paid in this pool in the given snapshot, in USD.      | number |
| user_fees_usd         | (Optional) The amount of total fees accrued to liquidity providers of the protocol, in USD. | number |
| protocol_fees_usd     | (Optional) The amount of total fees accrued to the protocol, in USD.            | number |

### Trades (All DEX Types)
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the transaction.                                    | number |
| chain_id              | The standard id of the chain.                                        | number |
| block_number          | The block number of the trade.                                       | number |
| log_index             | The log index of the event recorded.                                 | number |
| transaction_hash      | The hash of the transaction.                                         | string |
| user_address          | The address that initiates the transaction (ie, the transaction signer). | string |
| contract_address      | The smart contract address the user interacted with (ie, transaction to). | string |
| taker_address         | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| pair_name             | The name of the token pair.                                          | string |
| pool_address          | The contract address of the LP pool being traded in.                 | string |
| input_token_symbol    | The symbol of the input token.                                       | string |
| input_token_address   | The contract address of the input token.                             | string |
| input_token_amount    | The amount of the input token, decimal normalized.                   | number |
| output_token_symbol   | The symbol of the output token.                                      | string |
| output_token_address  | The contract address of the output token.                            | string |
| output_token_amount   | The amount of the output token, decimal normalized.                  | number |
| swap_amount_usd       | (Optional) The amount of the swap in USD.                                       | number |
| fees_usd              | (Optional) The fees paid by the user                                          | number |

### User Score Snapshot
| Property                | Description                                                                                     | Type   |
|-------------------------|-------------------------------------------------------------------------------------------------|--------|
| timestamp               | The timestamp of the record.                                                                    | number |
| chain_id                | The standard id of the chain.                                                                   | number |
| block_number            | The block number of the record.                                                                 | number |
| user_address            | The address of the user.                                                                        | string |
| pool_address            | The contract address of the pool.                                                               | string |
| market_depth_score      | (Ask for supporting documents and formula). The percentage price range market depth derived from a 30-day realized volatility. | number |
| total_value_locked_score | (Ask for supporting documents and formula). A score calculated based on TVL.                   | number |

## Event Data

### V2 Mints
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the record.                                         | number |
| chain_id              | The standard id of the chain.                                        | number |
| block_number          | The block number of the mint.                                        | number |
| user_address          | The address of the user who initiated this event.                    | string |
| pool_address          | The contract address of the pool.                                    | string |
| token0_address        | The contract address of token0.                                      | string |
| token0_amount         | The amount of token0.                                                | number |
| token1_address        | The contract address of token1.                                      | string |
| token1_amount         | The amount of token1.                                                | number |
| mint_amount           | The amount of LP token minted by the trader, decimal normalized.     | number |
| mint_amount_usd       | (Optional) The amount of the mint in USD.                                       | number |

### V2 Burns
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the transaction.                                    | number |
| chain_id              | The standard id of the chain.                                        | number |
| block_number          | The block number of the trade.                                       | number |
| log_index             | The log index of the event recorded.                                 | number |
| transaction_hash      | The hash of the transaction.                                         | string |
| user_address          | The address that initiates the transaction (ie, the transaction signer). | string |
| contract_address      | The smart contract address the user interacted with (ie, transaction to). | string |
| taker_address         | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| pool_address          | The contract address of the pool.                                    | string |
| token0_address        | The contract address of token0.                                      | string |
| token0_amount         | The amount of token0.                                                | number |
| token1_address        | The contract address of token1.                                      | string |
| token1_amount         | The amount of token1.                                                | number |
| burn_amount           | The amount of LP tokens burned, decimal normalized.                  | number |
| burn_amount_usd       | (Optional) The amount of the burn in USD.                                       | number |

###  V2 Syncs
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the transaction.                                    | number |
| chain_id              | The standard id of the chain.                                        | number |
| block_number          | The block number of the trade.                                       | number |
| log_index             | The log index of the event recorded.                                 | number |
| transaction_hash      | The hash of the transaction.                                         | string |
| user_address          | The address that initiates the transaction (ie, the transaction signer). | string |
| contract_address      | The smart contract address the user interacted with (ie, transaction to). | string |
| taker_address         | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| pool_address          | The contract address of the pool.                                    | string |
| token0_address        | The contract address of token0.                                      | string |
| token0_amount         | The amount of token0.                                                | number |
| token1_address        | The contract address of token1.                                      | string |
| token1_amount         | The amount of token1.                                                | number |

### V2 Transfers
| Property              | Description                                                          | Type   |
|-----------------------|----------------------------------------------------------------------|--------|
| timestamp             | The timestamp of the transaction.                                    | number |
| chain_id              | The standard id of the chain.                                        | number |
| block_number          | The block number of the trade.                                       | number |
| log_index             | The log index of the event recorded.                                 | number |
| transaction_hash      | The hash of the transaction.                                         | string |
| user_address          | The address that initiates the transaction (ie, the transaction signer). | string |
| contract_address      | The smart contract address the user interacted with (ie, transaction to). | string |
| taker_address         | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| pool_address          | The contract address of the pool.                                    | string |
| pool_token_balance    | The balance of the pool token, decimal normalized.                   | number |

### V3 Events
| Property                | Description                                                      | Type   |
|-------------------------|------------------------------------------------------------------|--------|
| timestamp               | The timestamp of the transaction.                                    | number |
| chain_id                | The standard id of the chain.                                        | number |
| block_number            | The block number of the trade.                                       | number |
| log_index               | The log index of the event recorded.                                 | number |
| transaction_hash        | The hash of the transaction.                                         | string |
| user_address            | The address that initiates the transaction (ie, the transaction signer). | string |
| contract_address        | The smart contract address the user interacted with (ie, transaction to). | string |
| taker_address           | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| event_type              | The action taken (Mint/Burn/Transfer).                           | string |
| pool_address            | The contract address of the pool.                                | string |
| token_address           | The contract address of the token.                               | string |
| liquidity_amount        | The amount of liquidity, decimal normalized.                                | number |
| liquidity_usd           | (Optional) The liquidity amount in USD.                                     | number |
| tick_lower              | The lower tick of the liquidity range.                           | number |
| tick_upper              | The upper tick of the liquidity range.                           | number |
| tick                    | The current tick.                                                | number |

### V3 Swaps
| Property                | Description                                                      | Type   |
|-------------------------|------------------------------------------------------------------|--------|
| timestamp               | The timestamp of the transaction.                                    | number |
| chain_id                | The standard id of the chain.                                        | number |
| block_number            | The block number of the trade.                                       | number |
| log_index               | The log index of the event recorded.                                 | number |
| transaction_hash        | The hash of the transaction.                                         | string |
| user_address            | The address that initiates the transaction (ie, the transaction signer). | string |
| contract_address        | The smart contract address the user interacted with (ie, transaction to). | string |
| taker_address           | The taker, the address that receives the output of the swap (ie, could be the same as user_address unless a proxy contract/router is used). | string |
| pool_address            | The contract address of the pool.                                | string |
| liquidity_amount        | The liquidity field emitted in a V3 event, decimal normalized.   | number |
| token0_amount           | The amount of token0 involved in the swap.                       | number |
| token1_amount           | The amount of token1 involved in the swap.                       | number |
| sqrt_price_x96          | The square root of the price multiplied by 2^96.                 | number |
| tick                    | The current tick.                                                | number |
