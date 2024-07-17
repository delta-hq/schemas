# Liquid Staking Tokens (LSTs) Schema

This is the OpenBlock Labs standard schema for liquid staking tokens.

## Schema

### Position Snapshot

**Description:** User level snapshot of holders in this protocol.

| Property      | Description                                                      | Type   |
|---------------|------------------------------------------------------------------|--------|
| timestamp     | The timestamp of the snapshot.                                   | number |
| protocolName  | The name of the protocol.                                        | string |
| chainId       | Standard chain ID.                                               | number |
| tokenAddress  | The address of the LST in the protocol.                          | string |
| tokenSymbol   | The symbol of the token.                                         | string |
| userAddress   | The address of the user holding the LST.                         | string |
| amount        | The amount of LST tokens held in the protocol, decimal normalized. | number |
| amountUsd     | The amount held in USD.                                          | number |

### Protocol Snapshot

**Description:** Snapshot at the protocol level, including TVL and fees data.

| Property      | Description                                                                              | Type   |
|---------------|------------------------------------------------------------------------------------------|--------|
| timestamp     | The timestamp of the snapshot.                                                           | number |
| protocolName  | The name of the protocol.                                                                | string |
| chainId       | Standard chain ID.                                                                       | number |
| tvlUsd        | The total value locked in USD (ie, the value of the liquid staking tokens in the protocol). | number |
| feesUsd       | The fees collected in USD in the given snapshot period.                                  | number |
