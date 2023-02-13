import my_chess as mc
import chess_constants as cc
import history_heuristic as hh
import my_relation as mr
import sqlite3

class my_game:
    def __init__(self):
        self.board = mc.chess_board()
        self.max_depth = cc.max_depth
        self.history_table = hh.history_table()
        self.best_move = mc.step()
        self.cnt = 0

    def alpha_beta(self, depth, alpha, beta, allowNull = True ):  # alpha-beta cắt tỉa，alpha min，beta max
        who = (self.max_depth - depth) % 2  # current player
        checkMate = False
        if self.is_game_over(who):  # if game over stop search
            return cc.min_val
        move_list, capture_list = self.board.generate_move(who,checkMate)  # list các nước đi
            
        # history_table 
        for i in range(len(move_list)):
            move_list[i].score = self.history_table.get_history_score(who, move_list[i])
        move_list.sort(key=lambda x: x.score, reverse=True) # move_ordering
        if depth == 0:  # stop search 
            if len(capture_list) == 0: 
                return self.evaluate(who)
            else: return self.quiescence_search(alpha, beta, who)
        
        if checkMate == False and allowNull == True and depth>3:
            # print ("***********************")
            who = (who+1)%2
            allowNull = False
            eval = - self.alpha_beta(3, alpha, beta, allowNull )
            who = (who+1)%2
            if(eval >= beta):
                print ("***********************")
                return eval; # Cutoff
        
        best_step = move_list[0]
        score_list = []
        for step in move_list:
            temp = self.move_to(step)
            score = -self.alpha_beta(depth - 1, -beta, -alpha ,True)
            score_list.append(score)
            self.undo_move(step, temp)
            if score > alpha:
                alpha = score
                if depth == self.max_depth:
                    self.best_move = step
                best_step = step
            if alpha >= beta:
                best_step = step
                break
        
        if best_step.from_x != -1:
            self.history_table.add_history_score(who, best_step, depth)
        if best_step.from_x == -1:
            self.best_move = best_step
        return alpha
    
    def evaluate(self, who):  
        self.cnt += 1
        relation_list = self.init_relation_list()
        base_val = [0, 0]
        pos_val = [0, 0]
        mobile_val = [0, 0]
        relation_val = [0, 0]
        for x in range(9):
            for y in range(10):
                now_chess = self.board.board[x][y]
                type = now_chess.chess_type
                if type == 0:
                    continue
                now = now_chess.belong
                pos = x * 9 + y
                temp_move_list,capture_list = self.board.get_chess_move(x, y, now, True, False)
                
                base_val[now] += cc.base_val[type]
                
                if now == 0:  
                    pos_val[now] += cc.pos_val[type][pos]
                else:
                    pos_val[now] += cc.pos_val[type][89 - pos]
                
                for item in temp_move_list:
                    
                    temp_chess = self.board.board[item.to_x][item.to_y]  
                    if temp_chess.belong != now:  
                        if temp_chess.chess_type == cc.vua:  
                            if temp_chess.belong != who:
                                return cc.max_val
        my_max_val = base_val[0] + pos_val[0] 
        my_min_val = base_val[1] + pos_val[1] 
        if who == 0:
            return my_max_val - my_min_val
        else:
            return my_min_val - my_max_val
                    
    def quiescence_search(self, alpha, beta, who):
        stand_pat = self.evaluate(who)
        if stand_pat >= beta:
            return beta
        if alpha < stand_pat:
            alpha = stand_pat
        move_list, capture_list = self.board.generate_move((who+1),checkMate=False)
        for step in capture_list:
            temp = self.move_to(step)
            score = -self.quiescence_search(-beta, -alpha, who)
            self.undo_move(step, temp)
            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
        return alpha            


    def init_relation_list(self):
        res_list = []
        for i in range(10):
            res_list.append([])
            for j in range(10):
                res_list[i].append(mr.relation())
        return res_list

    def init_lib(self):
        conn = sqlite3.connect("./init_lib/chess.db")
        cursor = conn.cursor()
        # sql = """select name from sqlite_master where type='table' order by name"""
        sql = "select * from chess"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        print(type(result))
        conn.close()

    def is_game_over(self, who):  
        for i in range(9):
            for j in range(10):
                if self.board.board[i][j].chess_type == cc.vua:
                    if self.board.board[i][j].belong == who:
                        return False
        return True

    def move_to(self, step, flag = False):  
        belong = self.board.board[step.to_x][step.to_y].belong
        chess_type = self.board.board[step.to_x][step.to_y].chess_type
        temp = mc.chess(belong, chess_type)
        # if flag:
        #     self.board.print_board()
        #     print(self.board.board[step.to_x][step.to_y].chess_type)
        self.board.board[step.to_x][step.to_y].chess_type = self.board.board[step.from_x][step.from_y].chess_type
        # if flag:
        #     print(self.board.board[step.from_x][step.from_y].chess_type)
        #     print(self.board.board[step.to_x][step.to_y].chess_type)
        #     print(step.to_x, step.to_y)
        self.board.board[step.to_x][step.to_y].belong = self.board.board[step.from_x][step.from_y].belong
        self.board.board[step.from_x][step.from_y].chess_type = cc.kong
        self.board.board[step.from_x][step.from_y].belong = -1
        return temp

    def undo_move(self, step, chess):  
        self.board.board[step.from_x][step.from_y].belong = self.board.board[step.to_x][step.to_y].belong
        self.board.board[step.from_x][step.from_y].chess_type = self.board.board[step.to_x][step.to_y].chess_type
        self.board.board[step.to_x][step.to_y].belong = chess.belong
        self.board.board[step.to_x][step.to_y].chess_type = chess.chess_type
if __name__ == "__main__":
    game = my_game()
    # game.board.print_board()
    while(True):
        from_x = int(input())
        from_y = int(input())
        to_x = int(input())
        to_y = int(input())
        s = mc.step(from_x, from_y, to_x, to_y)
        # game.board.print_board()

        game.alpha_beta(game.max_depth, cc.min_val, cc.max_val, True)
        print(game.best_move)
        game.move_to(game.best_move)


    game.move_to(s)
    # game.board.print_board()
