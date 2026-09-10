# Gradient Power Amplifier

The IMAGINE MRI scanner uses the open-source
[GPA-FHDO gradient power amplifier](https://github.com/menkueclab/GPA-FHDO)
to drive the X, Y, and Z gradient coils.

The GPA-FHDO is a four-channel gradient power amplifier designed for
low-field MRI applications. In the IMAGINE scanner, three channels are
used to drive the three gradient axes.

> **Note:** The GPA used in the IMAGINE scanner is based on the original
> GPA-FHDO design. Some components and implementation details were added
> or modified for our scanner configuration.

## Bill of Materials

The complete bill of materials (BOM) for the IMAGINE gradient power
amplifier is available here:

[Download the IMAGINE GPA BOM](./IMAGINE_GPA_BOM.xlsx)

The BOM includes the components used in our implementation, including
components that differ from or were added to the original GPA-FHDO design.

## Original GPA-FHDO Project

Original design and documentation:

https://github.com/menkueclab/GPA-FHDO
