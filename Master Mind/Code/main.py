import MasterMind as mtm


def main():
  game = mtm.MTMEngine()

  computerColors = game.GetComputerColorList()

  while True:
    results = game.CompareColorLists(game.GetUserInputColorList(),
                                     computerColors)

    if results["Correct colors"] == 4:
      game.Victory()
      break

    print(f"\nColors you got right with position: {results['Correct colors']}")
    print(f"Colors you misplaced: {results['Misplaced colors']}")

    choice = input("\nIf you want to quit enter '-1 else press enter :")

    if (choice == "-1") :
      game.Lost(computerColors)
      break

if __name__ == "__main__":
  main()
