
namespace Puzzle8 {

	export class Screen {
		scr : number[] =[];
		width : number;
		height : number;
		constructor(w:number, h:number) {
			this.width = w;
			this.height = h;
			for(let i=0;i<(this.width*this.height);i++) {
				this.scr[i] = 0;
			}
		}
		get(row:number,col:number) : number {
			let idx : number = row*this.width + col;
			return this.scr[idx];
		}
		rect(w:number, h:number) {

		}
		repr() :string {
			let ts : string = "";
			for(let i=0;i<this.width;i++) {
				for(let j=0;j<this.height;j++) {
					ts = ts + this.get(j,i) + " ";
				}
				ts = ts + "\n";
			}
			return ts;
		}
	}

}

let s = new Puzzle8.Screen(7,3);
console.log(s.repr());
