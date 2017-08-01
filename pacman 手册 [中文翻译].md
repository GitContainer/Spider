# pacman 手册 [中文翻译]

目录

[概要](https://www.archlinux.org/pacman/pacman.8.html#_synopsis)

[描述](https://www.archlinux.org/pacman/pacman.8.html#_description)

[操作](https://www.archlinux.org/pacman/pacman.8.html#_operations)

[选项](https://www.archlinux.org/pacman/pacman.8.html#_options)

[事务选项（适用于-S，-R和-U）](https://www.archlinux.org/pacman/pacman.8.html#_transaction_options_apply_to_em_s_em_em_r_em_and_em_u_em)

[升级选项（适用于-S和-U）](https://www.archlinux.org/pacman/pacman.8.html#_upgrade_options_apply_to_em_s_em_and_em_u_em_a_id_uo_a)

[查询选项](https://www.archlinux.org/pacman/pacman.8.html#_query_options_a_id_qo_a)

[删除选项](https://www.archlinux.org/pacman/pacman.8.html#_remove_options_a_id_ro_a)

[同步选项](https://www.archlinux.org/pacman/pacman.8.html#_sync_options_a_id_so_a)

[数据库选项](https://www.archlinux.org/pacman/pacman.8.html#_database_options_a_id_qo_a)

[文件选项](https://www.archlinux.org/pacman/pacman.8.html#_file_options_a_id_fo_a)

[处理配置文件](https://www.archlinux.org/pacman/pacman.8.html#_handling_config_files_a_id_hcf_a)

[例子](https://www.archlinux.org/pacman/pacman.8.html#_examples)

[组态](https://www.archlinux.org/pacman/pacman.8.html#_configuration)

[也可以看看](https://www.archlinux.org/pacman/pacman.8.html#_see_also)

[错误](https://www.archlinux.org/pacman/pacman.8.html#_bugs)

[作者](https://www.archlinux.org/pacman/pacman.8.html#_authors)

## 名称

pacman - 包管理器实用程序

## 概要

*pacman* <operation> [options] [targets]

## 描述

Pacman是用于跟踪Linux系统上已安装软件包的软件包管理实用程序。它具有依赖关系支持，软件包组，安装和卸载脚本，以及将本地计算机与远程存储库同步以自动升级软件包的功能。Pacman包是压缩的tar格式。

自3.0.0版起，pacman已经是[libalpm（3）](https://www.archlinux.org/pacman/libalpm.3.html)的前端，即“Arch Linux软件包管理”库。该库允许编写备用前端（例如，GUI前端）。

调用pacman涉及指定具有可操作的任何潜在选项和目标的操作。一个*目标*通常是包名，文件名，URL或搜索字符串。目标可以作为命令行参数提供。另外，如果stdin不是从一个终端，一个连字符（ - ）作为参数传递，目标将从stdin读取。

## 操作

- **-D, --database**

  在包数据库上操作。此操作允许您修改pacman数据库中已安装软件包的某些属性。它还允许您检查数据库的内部一致性。见下面的[数据库选项](https://www.archlinux.org/pacman/pacman.8.html#DO)。

- **-Q, --query**

  查询包数据库。此操作允许您查看已安装的软件包及其文件，以及有关各个软件包（依赖关系，冲突，安装日期，构建日期，大小）的元信息。这可以针对本地包数据库运行，也可以在单个包文件上使用。在第一种情况下，如果在命令行中没有提供软件包名称，则将查询所有已安装的软件包。此外，各种过滤器可以应用于包装清单上。参见下面的[查询选项](https://www.archlinux.org/pacman/pacman.8.html#QO)。

- **-R, --remove**

  从系统中删除软件包。组也可以指定删除，在这种情况下，该组中的每个包将被删除。属于指定包的文件将被删除，数据库将被更新。大多数配置文件将使用*.pacsave*扩展名保存，除非使用了*--nosave*选项。请参阅下面的 [删除选项](https://www.archlinux.org/pacman/pacman.8.html#RO)

- **-S，--sync**

  同步包 软件包直接从远程存储库安装，包括运行软件包所需的所有依赖项。例如，`pacman -S qt`将下载并安装qt及其所依赖的所有软件包。如果一个包名称存在于多个存储库中，则可以明确指定存储库以澄清要安装的包：`pacman -S testing/qt`。您还可以指定版本要求：`pacman -S "bash>=3.2"`。需要引用，否则shell将“>”解释为重定向到文件。除了包之外，还可以指定组。例如，如果gnome是定义的包组，`pacman -S gnome`则会提供一个提示，允许您从编号列表中选择要安装的包。软件包选择使用空格和/或逗号分隔的软件包编号列表指定。可以通过指定由连字符（`-`）分隔的第一个和最后一个包编号来选择顺序包。通过用数字或范围的数字与caret（`^`）前缀来实现排除包。还提供其他软件包的软件包。例如，`pacman -S foo`将首先查找一个foo包。如果没有找到foo，将搜索提供与foo相同功能的软件包。如果找到任何包，它将被安装。如果找到提供foo的多个包，则提供选择提示。您还可以使用`pacman -Su`升级所有过期的软件包。请参阅 下面[同步选项](https://www.archlinux.org/pacman/pacman.8.html#SO)。升级时，pacman执行版本比较，以确定哪些软件包需要升级。此行为如下：`Alphanumeric:  1.0a < 1.0b < 1.0beta < 1.0p < 1.0pre < 1.0rc < 1.0 < 1.0.a < 1.0.1Numeric:  1 < 1.0 < 1.1 < 1.1.1 < 1.2 < 2.0 < 3.0.0`此外，版本字符串可以具有定义的*时期*值，这将超过任何版本比较，除非时期值相等。这是以`epoch:version-rel`格式指定的。例如，`2:1.0-1`总是大于`1:3.6-1`。

- **-T, --deptest**

  检查依赖关系 这在诸如makepkg的脚本中可用于检查已安装的软件包。此操作将检查指定的每个依赖关系，并返回系统当前不满足的依赖关系列表。此操作不接受任何其他选项。使用示例：`pacman -T qt "bash>=3.2"`。

- **-U, --upgrade**

  升级或添加软件包到系统并从同步存储库安装所需的依赖关系。可以指定URL或文件路径。这是一个“remove-then-add”过程。请参阅下面的[升级选项 ](https://www.archlinux.org/pacman/pacman.8.html#UO)另请参阅[处理配置文件](https://www.archlinux.org/pacman/pacman.8.html#HCF)以了解pacman如何处理配置文件。

- **-F, --files**

  查询文件数据库。此操作允许您查找拥有特定文件的包或某些包所有的显示文件。只搜索同步数据库的一部分包。参见 下面的[文件选项](https://www.archlinux.org/pacman/pacman.8.html#FO)。

- **-V，--version**

  显示版本并退出。

- **-h，--help**

  显示给定操作的语法。如果没有提供操作，则会显示一般语法。

## 选项

- **-b，--dbpath** <path>

  指定备用数据库位置（典型的默认值 `/var/lib/pacman`）。这不应该被使用，除非你知道你在做什么。 **注意**：如果指定，这是绝对路径，根路径不会自动添加。

- **-r，--root** <path>

  指定备用安装根（默认为`/`）。这不应该用作安装软件`/usr/local`而不是 `/usr`。如果要在由另一个系统“拥有”的临时安装的分区上安装软件包，则会使用此选项。 **注意**：如果在命令行或[pacman.conf（5）](https://www.archlinux.org/pacman/pacman.conf.5.html)中未指定数据库路径或日志文件，则其默认位置将位于此根路径内。

- **-v，--verbose**

  输出路径，如Root，Conf File，DB Path，Cache Dirs等

- **--arch** <arch>

  指定备用架构。

- **--cachedir** <dir>

  指定替代包缓存位置（典型的默认值 `/var/cache/pacman/pkg`）。可以指定多个缓存目录，并按照传递给pacman的顺序进行尝试。 **注意**：这是绝对路径，根路径不会自动添加。

- **--color** <when>

  指定何时启用着色。有效的选项是*永远*，*永不*或 *自动*。*总是*强制颜色; *永远不会*强制颜色关闭 而*自动*只能在输出到tty时自动启用颜色。

- **--config** <file>

  指定备用配置文件。

- **--debug**

  显示调试消息。报告错误时，建议使用此选项。

- **--gpgdir** <dir>

  指定GnuPG使用的文件目录来验证包签名（典型的默认值`/etc/pacman.d/gnupg`）。此目录应包含两个文件：`pubring.gpg`和`trustdb.gpg`。`pubring.gpg`持有所有包装商的公钥。`trustdb.gpg`包含一个所谓的信任数据库，它指定这些密钥是真实可信的。**注意**：这是绝对路径，根路径不会自动添加。

- **--hookdir** <dir>

  指定一个包含钩子文件的备用目录（一个典型的默认值 `/etc/pacman.d/hooks`）。可以使用以前的目录中的钩子优先的后续目录中的钩子指定多个挂钩目录。**注意**：这是绝对路径，根路径不会自动添加。

- **--logfile** <file>

  指定备用日志文件。无论安装根设置如何，这是一个绝对路径。

- **--noconfirm**

  绕过任何和所有“你确定吗？”消息。除非你想从脚本运行pacman，这不是一个好主意。

- **--confirm**

  取消先前的*--noconfirm*的影响。

## 事务选项（适用于*-S*，*-R*和*-U*）

- **-d，--nodeps**

  跳过依赖版本检查。软件包名称仍然被检查。通常，pacman将始终检查包的依赖关系字段，以确保所有依赖关系都已安装，并且系统中没有包冲突。指定此选项两次以跳过所有依赖关系检查。

- **--assume-installed** <package = version>

  将一个带有版本“version”的虚拟包“package”添加到事务中以满足依赖关系。这允许禁用特定的依赖关系检查，而不影响所有依赖关系检查 要禁用所有依赖关系检查，请参阅*--nodeps*选项。

- **--dbonly**

  仅添加/删除数据库条目，保留所有文件。

- **--noprogressbar**

  下载文件时不要显示进度条。这可以用于调用pacman并捕获输出的脚本。

- **--noscriptlet**

  如果存在安装脚本，请不要执行它。不要使用它，除非你知道你在做什么。

- **-p，--print**

  只打印目标，而不是执行实际操作（同步，删除或升级）。使用*--print-format*指定目标的显示方式。默认格式字符串为“％l”，显示带*-S的* URL， 带*-U的*文件名和带*-R的* pkgname-pkgver 。

- **--print-format** <format>

  指定一个printf格式来控制*--print* 操作的输出。可能的属性有：pkgname的“％n”，pkgver的“％v”，位置的“％l”，存储库的“％r”和大小的“％s”。暗示 - *印*。

## 升级选项（适用于*-S*和*-U*）

- **- force**

  旁路文件冲突检查并覆盖冲突文件。如果要安装的软件包包含已安装的文件，则此选项将导致所有这些文件被覆盖。使用*--force*将不允许使用文件覆盖目录或安装具有冲突文件和目录的软件包。该选项应该谨慎使用，理想情况下根本不用。

- **--asdeps**

  非包装安装包; 换句话说，假装他们的安装原因被安装为依赖。这对于在构建包之前需要安装依赖关系的makepkg和其他源代码工具非常有用。

- **--asexplicit**

  明确安装包; 换句话说，假装他们的安装原因要被明确的安装。如果要将依赖项标记为显式安装，则不会被*--recursive* remove操作删除。

- **--ignore** <package>

  指示pacman忽略包的升级，即使有一个可用。可以使用逗号分隔多个包。

- **--ignoregroup** <group>

  指示pacman忽略*组*中所有包的升级，即使有一个可用。可以使用逗号分隔多个组。

- **--needed**

  不要重新安装已经是最新的目标。

## 查询选项

- **-c，--changelog**

  查看包的ChangeLog（如果存在）。

- **-d，--deps**

  限制或过滤输出到作为依赖关系安装的包。此选项可以与*-t*组合以列出真正的孤儿 - 作为依赖关系安装但不再需要安装的软件包的软件包。

- **-e，-explicit**

  限制或过滤输出到显式安装的包。此选项可以与*-t*组合以列出任何其他软件包不需要的显式安装的软件包。

- **-g，--groups**

  显示作为命名组成员的所有软件包。如果未指定名称，请列出所有分组的包。

- **-i，--info**

  显示给定包的信息。该*-p*选项，如果查询包文件，而不是本地数据库中。传递两个 *--info*或*-i*标志也将显示备份文件及其修改状态列表。

- **-k - check**

  检查系统中是否存在给定包所有的所有文件。如果未指定包或未提供过滤器标志，请检查所有安装的包。指定此选项两次将对包含所需mtree文件的软件包执行更详细的文件检查（包括权限，文件大小和修改时间）。

- **-l，--list**

  列出给定包所有的所有文件。可以在命令行中指定多个包。

- **-m， - foreign**

  限制或过滤输出到在同步数据库中未找到的包。通常这些是手动下载并使用*--upgrade*安装的*软件包*。

- **-n，-native**

  限制或过滤输出到在同步数据库中找到的包。这是*--foreign*的反向过滤器。

- **-o，--owns** <file>

  搜索拥有指定文件的包。该路径可以是相对的或绝对的，并且可以指定一个或多个文件。

- **-p，--file**

  表示在命令行中提供的包是数据库中的文件，而不是数据库中的条目。该文件将被解压缩和查询。这与*--info*和*--list*组合很有*用*。

- **-q，--quiet**

  显示某些查询操作的信息较少。当在脚本中处理pacman的输出时，这是非常有用的。搜索只显示包名，而不是版本，组和描述信息; 拥有者只会显示软件包名称而不是“文件由pkg拥有”消息; 组只会显示包名，省略组名; 列表将仅显示文件并省略包名称; 检查只会显示包名和丢失的文件; 一个裸查询只会显示包名，而不是名称和版本。

- **-s，--search** <regexp>

  搜索每个本地安装的包，以获取匹配的名称或描述`regexp`。当包含多个搜索字词时，只返回与所有这些条款匹配的描述的包。

- **-t， - unrequired**

  限制或过滤输出到任何当前安装的软件包不需要或可选地需要的软件包。指定此选项两次，以仅过滤直接依赖关系的包（即不过滤可选依赖关系）。

- **-u， - upgrades**

  限制或过滤输出到本地系统上已过期的包。仅使用包版本来查找过期的包; 这里没有检查更换。如果使用*-Sy*刷新同步数据库，则此选项最有效。

## 删除选项

- **-c， - cascade**

  删除所有目标软件包，以及依赖于一个或多个目标软件包的所有软件包。此操作是递归的，必须谨慎使用，因为它可以删除许多可能需要的包。

- **-n， - nosave**

  指示pacman忽略文件备份指定。通常，当从系统中删除文件时，将检查数据库以查看该文件是否应使用*.pacsave*扩展名重命名。

- **-s，--recursive**

  删除指定的每个目标，包括其所有的依赖项，前提是（A）它们不是其他软件包所要求的; 和（B）它们没有被用户显式安装。此操作是递归的，类似于向后*同步*操作，它有助于保持干净的系统，而无需孤儿。如果要省略条件（B），请将此选项传递两次。

- **-u, --unneeded**

  删除任何其他软件包不需要的目标。删除组而不使用*-c*选项时，这是非常有用的，以避免破坏任何依赖关系。

## 同步选项

- **-c, --clean**

  从缓存中删除不再安装的软件包以及当前未使用的同步数据库以释放磁盘空间。当pacman下载软件包时，它将它们保存在缓存目录中。此外，数据库将为您下载的每个同步数据库保存，即使它们从配置文件[pacman.conf（5）中](https://www.archlinux.org/pacman/pacman.conf.5.html)删除也不会被删除 。使用一个*清洁*开关仅删除不再安装的包; 使用两个从缓存中删除所有文件。在这两种情况下，您将有一个“是”或“否”选项来删除软件包和/或未使用的下载数据库。如果使用网络共享缓存，请参阅[pacman.conf（5）中](https://www.archlinux.org/pacman/pacman.conf.5.html)的*CleanMethod*选项 。

- **-g，--groups**

  显示指定的每个包组的所有成员。如果没有提供组名，所有组将被列出; 通过标志两次以查看所有组及其成员。

- **-i，--info**

  显示给定同步数据库包的信息。传递两个*-info* 或*-i*标志也将在依赖此包的所有存储库中显示这些包。

- **-l，--list**

  列出指定资料库中的所有包。可以在命令行中指定多个存储库。

- **-q，--quiet**

  显示某些同步操作的信息较少。当在脚本中处理pacman的输出时，这是非常有用的。搜索只显示包名，而不是存储库，版本，组和描述信息; 列表将仅显示包名称并省略数据库和版本; 组将仅显示包名称并省略组名称。

- **-s，--search** <regexp>

  这将搜索同步数据库中的每个包，以匹配匹配的名称或描述`regexp`。当您包含多个搜索字词时，只会返回与所有这些条款相匹配的说明。

- **-u，--supupgrade**

  升级所有过期的软件包。如果存在较新的软件包，则每个当前安装的软件包将被检查和升级。将显示所有要升级的软件包的报告，如果没有用户确认，操作将不会进行。依赖关系将在此级别自动解决，并在必要时进行安装/升级。通过此选项两次以启用程序包降级; 在这种情况下，pacman将选择与本地版本不匹配的同步包。当用户从测试库切换到稳定的存储库时，这将非常有用。还可以手动指定附加目标，以便*-Su foo*在同一操作中进行系统升级并安装/升级“foo”软件包。

- **-w，--downloadonly**

  从服务器检索所有包，但不要安装/升级任何东西。

- **-y，--refresh**

  从[pacman.conf（5）中](https://www.archlinux.org/pacman/pacman.conf.5.html)定义的服务器下载主包数据库的新副本。通常每次使用*-sysupgrade*或*-u*时都应该使用*它*。传递两个*--refresh*或*-y*标志将强制刷新所有包数据库，即使它们看起来是最新的。

## 数据库选项

- **--asdeps** <package>

  将包标记为非显式安装; 换句话说，将安装原因设置为依赖。

- **--asexplicit <包>**

  将包标记为显式安装; 换句话说，将安装原因设置为明确安装。这是有用的，你想保持一个包安装，即使它最初安装作为另一个包的依赖。

- **-k --check**

  检查本地包数据库内部是否一致。这将检查所有必需的文件是否存在，并且已安装的软件包具有所需的依赖关系，不要冲突，并且多个软件包不拥有相同的文件。两次指定此选项将对同步数据库执行检查，以确保所有指定的依赖关系可用。

## 文件选项

- **-y，--refresh**

  从服务器下载新的包数据库。使用两次以强制刷新即使数据库是最新的。

- **-l，--list**

  列出查询包所有的文件。

- **-s，--search**

  搜索匹配字符串的包文件名。

- **-x，--regex**

  治疗参数*-搜索*正则表达式。

- **-o，--owns**

  搜索拥有特定文件的包。

- **-q，--quiet**

  显示某些文件操作的信息较少。当在脚本中处理pacman的输出时，这很有用，但是您可能希望使用 *--machinereadable*。

- **--machinereadable**

  使用*--list*，-- *search*和 *--owns*的机器可读输出格式。格式为*repository \ 0pkgname \ 0pkgver \ 0path \ n，*其中*\ 0* 为NULL字符，*\ n*为换行符。

## 处理配置文件

Pacman使用与*rpm*相同的逻辑来确定对指定要备份的文件的操作。在升级过程中，每个备份文件都使用三个MD5散列，以确定所需的操作：一个用于安装原始文件，一个用于要安装的新文件，另一个用于文件系统上存在的实际文件。在比较这三个哈希后，可以得出以下情况：

- original = X，current = X，new = X

  所有三个文件是一样的，所以覆盖不是一个问题。安装新文件。

- original = X，current = X，new = Y

  当前文件与原始文件相同，但新的文件不同。由于用户没有修改该文件，并且新的文件可能包含改进或错误修复，请安装新文件。

- original = X，current = Y，new = X

  两个软件包版本都包含完全相同的文件，但文件系统中的文件已被修改。将当前文件保留到位。

- original = X，current = Y，new = Y

  新文件与当前文件相同。安装新文件。

- original = X，current = Y，new = Z

  所有这三个文件是不同的，所以使用*.pacnew* 扩展名安装新文件并警告用户。用户必须手动将任何必要的更改合并到原始文件中。

- original = NULL，current = Y，new = Z

  该软件包以前未安装，该文件已存在于文件系统上。使用*.pacnew*扩展名安装新文件，*并向*用户发出警告。用户必须手动将任何必要的更改合并到原始文件中。

## 例子

- pacman -Ss ne.hack

  在包数据库中搜索regexp“ne.hack”。

- pacman -S gpm

  下载并安装gpm，包括依赖关系。

- pacman -U /home/user/ceofhack-0.6-1-x86_64.pkg.tar.gz

  从本地文件安装ceofhack-0.6-1包。

- pacman -Syu

  更新包列表，然后升级所有包。

- pacman -Syu gpm

  更新包列表，升级所有包，然后安装gpm（如果尚未安装）。

## 组态

有关使用*pacman.conf*文件配置pacman的更多详细信息， 请参阅[pacman.conf（5）](https://www.archlinux.org/pacman/pacman.conf.5.html)。**

## 也可以看看

[pacman.conf（5）](https://www.archlinux.org/pacman/pacman.conf.5.html)，[makepkg（8）](https://www.archlinux.org/pacman/makepkg.8.html)，[libalpm（3）](https://www.archlinux.org/pacman/libalpm.3.html)

有关pacman 及其相关工具的最新信息，请访问pacman网站：[https：](https://www.archlinux.org/pacman/) //www.archlinux.org/pacman/。

## 错误

错误？你一定在开玩笑; 这个软件没有错误。但是如果我们错误的话，给我们发送一封尽可能详细的电子邮件给 [pacman-dev@archlinux.org](mailto:pacman-dev@archlinux.org)。

## 作者

当前维护者：

- Allan McRae < [allan@archlinux.org](mailto:allan@archlinux.org) >
- Andrew Gregory < [andrew.gregory.8@gmail.com](mailto:andrew.gregory.8@gmail.com) >
- Dan McGee < [dan@archlinux.org](mailto:dan@archlinux.org) >
- Dave Reisner < [dreisner@archlinux.org](mailto:dreisner@archlinux.org) >

过去主要贡献者：

- Judd [Vinet](mailto:jvinet@zeroflux.org) < [jvinet@zeroflux.org](mailto:jvinet@zeroflux.org) >
- Aurelien Foret < [aurelien@archlinux.org](mailto:aurelien@archlinux.org) >
- Aaron Griffin < [aaron@archlinux.org](mailto:aaron@archlinux.org) >
- Xavier Chantry < [shiningxc@gmail.com](mailto:shiningxc@gmail.com) >
- Nagy Gabor < [ngaba@bibl.u-szeged.hu](mailto:ngaba@bibl.u-szeged.hu) >

对于其他贡献者，请`git shortlog -s`在pacman.git存储库中使用。

最后更新2016-01-29 09:50:49 AEST