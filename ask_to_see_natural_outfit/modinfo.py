#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'AskToSeeNaturalOutfit'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'ask_to_see_natural_outfit'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '0.0.2'


r"""
v0.0.2
    Folder Cleanup
    Renamed '_19_/o19_ask_to_see_natural_outfit.package' to '_19_/ask_to_see_natural_outfit.package' - delete the old file when updating from v0.0.1
v0.0.1
"""