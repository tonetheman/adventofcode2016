var Puzzle8;
(function (Puzzle8) {
    var Screen = (function () {
        function Screen(w, h) {
            this.scr = [];
            this.width = w;
            this.height = h;
            for (var i = 0; i < (this.width * this.height); i++) {
                this.scr[i] = 0;
            }
        }
        Screen.prototype.get = function (row, col) {
            var idx = row * this.width + col;
            return this.scr[idx];
        };
        Screen.prototype.rect = function (w, h) {
        };
        Screen.prototype.repr = function () {
            var ts = "";
            for (var i = 0; i < this.width; i++) {
                for (var j = 0; j < this.height; j++) {
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
