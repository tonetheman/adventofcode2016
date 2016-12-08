
namespace Puzzle8 {

	export class Screen {
		scr : number[] =[];
		rows : number;
		cols : number;
		constructor(rows:number, cols:number) {
			this.rows = rows;
			this.cols = cols;
			for(let i=0;i<(this.rows*this.cols);i++) {
				this.scr[i] = 0;
			}
		}
		get(row:number,col:number) : number {
			let idx : number = row*this.cols + col;
			return this.scr[idx];
		}
		set(row:number,col:number,val:number) {
			let idx : number = row*this.cols + col;
			let old_val = this.scr[idx];
			this.scr[idx] = val;
			return old_val;
		}
		rect(a:number, b:number) {
			// turn on rect at top corner a wide, b tall
			for(let i=0;i<b;i++) {
				for(let j=0;j<a;j++) {
					this.set(j,i,1);
				}
			}

		}
		repr() :string {
			let ts : string = "";
			for(let i=0;i<this.cols;i++) {
				for(let j=0;j<this.rows;j++) {
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
s.rect(6,2);
console.log(s.repr());
