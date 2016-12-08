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
        Screen.prototype.rect = function (w, h) {
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
