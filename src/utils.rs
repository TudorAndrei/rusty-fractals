pub fn convert_color(color: f32) -> u8 {
    // return color as u8 * 255;
    let new_color: f32 = if color == 1.0 { 255.0 } else { color * 256.0 };
    new_color.floor() as u8
}

pub fn min<T: PartialOrd>(a: T, b: T) -> T {
    if a < b {
        a
    } else {
        b
    }
}

pub fn max<T: PartialOrd>(a: T, b: T) -> T {
    if a > b {
        a
    } else {
        b
    }
}
