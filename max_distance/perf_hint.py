import typing as T

Linear = T.Literal['linear']
Log = T.Literal['log']
Square = T.Literal['square']

PerfHint = T.Literal[Linear, Log, Square]