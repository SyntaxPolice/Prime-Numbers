#!/bin/sh

echo '  ________________________________________
> / " know that two and two make four - and  \
> | should be glad to prove it too if I      |
> | could - though I must say if by any sort |
> | of process I could convert 2 and 2 into  |
> | five it would give me much greater       |
> \ pleasure."  - George Gordon Byron        /
>   ----------------------------------------
>          \   ^__^ 
>           \  (oo)\_______
>              (__)\       )\/\
>                  ||----w |
>                  ||     ||'

LOG=testLog-`date "+%Y-%m-%d-%H:%M:%S"`.txt

echo "Outputing to $LOG"
python test_poly_divmod.py > $LOG
python test_poly_gcd.py >> $LOG
python test_sieve.py >> $LOG
python testing.py >> $LOG
