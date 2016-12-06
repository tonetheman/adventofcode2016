
extern crate md5;

fn main() {
    println!("Hello, world!");

    let prefix = "reyedfim";

    for x in 0..1000000 {
      let s: String = format!("{}{}",prefix,x.to_string());
      let digest = md5::compute(s.as_bytes());

      if digest[0] == 0x00 && digest[1] == 0x00  &&
        (digest[2]>>4)==0x00 {
          println!("possible match {} {} {} {}",
          x, digest[0], digest[1], digest[2]);
          println!("{:X} {:X} {:X}", digest[0], digest[1], digest[2]);
      }
    }


}
