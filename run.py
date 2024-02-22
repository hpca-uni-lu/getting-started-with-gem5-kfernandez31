from components.boards            import HW0RISCVBoard
from components.processors        import HW0TimingSimpleCPU
from components.cache_hierarchies import HW0MESITwoLevelCache
from components.memories          import HW0DDR3_1600_8x8
from gem5.simulate.simulator      import Simulator

from workloads.hello_world_workload import HelloWorldWorkload

if __name__ == "__m5_main__":
        cpu   = HW0TimingSimpleCPU()
        cache = HW0MESITwoLevelCache()
        mem   = HW0DDR3_1600_8x8()
        board = HW0RISCVBoard(
            clk_freq="2GHz", processor=cpu, cache_hierarchy=cache, memory=mem
        )

        workload = HelloWorldWorkload()
        board.set_workload(workload)
        simulator = Simulator(board=board, full_system=False)
        simulator.run()
        
        print("Finished simulation.")

