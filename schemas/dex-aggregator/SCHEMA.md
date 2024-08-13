# DEX Aggregator

Standard table definitions for DEX aggregators.

## Version: 1.0.0-alpha

### Tokens

List of tokens supported by the protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| chain_id                 | The standard id of the chain.                             | number |
| token_address            | The contract address of the token.                        | string |
| token_name               | The full name of the token, from the eth_call name().     | string |
| token_symbol             | The symbol of the token, from the eth_call symbol().      | string |
| decimals                 | The decimals name of the token, from the eth_call decimals(). | number |

### Token Snapshot

Volume, fees, and incentives data at the token level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the record.                              | number |
| chain_id                 | The standard id of the chain.                             | number |
| token_address            | The contract address of the token.                        | string |
| volume_amount            | The volume amount of the token, during the snapshot period, decimal normalized. | number |
| volume_usd               | The volume of the token in USD.                           | number |
| fees                     | The fees (ie, revenue generated from trading this token) from this token in native, decimal normalized terms. | number |
| fees_usd                 | The fees collected in USD.                                | number |
| incentive_amount         | The amount of incentives collected from this token, during the snapshot period, decimal normalized. | number |
| incentive_usd            | The value of incentives in USD.                           | number |

### Protocol Snapshot

Volume and fees data at the protocol level.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the block this snapshot was taken.       | number |
| chain_id                 | The standard id of the chain.                             | number |
| volume_usd               | The volume in USD, in the given snapshot period.          | number |
| fees_usd                 | The fees (ie, total revenue generated in the protocol) collected in USD, during the snapshot period. | number |

### Trades

List of trades executed on the protocol.

| Property                | Description                                               | Type   |
|-------------------------|-----------------------------------------------------------|--------|
| timestamp                | The timestamp of the trade.                               | number |
| chain_id                 | The standard id of the chain this trade belongs to.       | number |
| block_number             | The block number in which the trade occurred.             | number |
| transaction_hash         | The transaction hash associated with this trade.          | string |
| fees                     | The amount of fees from this trade (ie, the revenue generated from executing this trade). | number |
| fees_usd                 | The fees for this trade in USD.                           | number |
| slippage                 | (Optional) The slippage of the given trade, as a percentage (ie, 1.3% slippage is 0.013). | number |
| user_address             | The address of the user initiating the trade.             | string |
| input_tokens             | The contract address of the input token(s).               | [string] |
| input_token_amounts      | Parallel array to input_tokens, dictating the normalized native amounts of each token traded. | [number] |
| output_tokens            | The contract address of the output token(s).              | [string] |
| output_token_amounts     | Parallel array to output_tokens, dictating the normalized native amounts of each token traded. | [number] |
| swap_amount_usd          | The value of the swap in USD.                             | number |

> Note: This markdown file is auto-generated.
