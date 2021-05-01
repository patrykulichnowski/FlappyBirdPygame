from klasa_mainGame import MAIN_GAME

main = MAIN_GAME()
while main.running:
    main.current_menu.display_menu()
    main.main_loop()
