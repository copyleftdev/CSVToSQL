n=1
max=50
set -- # this sets $@ [the argv array] to an empty list.

while [ "$n" -le "$max" ]; do
    set -- "$@" "s$n" # this adds s$n to the end of $@
    n=$(( $n + 1 ));
done

mkdir "$@"
