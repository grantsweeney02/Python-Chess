# Grant Sweeney - gcx8yv& Robert Stambaugh - mjk3rn
# Orginal Idea (CP #1)
# The game my partner and I are going to make is chess. We will make it object-oriented with each piece being its own
# object. It is under the assumption that the players know how each piece can move in certain situations. For
# example, the players should know that their knight can jump two spaces vertically or horizontally and the one to
# the left, right, up, or down. It is also under the assumption that if a piece is in a players piece's way,
# it cannot make that move unless it is the knight, which then, it can jump it. The game will end when
# a player's King dies. The players will be removed when they die and
# placed at the bottom of the screen.

# Required Features:
# 1. User Input - The user will click pieces and click where they want to move that piece.
# 2. Start Screen -  The start screen will have our names, ID's, and the game instructions.
# 3. Game Over - The game ends when the King dies, prints out game over, and the king is returned to its original
# position.
# 4. Small Enough Window - Our game box is 400x600.
# 5. Graphics/Images - Each game piece and the game board is its own image.
# Optional features:
# 1. Restart from Game over - The players will have the option to restart the game after the game because
# it will return to the start screen.
# 2. Sprite Animation - All characters come from a sprite sheet.
# 3. Timer - like in real chess each player will have a timer.
# 5. Two Players simultaneously - Two players are taking their turn making their move.

import pygame
import gamebox

camera = gamebox.Camera(400, 600)  # The camera window is 400 x 600 as specified in the instructions.
black_rook1_x = 25
black_rook1_y = 25
black_knight_x = 75
black_knight_y = 25
black_bishop_x = 125
black_bishop_y = 25
black_queen_x = 175
black_queen_y = 25
black_king_x = 225
black_king_y = 25
black_bishop2_x = 275
black_bishop2_y = 25
black_knight2_x = 325
black_knight2_y = 25
black_rook2_x = 375
black_rook2_y = 25
black_pawn1_x = 25
black_pawn1_y = 75
black_pawn2_x = 75
black_pawn2_y = 75
black_pawn3_x = 125
black_pawn3_y = 75
black_pawn4_x = 175
black_pawn4_y = 75
black_pawn5_x = 225
black_pawn5_y = 75
black_pawn6_x = 275
black_pawn6_y = 75
black_pawn7_x = 325
black_pawn7_y = 75
black_pawn8_x = 375
black_pawn8_y = 75
white_rook1_x = 25
white_rook1_y = 375
white_knight_x = 75
white_knight_y = 375
white_bishop_x = 125
white_bishop_y = 375
white_queen_x = 175
white_queen_y = 375
white_king_x = 225
white_king_y = 375
white_bishop2_x = 275
white_bishop2_y = 375
white_knight2_x = 325
white_knight2_y = 375
white_rook2_x = 375
white_rook2_y = 375
white_pawn1_x = 25
white_pawn1_y = 325
white_pawn2_x = 75
white_pawn2_y = 325
white_pawn3_x = 125
white_pawn3_y = 325
white_pawn4_x = 175
white_pawn4_y = 325
white_pawn5_x = 225
white_pawn5_y = 325
white_pawn6_x = 275
white_pawn6_y = 325
white_pawn7_x = 325
white_pawn7_y = 325
white_pawn8_x = 375
white_pawn8_y = 325

# Creates the pieces and their starting points. This is the inclusion of graphics and sprite sheet.
chess_board = gamebox.from_image(200, 200, "chess_board.png")  # chess_board.png
# http://vladsukhoy.com/Teaching/2020_Spring_575/HW2/hw2.html
confetti = gamebox.from_image(200, 190, "confetti.png")  # confetti.png
# https://pngimg.com/uploads/confetti/confetti_PNG87007.png
black_rook1 = gamebox.from_image(black_rook1_x, black_rook1_y, "black_rook.png")  # black_rook.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_rdt45.svg
black_knight1 = gamebox.from_image(black_knight_x, black_knight_y, "black_knight.png")  # black_knight.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_ndt45.svg
black_bishop1 = gamebox.from_image(black_bishop_x, black_bishop_y, "black_bishop.png")  # black_bishop.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_bdt45.svg
black_queen = gamebox.from_image(black_queen_x, black_queen_y, "black_queen.png")  # black_queen.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_qdt45.svg
black_king = gamebox.from_image(black_king_x, black_king_y, "black_king.png")  # black_king.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_kdt45.svg
black_bishop2 = gamebox.from_image(black_bishop2_x, black_bishop2_y, "black_bishop.png")  # black_bishop.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_bdt45.svg
black_knight2 = gamebox.from_image(black_knight2_x, black_knight2_y, "black_knight.png")  # black_knight.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_ndt45.svg
black_rook2 = gamebox.from_image(black_rook2_x, black_rook2_y, "black_rook.png")  # black_rook.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_rdt45.svg

