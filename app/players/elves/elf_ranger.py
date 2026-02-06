from ..elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self._bow_level = bow_level

    def play_elf_song(self) -> None:
        print(f""
              f"{self.nickname} is playing a "
              f"song on the {self._musical_instrument}")

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow "
            f"of the {self._bow_level} level"
        )

    def get_rating(self) -> int:
        return 3 * self._bow_level