
extern crate md5;

fn main() {
    println!("Hello, world!");

    let digest = md5::compute(b"reyedfim797564");
    println!(" got it {} {} {} {} {}",
    digest[0],digest[1],digest[2],digest[3],digest[4]);

    if digest[0] == 0 && digest[1] == 0 && digest[2] == 0
      && digest[3] == 0 && digest[4] == 0 {
      println!(" got it {} {} {} {} {}",
      digest[0],digest[1],digest[2],digest[3],digest[4]);
    }


    let digest2 = md5::compute(b"reyedfim938629");
    println!(" got it {} {} {} {} {}",
    digest2[0],digest2[1],digest2[2],digest2[3],digest2[4]);


}