black_pawn1 = gamebox.from_image(black_pawn1_x, black_pawn1_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg
black_pawn2 = gamebox.from_image(black_pawn2_x, black_pawn2_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg
black_pawn3 = gamebox.from_image(black_pawn3_x, black_pawn3_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg
black_pawn4 = gamebox.from_image(black_pawn4_x, black_pawn4_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg
black_pawn5 = gamebox.from_image(black_pawn5_x, black_pawn5_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg
black_pawn6 = gamebox.from_image(black_pawn6_x, black_pawn6_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg
black_pawn7 = gamebox.from_image(black_pawn7_x, black_pawn7_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg
black_pawn8 = gamebox.from_image(black_pawn8_x, black_pawn8_y, "black_pawn.png")  # black_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_pdt45.svg

white_rook1 = gamebox.from_image(white_rook1_x, white_rook1_y, "white_rook.png")  # white_rook.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_rlt45.svg
white_knight1 = gamebox.from_image(white_knight_x, white_knight_y, "white_knight.png")  # white_knight.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_nlt45.svg
white_bishop1 = gamebox.from_image(white_bishop_x, white_bishop_y, "white_bishop.png")  # white_bishop.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_blt45.svg
white_king = gamebox.from_image(white_king_x, white_king_y, "white_king.png")  # white_king.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_klt45.svg
white_queen = gamebox.from_image(white_queen_x, white_queen_y, "white_queen.png")  # white_queen.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_qlt45.svg
white_bishop2 = gamebox.from_image(white_bishop2_x, white_bishop2_y, "white_bishop.png")  # white_bishop.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_blt45.svg
white_knight2 = gamebox.from_image(white_knight2_x, white_knight2_y, "white_knight.png")  # white_knight.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_nlt45.svg
white_rook2 = gamebox.from_image(white_rook2_x, white_rook2_y, "white_rook.png")  # white_rook.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_rlt45.svg

white_pawn1 = gamebox.from_image(white_pawn1_x, white_pawn1_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
white_pawn2 = gamebox.from_image(white_pawn2_x, white_pawn2_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
white_pawn3 = gamebox.from_image(white_pawn3_x, white_pawn3_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
white_pawn4 = gamebox.from_image(white_pawn4_x, white_pawn4_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
white_pawn5 = gamebox.from_image(white_pawn5_x, white_pawn5_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
white_pawn6 = gamebox.from_image(white_pawn6_x, white_pawn6_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
white_pawn7 = gamebox.from_image(white_pawn7_x, white_pawn7_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
white_pawn8 = gamebox.from_image(white_pawn8_x, white_pawn8_y, "white_pawn.png")  # white_pawn.png
# https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces#/media/File:Chess_plt45.svg
blue_dot = gamebox.from_image(-100, -100, "blue_dot.png")  # blue_dot.png
#  https://www.piskelapp.com/p/create/sprite
green_dot = gamebox.from_image(-100, -100, "green_dot.png")  # green_dot.png
#  https://www.piskelapp.com/p/create/sprite
moving_piece_1 = object()
moving_piece_2 = object()
pieces = [
    black_rook1, black_knight1, black_bishop1, black_queen, black_king, black_bishop2, black_knight2, black_rook2,
    black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8,
    white_rook1, white_knight1, white_bishop1, white_king, white_queen, white_bishop2, white_knight2, white_rook2,
    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7, white_pawn8,
]
start_game = False
white_turn = False
black_turn = False
white_timer = 600
black_timer = 600
white_wins = False
black_wins = False
ending = False
first_click = True


def restart():
    """
    This function restarts the game by resetting all global variables to their original values.
    :return: There is no return from this function.
    """
    global start_game, white_turn, black_turn, white_timer, black_timer, ending, black_rook1_x, black_rook1_y, \
        black_knight_x, black_knight_y, black_bishop_x, black_bishop_y, black_queen_x, black_queen_y, black_king_x, \
        black_king_y, black_bishop2_x, black_bishop2_y, black_knight2_x, black_knight2_y, black_rook2_x, \
        black_rook2_y, black_pawn1_x, black_pawn1_y, black_pawn2_x, black_pawn2_y, black_pawn3_x, \
        black_pawn3_y, black_pawn4_x, black_pawn4_y, black_pawn5_x, black_pawn5_y, black_pawn6_x, black_pawn6_y, \
        black_pawn7_x, black_pawn7_y, black_pawn8_x, black_pawn8_y, white_rook1_x, white_rook1_y, white_knight_x, \
        white_knight_y, white_bishop_x, white_bishop_y, white_queen_x, \
        white_queen_y, white_king_x, white_king_y, white_bishop2_x, white_bishop2_y, white_knight2_x, white_knight2_y, \
        white_rook2_x, white_rook2_y, white_pawn1_x, white_pawn1_y, white_pawn2_x, white_pawn2_y, white_pawn3_x, \
        white_pawn3_y, white_pawn4_x, white_pawn4_y, white_pawn5_x, white_pawn5_y, white_pawn6_x, white_pawn6_y, \
        white_pawn7_x, white_pawn7_y, white_pawn8_x, white_pawn8_y, blue_dot, \
        green_dot, first_click, moving_piece_1, moving_piece_2
    black_rook1.x = 25
    black_rook1.y = 25
    black_knight1.x = 75
    black_knight1.y = 25
    black_bishop1.x = 125
    black_bishop1.y = 25
    black_queen.x = 175
    black_queen.y = 25
    black_king.x = 225
    black_king.y = 25
    black_bishop2.x = 275
    black_bishop2.y = 25
    black_knight2.x = 325
    black_knight2.y = 25
    black_rook2.x = 375
    black_rook2.y = 25
    black_pawn1.x = 25
    black_pawn1.y = 75
    black_pawn2.x = 75
    black_pawn2.y = 75
    black_pawn3.x = 125
    black_pawn3.y = 75
    black_pawn4.x = 175
    black_pawn4.y = 75
    black_pawn5.x = 225
    black_pawn5.y = 75
    black_pawn6.x = 275
    black_pawn6.y = 75
    black_pawn7.x = 325
    black_pawn7.y = 75
    black_pawn8.x = 375
    black_pawn8.y = 75
    white_rook1.x = 25
    white_rook1.y = 375
    white_knight1.x = 75
    white_knight1.y = 375
    white_bishop1.x = 125
    white_bishop1.y = 375
    white_queen.x = 175
    white_queen.y = 375
    white_king.x = 225
    white_king.y = 375
    white_bishop2.x = 275
    white_bishop2.y = 375
    white_knight2.x = 325
    white_knight2.y = 375
    white_rook2.x = 375
    white_rook2.y = 375
    white_pawn1.x = 25
    white_pawn1.y = 325
    white_pawn2.x = 75
    white_pawn2.y = 325
    white_pawn3.x = 125
    white_pawn3.y = 325
    white_pawn4.x = 175
    white_pawn4.y = 325
    white_pawn5.x = 225
    white_pawn5.y = 325
    white_pawn6.x = 275
    white_pawn6.y = 325
    white_pawn7.x = 325
    white_pawn7.y = 325
    white_pawn8.x = 375
    white_pawn8.y = 325

    blue_dot = gamebox.from_image(-100, -100, "blue_dot.png")
    green_dot = gamebox.from_image(-100, -100, "green_dot.png")
    moving_piece_1 = object()
    moving_piece_2 = object()
    start_game = False
    white_turn = False
    black_turn = False
    white_timer = 600
    black_timer = 600
    ending = False
    first_click = True


def tick(keys):
    """
    This function contains the logic for the game that is checked 6 times per second.
    :param keys: This function takes in the activation of the B, W, K, R, mouse keys.
    :return: There is no return for this function.
    """

    camera.display()
    global start_game, white_turn, black_turn, white_timer, black_timer, ending, black_rook1_x, black_rook1_y, \
        black_knight_x, black_knight_y, black_bishop_x, black_bishop_y, black_queen_x, black_queen_y, black_king_x, \
        black_king_y, black_bishop2_x, black_bishop2_y, black_knight2_x, black_knight2_y, black_rook2_x, \
        black_rook2_y, black_pawn1_x, black_pawn1_y, black_pawn2_x, black_pawn2_y, black_pawn3_x, \
        black_pawn3_y, black_pawn4_x, black_pawn4_y, black_pawn5_x, black_pawn5_y, black_pawn6_x, black_pawn6_y, \
        black_pawn7_x, black_pawn7_y, black_pawn8_x, black_pawn8_y, white_rook1_x, white_rook1_y, white_knight_x, \
        white_knight_y, white_bishop_x, white_bishop_y, white_queen_x, \
        white_queen_y, white_king_x, white_king_y, white_bishop2_x, white_bishop2_y, white_knight2_x, white_knight2_y, \
        white_rook2_x, white_rook2_y, white_pawn1_x, white_pawn1_y, white_pawn2_x, white_pawn2_y, white_pawn3_x, \
        white_pawn3_y, white_pawn4_x, white_pawn4_y, white_pawn5_x, white_pawn5_y, white_pawn6_x, white_pawn6_y, \
        white_pawn7_x, white_pawn7_y, white_pawn8_x, white_pawn8_y, white_wins, black_wins, confetti, blue_dot, \
        green_dot, first_click, moving_piece_1, moving_piece_2
    # This is the start screen which displays the programmer's names, ID's, and the instructions for the game.
    camera.clear("white")
    camera.draw("Chess", 30, "black", 200, 100)
    camera.draw("Grant Sweeney - gcx8yv", 30, "purple", 200, 130)
    camera.draw("Robert Stambaugh - mjk3rn", 30, "purple", 200, 160)
    camera.draw("This is a two player chess game. Each player must know the rules of chess.", 15, "purple", 200, 200)
    camera.draw("This includes knowing how pieces move, and when the king is in check.", 15, "purple", 200, 220)
    camera.draw("Prior to starting the first player must press either B or W.", 15, "purple", 200, 240)
    camera.draw("This determines which pieces each player is in control of.", 15, "purple", 200, 260)
    camera.draw("After a player has gone, be sure to press either the B or W key.", 15, "purple", 200, 280)
    camera.draw("Ensure that this has been done as it changes the timer that is counting down.", 15, "purple", 200, 300)
    camera.draw("The game will end if a king dies or if one players timer hits zero.", 15, "purple", 200, 320)
    camera.draw("When playing, be sure that the mouse is on a piece when clicked.", 15, "purple", 200, 340)
    camera.draw("Also be sure to click quickly and a pawn can not change is identity.", 15, "purple", 200, 360)
    camera.draw("Watch the control console, you can only move a piece after the \"FIRST CLICK\"", 15, "purple", 200,
                380)
    camera.draw("If you see \"SECOND CLICK\" before you have clicked twice, try again carefully", 15, "purple", 200,
                400)
    camera.draw("Most importantly have fun!", 15, "purple", 200, 420)

    if not start_game:
        camera.draw("Press Space to Start", 40, "purple", 200, 450)
        if pygame.K_SPACE in keys:
            start_game = True

    if start_game:
        camera.clear("white")
        camera.draw(chess_board)
        for piece in pieces:
            camera.draw(piece)
        camera.draw("White Timer: " + str(white_timer), 25, "black", 80, 420)
        camera.draw("Black Timer: " + str(black_timer), 25, "black", 315, 420)

        if pygame.K_w in keys:  # Two players (white and black) Both the players are able to compete against each other
            # and interact with each other's pieces. This is also additional user input as they can
            # decide which timer to start.
            white_turn = True
            black_turn = False
        if pygame.K_b in keys:
            white_turn = False  # Two players (white and black)
            black_turn = True

        if pygame.K_k in keys:  # this is a kill code, it will end the game immediately resulting in a white win
            black_king_y = 550
            camera.clear("white")
            camera.draw(chess_board)
        if int(white_timer) == 0 or white_king.y > 400:  # Game over, if either of the kings is
            # moved into the captured piece area or either of the timers are 0 the game ends.
            start_game = False
            ending = True  # Game over parameter, the game will end if the timer for either player reaches 0.
            black_wins = True
            white_wins = False
            moving_piece_1 = object()
            moving_piece_2 = object()
        if int(black_timer) == 0 or black_king.y > 400:
            start_game = False
            ending = True  # Game over parameter, the game will end if the timer for either player reaches 0.
            black_wins = False
            white_wins = True
            moving_piece_1 = object()
            moving_piece_2 = object()
        if white_turn:
            camera.clear("white")
            camera.draw(chess_board)
            for piece in pieces:
                camera.draw(piece)
            white_timer -= 0.13333  # The timer counts down the total time a player has within the match.
            # It is set for 10 minutes per player.
            camera.draw("White Timer: " + str(int(white_timer)), 25, "black", 80, 420)
            camera.draw("Black Timer: " + str(int(black_timer)), 25, "black", 315, 420)
            if pygame.K_k in keys:
                black_king_y = 550
                camera.clear("white")
                camera.draw(chess_board)
                for piece in pieces:
                    camera.draw(piece)
            # User input
            if camera.mouseclick:
                if first_click:
                    print("FIRST CLICK (WHITE)")
                    blue_dot.center = camera.mouse
                    camera.draw(blue_dot)
                    for piece_1 in pieces:
                        if blue_dot.touches(piece_1):
                            if piece_1 in pieces:
                                moving_piece_1 = piece_1
                    first_click = False
                else:
                    print("SECOND CLICK (WHITE)")
                    green_dot.center = camera.mouse
                    camera.draw(green_dot)
                    if moving_piece_1 != object():
                        if moving_piece_1 in pieces:
                            moving_piece_1.center = camera.mouse
                    for piece_2 in pieces:
                        if moving_piece_1 != object():
                            if moving_piece_1.touches(piece_2):
                                if not (piece_2.x == moving_piece_1.x and piece_2.y == moving_piece_1.y):
                                    moving_piece_2 = piece_2
                                    moving_piece_2.y = 500

                    moving_piece_1 = object()
                    moving_piece_2 = object()
                    first_click = True
        if black_turn:
            camera.clear("white")
            camera.draw(chess_board)
            for piece in pieces:
                camera.draw(piece)
            black_timer -= .13333  # The timer counts down the total time a player has within the match.
            # It is set for 10 minutes per player.
            camera.draw("White Timer: " + str(int(white_timer)), 25, "black", 80, 420)
            camera.draw("Black Timer: " + str(int(black_timer)), 25, "black", 315, 420)
            if pygame.K_k in keys:
                black_king_y = 550
            if camera.mouseclick:  # User input, the user is able to click where they want their pieces to move.
                if first_click:
                    print("FIRST CLICK (BLACK)")
                    blue_dot.center = camera.mouse
                    camera.draw(blue_dot)
                    for piece_1 in pieces:
                        if blue_dot.touches(piece_1):
                            if piece_1 in pieces:
                                moving_piece_1 = piece_1
                    first_click = False
                else:
                    print("SECOND CLICK (BLACK)")
                    green_dot.center = camera.mouse
                    camera.draw(green_dot)
                    if moving_piece_1 != object():
                        moving_piece_1.center = camera.mouse
                    for piece_2 in pieces:
                        if moving_piece_1 != object():
                            if moving_piece_1.touches(piece_2):
                                if not (piece_2.x == moving_piece_1.x and piece_2.y == moving_piece_1.y):
                                    moving_piece_2 = piece_2
                                    moving_piece_2.y = 500
                    moving_piece_1 = object()
                    moving_piece_2 = object()
                    first_click = True

    if ending:
        camera.clear("white")
        camera.draw(confetti)
        camera.draw("White Timer: " + str(int(white_timer)), 25, "black", 80, 550)
        camera.draw("Black Timer: " + str(int(black_timer)), 25, "black", 315, 550)
        camera.draw("Game Over", 30, "black", 200, 200)
        camera.draw("Press r to ", 30, "black", 200, 250)
        camera.draw("restart the game", 30, "black", 200, 300)
        if white_wins:
            camera.draw("White Wins!", 60, "black", 200, 450)
        else:
            camera.draw("Black Wins!", 60, "black", 200, 450)
        if pygame.K_r in keys:
            restart()  # The game will restart if the player presses "r". All the pieces will return to
            # their original positions.


gamebox.timer_loop(6, tick)
