import pyNN.nest as sim
from pyNN.utility.plotting import Figure, Panel
sim.setup(timestep=0.1)

cell_type = sim.IF_curr_exp(v_rest=-65, v_thresh=-55, v_reset=-65, tau_refrac=1, tau_m=10, cm=1, i_offset=1.1)
population1 = sim.Population(100, cell_type, label="Population 1")

population1.record("v")
sim.run(100.0)

data_v = population1.get_data().segments[0].filter(name='v')[0]

n0_fig = Figure(
        Panel(
            data_v[:,0],
            xticks=True, xlabel="Time (ms)",
            yticks=True, ylabel="Membrane Pot(mV)"
            ),
        title="Response of neuron #0",
        annotations="NEST simulation"
    )
n0_fig.save('./neuron0_plot.png')
