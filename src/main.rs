#![allow(dead_code)]
use colourado::{ColorPalette, PaletteType};
use num::complex::Complex;
pub mod fractals;
pub mod utils;
use crate::fractals::MandelbrotSet;
use crate::utils::convert_color;

const WIDTH: i16 = 1024;
const HEIGHT: i16 = 1024;
const SCALE: f32 = 0.075;

fn main() {
    let set = MandelbrotSet {
        max_iter: 5,
        escape_radius: 2,
    };
    let mut imgbuf: image::RgbImage = image::ImageBuffer::new(WIDTH as u32, HEIGHT as u32);
    let palette = ColorPalette::new(510, PaletteType::Dark, false);

    for (x, y, pixel) in imgbuf.enumerate_pixels_mut() {
        let c: Complex<f64> = Complex::new(SCALE as f64, 0_f64)
            * Complex::new(
                (x as i16 - WIDTH / 2) as f64,
                (HEIGHT / 2 - y as i16) as f64,
            );
        let instab = 1_f64 - set.stability(c, true, true);
        let r = convert_color(palette.colors[instab as usize].red);
        let g = convert_color(palette.colors[instab as usize].green);
        let b = convert_color(palette.colors[instab as usize].blue);

        *pixel = image::Rgb([r, g, b]);
        // print!("R {r}, G {g}, B {b}");
    }

    match imgbuf.save("output.png") {
        Err(e) => eprintln!("Error writing file: {}", e),
        Ok(()) => println!("Done."),
    };
}
