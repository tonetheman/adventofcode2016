var Puzzle8;
(function (Puzzle8) {
    var Screen = (function () {
        function Screen(rows, cols) {
            this.scr = [];
            this.rows = rows;
            this.cols = cols;
            for (var i = 0; i < (this.rows * this.cols); i++) {
                this.scr[i] = 0;
            }
        }
        Screen.prototype.get = function (row, col) {
            var idx = row * this.cols + col;
            return this.scr[idx];
        };
        Screen.prototype.set = function (row, col, val) {
            var idx = row * this.cols + col;
            var old_val = this.scr[idx];
            this.scr[idx] = val;
            return old_val;
        };
        Screen.prototype.rect = function (a, b) {
            // turn on rect at top corner a wide, b tall
            for (var i = 0; i < b; i++) {
                for (var j = 0; j < a; j++) {
                    this.set(j, i, 1);
                }
            }
        };
        Screen.prototype.rotate_col = function (x, b) {
            // rotate the column x, by the number b
        };
        Screen.prototype.repr = function () {
            var ts = "";
            for (var i = 0; i < this.cols; i++) {
                for (var j = 0; j < this.rows; j++) {
                    ts = ts + this.get(j, i) + " ";
                }
                ts = ts + "\n";
            }
            return ts;
        };
        return Screen;
    }());
    Puzzle8.Screen = Screen;
})(Puzzle8 || (Puzzle8 = {}));
var s = new Puzzle8.Screen(7, 3);
console.log(s.repr());
s.rect(6, 2);
console.log(s.repr());
