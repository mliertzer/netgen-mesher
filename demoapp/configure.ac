AC_INIT([demoapp],[4.9.10],[])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])

AC_PREFIX_DEFAULT(["/opt/netgen"])


AC_ARG_WITH([netgen], 
        [  --with-netgen=dir       use Netgen installed in directory dir],
        [netgendir=$withval],
        [netgendir="/opt/netgen"]
        )


AC_SUBST([NETGEN_INCLUDES], ["-I$netgendir/include"])


AC_PROG_CC
AC_PROG_CXX
AC_PROG_LIBTOOL

AC_CONFIG_HEADERS(config.h) 
AC_CONFIG_FILES(Makefile windows/Makefile)

AC_OUTPUT
