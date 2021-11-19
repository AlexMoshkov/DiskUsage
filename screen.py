import curses
import curses.textpad


class Screen(object):
    UP = -1
    DOWN = 1

    def __init__(self, items):
        self.window = None

        self.width = 0
        self.height = 0

        self.init_curses()

        self.items = items

        self.max_lines = curses.LINES
        self.top = 0
        self.bottom = len(self.items)
        self.current = 0
        self.page = self.bottom // self.max_lines

    def init_curses(self):
        self.window = curses.initscr()
        self.window.keypad(True)

        curses.noecho()
        curses.cbreak()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

        self.current = curses.color_pair(2)

        self.height, self.width = self.window.getmaxyx()

    def run(self):
        try:
            self.input_stream()
        except KeyboardInterrupt:
            pass
        finally:
            curses.endwin()

    def input_stream(self):
        while True:
            self.display()

            ch = self.window.getch()
            if ch == curses.KEY_UP:
                self.scroll(self.UP)
            elif ch == curses.KEY_DOWN:
                self.scroll(self.DOWN)
            elif ch == curses.KEY_LEFT:
                self.paging(self.UP)
            elif ch == curses.KEY_RIGHT:
                self.paging(self.DOWN)
            elif ch == curses.ascii.ESC or ch == ord('q'):
                break

    def scroll(self, direction):
        next_line = self.current + direction

        if direction == self.UP:
            if self.top > 0 and self.current == 0:
                self.top += direction
            elif self.top > 0 or self.current > 0:
                self.current = next_line
        else:
            if next_line == self.max_lines and self.top + self.max_lines < self.bottom:
                self.top += direction
            elif next_line < self.max_lines and self.top + next_line < self.bottom:
                self.current = next_line

    def paging(self, direction):
        current_page = (self.top + self.current) // self.max_lines
        next_page = current_page + direction
        if next_page == self.page:
            self.current = min(self.current, self.bottom % self.max_lines - 1)
        if (direction == self.UP) and (current_page > 0):
            self.top = max(0, self.top - self.max_lines)
            return
        if (direction == self.DOWN) and (current_page < self.page):
            self.top += self.max_lines
            return

    def display(self):
        self.window.erase()
        for idx, item in enumerate(self.items[self.top:self.top + self.max_lines]):
            if idx == self.current:
                self.window.addstr(idx, 0, item, curses.color_pair(2))
            else:
                self.window.addstr(idx, 0, item, curses.color_pair(1))
        self.window.refresh()


if __name__ == '__main__':
    items = [f'{num + 1}. Item' for num in range(1000)]
    screen = Screen(items)
    screen.run()