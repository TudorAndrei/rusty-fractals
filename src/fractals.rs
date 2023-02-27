use crate::utils::{max, min};
use num::Complex;

pub struct MandelbrotSet {
    pub max_iter: i64,
    pub escape_radius: i64,
}

impl MandelbrotSet {
    fn escape_count(&self, candidate: Complex<f64>, smooth: bool) -> f64 {
        let mut z: Complex<f64> = Complex::new(0.0, 0.0);
        for iteration in 0..self.max_iter {
            z = z.powi(2) + candidate;
            if z.norm() > self.escape_radius as f64 {
                if smooth {
                    return (iteration as f64) + -(z.norm().ln() / 2_f64.ln()).ln();
                }
                return iteration as f64;
            }
        }
        self.max_iter as f64
    }
    pub fn stability(&self, candidate: Complex<f64>, smooth: bool, clamp: bool) -> f64 {
        let value = self.escape_count(candidate, smooth) / self.max_iter as f64;
        if clamp {
            return max(0.0_f64, min(value, 1.0_f64));
        }
        value as f64
    }
    pub fn check(&self, candidate: Complex<f64>) -> bool {
        self.stability(candidate, false, false) == 1.0
    }
}
