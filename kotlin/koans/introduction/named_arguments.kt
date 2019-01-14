fun joinToString(
    separator: String = ", ",
    prefix: String = "",
    postfix: String = "",
    /* ... */
): String


fun joinOptions(options: Collection<String>) = options.joinToString(
prefix="[", postfix="]"
)