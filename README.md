# HeatDecipation
A python script to simulate heat decipation on a system.

This version simulates heat transfer between two bodies each of 16 unit cells (atoms).

## Results
| Total Phonons | Most Probable Combination(MPC) | MPC probability | Least Probable Combination(LPC) | LPC probability |
|---|---|---|---|---|
|2|(1, 1)|51.61290322580645|(0, 2)|48.38709677419355|
|3|(1, 2)|77.41935483870968|(0, 3)|22.58064516129032|
|4|(1, 3)|49.83314794215795|(0, 4)|10.122358175750835|
|5|(2, 3)|66.74082313681868|(0, 5)|4.338153503893214|
|6|(2, 4)|48.2017055988135|(0, 6)|1.7673958719564948|
|7|(3, 4)|60.56111729081696|(0, 7)|0.6797676430601903|
|8|(3, 5)|46.510938079347426|(0, 8)|0.2447163515016685|
|9|(4, 5)|56.685205784204676|(0, 9)|0.08157211716722285|
|10|(4, 6)|45.1838596830617|(0, 10)|0.024826296529154777|
|11|(5, 6)|54.22063161967403|(0, 11)|0.006770808144314939|
|12|(5, 7)|44.261740097693085|(0, 12)|0.0016120971772178427|

Here a weird thing happens, the probabilty of equal spread of phonons between two matrices is almost never the highest probable event.
Instead, the a slight unequal one has the most probability.