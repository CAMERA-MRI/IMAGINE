# ERNIE RF System: Low-Noise Amplifier (LNA)

## Overview

The ERNIE low-field MRI scanner uses a **Wenteq (ABL0050-00-4510)** broadband low-noise amplifier (LNA) in its RF receive chain. The LNA amplifies the weak MR signal received by the RF coil before the signal reaches the MRI receiver. Its high gain helps reduce the relative contribution of noise from subsequent receiver electronics.

## LNA Specifications

| Parameter | Specification |
|---|---|
| Manufacturer | Wenteq Microwave Corp. |
| Model / part number | **ABL0050-00-4510** |
| Amplifier type | Broadband low-noise amplifier |
| Operating frequency range | 10 kHz–500 MHz |
| Typical small-signal gain | 45 dB |
| Typical noise figure | 1.0 dB |
| Typical gain flatness | ±1.0 dB |
| Typical output 1-dB compression point | +16 dBm |
| DC supply voltage | +12 V |
| Typical DC supply current | 110 mA |
| RF input/output connectors | SMA female |

*These are manufacturer-listed nominal specifications, not measurements of the assembled ERNIE receiver.*

## Integration into the ERNIE RF Receive Chain

**RF coil → Transmit/receive (T/R) switch → Wenteq LNA → MRI receiver/digitizer**

The T/R switch routes the received MR signal to the LNA and must adequately isolate the LNA from high-power RF transmission. The amplified signal is then delivered to the MRI receiver for acquisition.

## Assembly and Operating Procedure

1. Mount the LNA securely in the RF receiver assembly.
2. Connect the **receive output of the T/R switch** to the LNA RF input using a suitable SMA coaxial cable.
3. Connect the LNA RF output to the MRI receiver/digitizer.
4. Confirm the DC connection polarity and supply requirements for the actual unit. Apply a regulated **+12 V DC** supply.
5. With RF transmission disabled, verify the receive path using a suitably low-level test signal and check for receiver saturation.
6. Before running an MRI sequence, verify that the T/R switch provides sufficient transmit-pulse isolation to protect the LNA.

## Important Notes

- The specified 10 kHz–500 MHz frequency range includes the approximately 2 MHz operating frequency of the ERNIE low-field scanner. Verify actual gain and noise performance at your scanner's operating frequency.
- **Do not connect the LNA directly to the RF power-amplifier transmit output.**
- Check the **maximum safe RF input power** and DC connection details in the part-specific documentation before operating the system; these limits are not confirmed by the summary specifications above.
- The listed gain and noise figure are typical manufacturer values and may differ under actual operating conditions.

## Manufacturer References

- [Wenteq (ABL0050-00-4510) — Product Page](https://store.wenteq.com/product/abl0050-00-4510/)
- [Wenteq Microwave — Amplifier Specifications](https://wenteq.com/services/)
