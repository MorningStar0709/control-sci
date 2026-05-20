import os
import sys

if any(arg in {"-h", "--help"} for arg in sys.argv[1:]):
    print(
        "Validate the 14 Track1 cited chunk evidence files under corpus/chunks/.\n"
        "Usage: python scripts/validate_t1_chunks.py\n"
        "Note: public release packages may rely on docs/submissions/data_trace_bundle/ "
        "instead of the full raw corpus tree."
    )
    raise SystemExit(0)
refs = [
    '2201.05599_Smart_Magnetic_Microrobots_Learn_to_Swim_with_Deep_Reinforce_chunk_047',
    '2204.07041_Distributed_Optimal_Control_with_Recovered_Robustness_for_Un_chunk_010',
    '2307.08762_Geometric_Extended_State_Observer_on_SE3_with_Fast_Finite_Ti_chunk_051',
    '2204.07041_Distributed_Optimal_Control_with_Recovered_Robustness_for_Un_chunk_023',
    '智能控制_chunk_307',
    '2201.02997_Performance_Analysis_of_Event_Triggered_Consensus_Control_fo_chunk_010',
    '自动控制原理_胡寿松_chunk_368',
    'Computer_Controlled_Systems_Astrom_chunk_447',
    'Ogata_Modern_Control_5th_chunk_332',
    'Belanger_Control_Engineering_chunk_375',
    'Dynamic_Systems_Modeling_Simulation_Control_chunk_292',
    '2505.13475_Causality_for_Cyber_Physical_Systems_chunk_065',
    '控制理论导论_郭雷_chunk_179',
    '2511.02717_An_unscented_Kalman_filter_method_for_real_time_input_parame_chunk_023',
]
found = 0
for r in refs:
    for split in ['train','eval']:
        fp = os.path.join('corpus','chunks',split,f'{r}.md')
        if os.path.exists(fp):
            found += 1
            break
print(f'Found {found}/{len(refs)} chunk evidence files')
