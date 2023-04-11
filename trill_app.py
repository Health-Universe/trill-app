import streamlit as st
from pathlib import Path
import os
import tempfile

def run_trill_command(trill_args):
    trill_args_str = " ".join(trill_args)
    os.system(f"trill {trill_args_str}")

st.title("TRILL Protein Engineering")

operations = ["embed", "finetune", "generate", "fold", "visualize"]

tabs = dict(zip(operations, st.tabs(operations)))

name = st.text_input("Enter run name", value="example")
gpus = st.number_input("Enter number of GPUs", value=1, step=1)
nodes = st.number_input("Enter number of nodes", value=1, step=1)
logger_enabled = st.checkbox("Enable Tensorboard logger")
profiler_enabled = st.checkbox("Utilize PyTorchProfiler")
rng_seed = st.number_input("Enter RNG seed", value=123)

st.markdown("Upload input file:")
input_file = st.file_uploader("", type=["fasta", "pdb", "cif", "csv"])

args = ["--nodes", str(nodes)]

if logger_enabled:
    args.append("--logger")
if profiler_enabled:
    args.append("--profiler")
if rng_seed is not None:
    args.extend(["--RNG_seed", str(rng_seed)])

if input_file:
    with tempfile.NamedTemporaryFile(mode="wb", delete=False) as fp:
        fp.write(input_file.getvalue())
        input_path = Path(fp.name)
        args.extend(["--query", str(input_path)])


with tabs["generate"]:
    model = st.selectbox("Choose model", ("ESM-IF1", "ProtGPT2", "ProteinMPNN", "ESM2_Gibbs"), key="choose_model_generate")
    args.append(model)

for operation in ["embed", "finetune", "fold"]:
    with tabs[operation]:
        model = st.selectbox("Choose model", ("esm2_t12_35M_UR50D", "esm2_t30_150M_UR50D"), key=f"choose_model_{operation}")
        args.extend(["--model", model])

# Add more UI components for other named arguments
# ...

submit = st.button("Run")

if input_file and submit:
    trill_args = [name, str(gpus), operation, *args]
    run_trill_command(trill_args)
    st.success("TRILL operation completed.")
    if input_path.exists():
        input_path.unlink() 