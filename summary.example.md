%% DATAVIEW_PUBLISHER: start
#dataview-publisher
```dataviewjs
const date_start = dv.date("2025-03-01");
const date_end = dv.date("2025-12-31");

const config_tag = ""; // should be empty, or formatted as #bla
const task_status = "u";

const directory_mdfiles = "mdfiles/";
const task_status_map = {
    "u": "papers to filter",
    "r": "papers to read",
    "d": "papers to download",
    "D": "papers already downloaded",
    "-": "papers that are not relevant"
};

// Collect a complete list of papers meeting the specified conditions
let pages = dv.pages().filter(
    p => p.file.path.startsWith(directory_mdfiles)
).filter(
    p => (task_status && p.file.tasks.filter(t => t.status === task_status).length > 0) || (!task_status)
).filter(
    p => (config_tag && p?.config_tags?.contains(config_tag)) || (!config_tag)
).filter(
    p => p.date_updated && dv.date(p.date_updated) >= date_start && dv.date(p.date_updated) <= date_end // Date filtering
).sort(
    p => -p.ai_rating // Sort by AI rating in descending order
);

// Get the total number of articles
const totalArticles = pages.length;

// Summary Information
let summary = [
    `- **Date Range:** ${date_start.toISODate()} to ${date_end.toISODate()}`,
    `- **Status Filter:** list of ${task_status_map[task_status] || "all papers"}`,
    `- **Tag Filter:** ${config_tag || "None (All Tags)"}`,
    `- **Total Number of Papers:** **${totalArticles}**`,
    `\n---\n`
].join("\n");

// Format each article with index/total
let formattedPages = pages.map((p, index) => {
    const rating = typeof p.ai_rating === 'number' ? p.ai_rating : 0;
    const percentage = (rating / 10) * 100;

    return {
        content: [
            `# (${index + 1}/${totalArticles}) ${p.url_pdf}`,
            `\n`,
            `### Rating: ${rating}/10`,
            `\n`,
            `<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: ${percentage}%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>`,
            `\n`,
            `### ${p.title}`,
            `**${p.authors}**`,
            `\n`,
            p?.config_tags?.join(" ") || "",
            `### Abstract:\n${p.abstract}`,
            `\n`,
            p.file.link.toEmbed(),
            `### AI Justification:\n${p.ai_reason || "N/A"}`,
        ].join("\n"),
        rating: rating
    };
});

// Extract the formatted content
const output = [summary, ...formattedPages.map(p => p.content)].join("\n");
// const output = formattedPages.map(p => p.content).join("\n");

// Display content
output;
```
%%

- **Date Range:** 2025-03-01 to 2025-12-31
- **Status Filter:** list of papers to filter
- **Tag Filter:** None (All Tags)
- **Total Number of Papers:** **382**

---

# (1/382) http://arxiv.org/pdf/2504.07136v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The spectrum of magnetized turbulence in the interstellar medium
**James R. Beattie,Christoph Federrath,Ralf S. Klessen,Salvatore Cielo,Amitava Bhattacharjee**


#mhd
### Abstract:
The interstellar medium (ISM) of our Galaxy is magnetized, compressible and turbulent, influencing many key ISM properties, like star formation, cosmic ray transport, and metal and phase mixing. Yet, basic statistics describing compressible, magnetized turbulence remain uncertain. Utilizing grid resolutions up to $10,080^3$ cells, we simulate highly-compressible, magnetized ISM-style turbulence with a magnetic field maintained by a small-scale dynamo. We measure two coexisting kinetic energy cascades, $\mathcal{E}_{{\rm kin}}(k) \propto k^{-n}$ , in the turbulence, separating the plasma into scales that are non-locally interacting, supersonic and weakly magnetized $(n=2.01\pm 0.03\approx 2)$ and locally interacting, subsonic and highly magnetized $(n=1.465\pm 0.002\approx 3/2)$ , where $k$ is the wavenumber. We show that the $3/2$ spectrum can be explained with scale-dependent kinetic energy fluxes and velocity-magnetic field alignment. On the highly magnetized modes, the magnetic energy spectrum forms a local cascade $(n=1.798\pm 0.001\approx 9/5)$ , deviating from any known \textit{ab initio} theory. With a new generation of radio telescopes coming online, these results provide a means to directly test if the ISM in our Galaxy is maintained by the compressible turbulent motions from within it.


![[mdfiles/2504.07136.md|2504.07136]]
### AI Justification:
This paper is highly relevant to your research interests as it directly investigates the "spectrum of magnetized turbulence in the interstellar medium," which aligns with your focus on "magnetic dynamics of plasmas." The study's exploration of "compressible, magnetized turbulence" and its connection to scale-dependent magnetic structuring speaks to your interest in both magnetic field amplification through dynamical processes and the emergent behaviors of magnetic fields within turbulent plasma environments.
# (2/382) http://arxiv.org/pdf/2504.21082v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Kiloparsec-scale turbulence driven by reionization may grow intergalactic magnetic fields
**Christopher Cain,Matthew McQuinn,Evan Scannapieco,Anson D'Aloisio,Hy Trac**


#mhd
### Abstract:
The intergalactic medium (IGM) underwent intense heating that resulted in pressure disequilibrium in the wake of ionization fronts during cosmic reionization. The dynamical relaxation to restore pressure balance may have driven small-scale turbulence and, hence, the amplification of intergalactic magnetic fields. We investigate this possibility using a suite of $\approx 100$ pc resolution radiation-hydrodynamics simulations of IGM gas dynamics. We show that as the spatial resolution improves beyond that achieved with most prior studies, much of the IGM becomes turbulent unless it was pre-heated to $\gg 100~$ K before reionization. In our most turbulent simulations, we find that the gas energy spectrum follows the expected $k^{-5/3}$ Kolmogorov scaling to the simulations resolution, and the eddy turnover time of the turbulence is $< 1$ Gyr at $k \approx 1 ~$ kpc $^{-1}$ . Turbulence will grow magnetic fields, and we show that the fields grown by reionization-driven turbulence could explain lower limits on IGM B-field strengths from observations of TeV blazars.


![[mdfiles/2504.21082.md|2504.21082]]
### AI Justification:
This paper is highly relevant to your research interests as it examines "the amplification of intergalactic magnetic fields" driven by turbulence, which directly aligns with your focus on "how dynamos and other mechanisms drive the amplification and evolution of magnetic fields in astrophysical plasmas." Additionally, the use of "radiation-hydrodynamics simulations" provides theoretical insights into "scale-dependent magnetic structuring," aligning with your interest in multi-scale dynamics of magnetic fields in plasma environments.
# (3/382) http://arxiv.org/pdf/2504.10763v2


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Effective Field Theories in Magnetohydrodynamics
**Amir Jafari**


#mhd
### Abstract:
We briefly review the recent developments in magnetohydrodynamics, which in particular deal with the evolution of magnetic fields in turbulent plasmas. We especially emphasize (i) the necessity of renormalizing equations of motion in turbulence where velocity and magnetic fields become H\`older singular; (ii) the breakdown of Laplacian determinism (spontaneous stochasticity) for turbulent magnetic fields; and (iii) the possibility of eliminating the notion of magnetic field lines, using instead magnetic path lines as trajectories of Alfvenic wave-packets. These methodologies are then exemplified with their application to the problem of magnetic reconnection -- rapid change in magnetic field pattern that accelerates plasma -- a ubiquitous phenomenon in astrophysics and laboratory plasmas. The necessity of smoothing out rough velocity and magnetic fields on a finite scale L implies that magnetohydrodynamic equations should be regarded as effective field theories with running parameters depending upon the scale L.


![[mdfiles/2504.10763.md|2504.10763]]
### AI Justification:
The paper is highly relevant to my research on "magnetic dynamics of plasmas" as it discusses "the evolution of magnetic fields in turbulent plasmas" and addresses the complex interactions within magnetohydrodynamics that can lead to "emergent magnetic behaviors." Furthermore, the examination of "effective field theories" and the role of turbulence aligns well with my interest in "force interactions shaping magnetic dynamics" across various scales.
# (4/382) http://arxiv.org/pdf/2504.17855v2


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic fields in the Eos Cloud... dynamically important fields in the interface between atomic and molecular gas
**Janik Karoly,Kate Pattle,Blakesley Burkhart,Thavisha Dharmawardena,B-G Andersson,Thomas J. Haworth**


#mhd
### Abstract:
The recently-discovered Eos molecular cloud, is a CO-dark, low-density cloud located at a distance of approximately 94 pc from the Sun which does not appear to have formed stars at any point in its history. In this paper we investigate the magnetic fields in the Eos cloud, near the interface between the atomic Cold Neutral Medium (CNM) and molecular gas, using dust emission and extinction polarimetry. A Histogram of Relative Orientation analysis shows that the magnetic field is preferentially parallel to the density structure of the cloud, while a Davis-Chandrasekhar-Fermi analysis finds magnetic field strengths of 8 $\pm$ 4 $\mu$ G across the Eos cloud and 12 $\pm$ 4 $\mu$ G in the somewhat denser MBM 40 sub-region. These results are consistent with a previous estimate of magnetic field strength in the Local Bubble and suggest that the fields in the Eos cloud are dynamically important compared to both gravity and turbulence. Our findings are fully consistent with the expected behavior of magnetized, non-self-gravitating gas near the CNM/molecular cloud boundary.


![[mdfiles/2504.17855.md|2504.17855]]
### AI Justification:
This paper is highly relevant to your interests as it investigates "the magnetic fields in the Eos cloud" and emphasizes their "dynamically important" role, aligning with your focus on magnetic field amplification and the interactions of forces shaping magnetic dynamics in astrophysical plasmas. The study employs methods such as "dust emission and extinction polarimetry" and examines "the magnetic field strengths" at the interface of atomic and molecular gas, which directly addresses your interest in multi-scale magnetic dynamics.
# (5/382) http://arxiv.org/pdf/2504.19711v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic Moment-Field Interactions, A Universal Mechanism for Particle Energization
**Anil Raghav,Ajay Kumar,Mariyam Karari,Shubham Kadam,Kalpesh Ghag,Kishor Kumbhar,...**


#mhd
### Abstract:
Magnetic reconnection is a pivotal mechanisms in the energization and heating of cosmic plasmas, yet the exact process of energy transfer during these events remain elusive. Traditional models, which focus on acoustic and magnetohydrodynamic waves and micro/nano-flares, fall short of explaining the extreme heating of the solar corona and the origins of the supersonic solar wind. In this study, we provide compelling observational evidence from Wind spacecraft data supporting the Raghav effect, a mechanism where interactions between the magnetic moments of charged particles and dynamic magnetic fields result in abrupt kinetic energy changes. Our analysis demonstrates that the observed proton plasma heating is consistent with theoretical predictions, establishing the Raghav effect as a universal mechanism for particle energization. This discovery offers a unified framework for understanding energy dynamics across a wide range of astrophysical magnetised plasma environments.


![[mdfiles/2504.19711.md|2504.19711]]
### AI Justification:
This paper is highly relevant to your research as it explores "magnetic reconnection" and "energy transfer during these events," aligning well with your focus on "magnetic dynamics of plasmas." Furthermore, the introduction of the "Raghav effect" as a universal mechanism for particle energization can provide insights into the "magnetic field amplification" and the interactions that shape magnetic dynamics within plasma environments, which are core aspects of your work.
# (6/382) http://arxiv.org/pdf/2504.19202v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Explosive growth of large-scale magnetic fluctuations due to particle scattering on developed small-scale Weibel turbulence in magnetoactive plasma
**N. A. Emelyanov,Vl. V. Kocharovsky**


#mhd
### Abstract:
The analytical theory of non-linear generation of large-scale magnetic turbulence in anisotropic magnetoactive plasma in the quasilinear approximation without taking into account the direct non-linear interaction of individual harmonics is constructed. It is shown that anomalous collisions of particles due to scattering on small-scale fluctuations of the developed Weibel turbulence lead to instability of long-wave harmonics, which are stable in the linear approximation. The non-linear growth of such harmonics at a given anisotropy of the particle velocity distribution, consistent with the dynamics of short-wave perturbations at the saturation stage and possible anisotropic particle injection, occurs in the superexponential regime and corresponds to an explosive-type instability. The growth law of the large-scale magnetic field is found analytically and the critical time of explosive instability is estimated.


![[mdfiles/2504.19202.md|2504.19202]]
### AI Justification:
This paper is highly relevant to your research interests due to its focus on "large-scale magnetic fluctuations" and "non-linear generation of large-scale magnetic turbulence," which directly aligns with your emphasis on magnetic field amplification and the interactions in plasma environments. Additionally, the exploration of "Weibel turbulence" and its effects on "instability of long-wave harmonics" ties into your interest in emergent magnetic dynamics and the complex behavior of magnetic fields within turbulent plasma, providing valuable insights into multi-scale magnetic phenomena.
# (7/382) http://arxiv.org/pdf/2504.17842v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Magnetic Keys to Massive Star Formation... The Western $η$ Carinae Giant Molecular Cloud
**Peter J. Barnes,Stuart D. Ryder,Giles Novak,Laura M. Fissel**


#mhd
### Abstract:
We present SOFIA/HAWC+ continuum polarisation data on the magnetic fields threading 17 pc-scale massive molecular clumps at the western end of the $\eta$ Car GMC (Region 9 of CHaMP, representing all stages of star formation from pre-stellar to dispersing via feedback), revealing important details about the field morphology and role in the gas structures of this clump sample. We performed Davis-Chandrasekhar-Fermi and Histogram of Relative Orientation analyses tracing column densities 25.0 $<$ log( $N$ /m $^{-2}$ ) $<$ 27.2. With HRO, magnetic fields change from mostly parallel to column density structures to mostly perpendicular at a threshold $N_{\rm crit}$ = (3.7 $\pm$ 0.6) $\times$ 10 $^{26}$ m $^{-2}$ , indicating that gravitational forces exceed magnetic forces above this value. The same analysis in 10 individual clumps gives similar results, with the same clear trend in field alignments and a threshold $N_{\rm crit}$ = (1.9 $^{+1.5}_{-0.8}$ ) $\times$ 10 $^{26}$ m $^{-2}$ . In the other 7 clumps, the alignment trend with $N$ is much flatter or even reversed, inconsistent with the usual HRO pattern. Instead, these clumps fields reflect external environmental forces, such as from the nearby HII region NGC 3324. DCF analysis reveals field strengths somewhat higher than typical of nearby clouds, with the $Bn$ data lying mostly above the Crutcher (2012) relation. The mass...flux ratio $\lambda$ across all clumps has a gaussian distribution, with log $\lambda_{\rm DCF}$ = -0.75 $\pm$ 0.45 (mean $\pm\sigma$ )... only small areas are dominated by gravity. However, a significant trend of rising log $\lambda$ with falling $T_{\rm dust}$ parallels Pitts et als (2019) result... $T_{\rm dust}$ falls as $N_{\rm H_2}$ rises towards clump centres. Thus, in this massive clump sample, magnetic fields provide enough support against gravity to explain their overall low star formation rate.


![[mdfiles/2504.17842.md|2504.17842]]
### AI Justification:
This paper is highly relevant to your research interests as it examines "magnetic fields threading 17 pc-scale massive molecular clumps," directly aligning with your focus on "magnetic dynamics of plasmas in the interstellar medium." Additionally, the analysis of the "interactions between magnetic, gravitational, and thermal forces" and their influence on clump structures offers valuable insights into "force interactions shaping magnetic dynamics" in astrophysical environments.
# (8/382) http://arxiv.org/pdf/2504.15538v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Scale-dependent alignment in compressible magnetohydrodynamic turbulence
**James R. Beattie,Amitava Bhattacharjee**


#mhd
### Abstract:
Using $10,\!080^3$ grid simulations, we analyze scale-dependent alignment in driven, compressible, no net-flux magnetohydrodynamic turbulence. The plasma self-organizes into localized, strongly aligned regions. Alignment spans all primitive variables and their curls. Contrary to incompressible theory, velocity-magnetic alignment scales as $\theta(\lambda) \sim \lambda^{1/8}$ , where $\lambda$ is the scale, suggesting a distinct three-dimensional eddy anisotropy and a much higher critical transition scale toward a reconnection-mediated cascade.


![[mdfiles/2504.15538.md|2504.15538]]
### AI Justification:
This paper is highly relevant to your research interests as it explores "scale-dependent alignment" in compressible magnetohydrodynamic turbulence, directly addressing "scale-dependent magnetic structuring." The findings on "velocity-magnetic alignment" and "self-organized localized regions" provide key insights into how turbulent dynamics shape magnetic fields in plasma environments, aligning well with your focus on emergent behaviors in the interstellar medium.
# (9/382) http://arxiv.org/pdf/2504.13352v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Foundations of magnetohydrodynamics
**Jarett LeVan,Scott Baalrud**


#mhd
### Abstract:
In this tutorial, a derivation of magnetohydrodynamics (MHD) valid beyond the usual ideal gas approximation is presented. Non-equilibrium thermodynamics is used to obtain conservation equations and linear constitutive relations. When coupled with Maxwells equations, this provides closed fluid equations in terms of material properties of the plasma, described by the equation of state and transport coefficients. These properties are connected to microscopic dynamics using the Irving-Kirkwood procedure and Green-Kubo relations. Symmetry arguments and the Onsager-Casimir relations allow one to vastly simplify the number of independent coefficients. Importantly, expressions for current density, heat flux, and stress (conventionally Ohms law, Fouriers law, and Newtons law) take different forms in systems with a non-ideal equation of state. The traditional form of the MHD equations, which is usually obtained from a Chapman-Enskog solution of the Boltzmann equation, corresponds to the ideal gas limit of the general equations.


![[mdfiles/2504.13352.md|2504.13352]]
### AI Justification:
This paper closely aligns with my research interests as it explores the derivation of magnetohydrodynamics (MHD) that goes beyond the ideal gas approximation, which is essential for understanding magnetic field behavior in various astrophysical contexts. Furthermore, by addressing non-equilibrium thermodynamics and conservation equations, it provides valuable insights into the force interactions shaping magnetic dynamics and how they manifest in plasma environments, particularly relevant to my focus on the amplification and evolution of magnetic fields in the interstellar medium.
# (10/382) http://arxiv.org/pdf/2504.09722v2


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Thousand-Pulsar-Array programme on MeerKAT -- XVI. Mapping the Galactic magnetic field with pulsar observations
**L. S. Oswald,P. Weltevrede,B. Posselt,S. Johnston,A. Karastergiou,M. E. Lower**


#mhd
### Abstract:
Measuring the magnetic field of the Milky Way reveals the structure and evolution of the galaxy. Pulsar rotation measures (RMs) provide a means to probe this Galactic magnetic field (GMF) in three dimensions. We use the largest single-origin data set of pulsar measurements, from the MeerKAT Thousand-Pulsar-Array, to map out GMF components parallel to pulsar lines of sight. We also present these measurements for easy integration into the consolidated RM catalogue, RMTable. Focusing on the Galactic disk, we investigate competing theories of how the GMF relates to the spiral arms, comparing our observational map with five analytic models of magnetic field structure. We also analyse RMs to extragalactic radio sources, to help build up a three-dimensional picture of the magnetic structure of the galaxy. In particular, our large number of measurements allows us to investigate differing magnetic field behaviour in the upper and lower halves of the Galactic plane. We find that the GMF is best explained as following the spiral arms in a roughly bisymmetric structure, with antisymmetric parity with respect to the Galactic plane. This picture is complicated by variations in parity on different spiral arms, and the parity change location appears to be shifted by a distance of 0.15 kpc perpendicular to the Galactic plane. This indicates a complex relationship between the large-scale distributions of matter and magnetic fields in our galaxy. Future pulsar discoveries will help reveal the origins of this relationship with greater precision, as well as probing the locations of local magnetic field inhomogenities.


![[mdfiles/2504.09722.md|2504.09722]]
### AI Justification:
The paper is highly relevant to your interests in theoretical astrophysics and magnetic dynamics, particularly in its examination of the Galactic magnetic field (GMF) as it relates to the spiral arms, which aligns with your focus on "how magnetic fields behave, interact, and amplify across various scales." Additionally, the findings on "competing theories of how the GMF relates to the spiral arms" directly connect with your research on "force interactions shaping magnetic dynamics," providing valuable insights into the structure and behavior of magnetic fields within plasma environments.
# (11/382) http://arxiv.org/pdf/2504.07895v2


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic Fields of Satellite Galaxies Stronger Than Comparable Centrals in TNG100
**Bryanne McDonough,Alexander Poulin**


#mhd
### Abstract:
Magnetic fields exist in and around galaxies, but the properties of these fields have not been fully explored due to the challenges inherent in observing and modeling them. In this Note, we explore the differences in magnetic field strength of central and satellite galaxies from the magnetohydrodynamic TNG100 simulation. We find that on average, magnetic fields in satellite galaxies are roughly an order of magnitude stronger than those of central galaxies with comparable masses. The difference is greater for satellites that have already approached within $1 R_{200}$ of their host galaxies. These results indicate that magnetic fields in satellite galaxies are amplified by environmental processes as they fall into a host halo.


![[mdfiles/2504.07895.md|2504.07895]]
### AI Justification:
This paper is highly relevant to your research interests, particularly in the area of *Magnetic Field Amplification*, as it discusses the amplification of magnetic fields in satellite galaxies through environmental processes. The findings related to the comparative strength of magnetic fields in *central* versus *satellite galaxies* support your focus on how magnetic dynamics evolve within plasma structures across various scales, thus addressing your interest in *scale-dependent magnetic structuring*.
# (12/382) http://arxiv.org/pdf/2504.10755v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### TURB-MHD... an open-access database of forced homogeneous magnetohydrodynamic turbulence
**Damiano Capocci,Luca Biferale,Fabio Bonaccorso,Moritz Linkmann**


#mhd
### Abstract:
We present TURB-MHD, a database formed by six datasets of three-dimensional incompressible homogeneous magnetohydrodynamic turbulence maintained by a large-scale random forcing with minimal injection of cross helicity. Five of them describe a stationary state including one characterised by a weak background magnetic field. The remaining dataset is non-stationary and is featured by a strong background magnetic field. The aim is to provide datasets that clearly exhibit the phenomenon of the total energy cascade from the large to the small scales generated by the large-scale energy injection and one showing a partial inverse kinetic energy cascade from the small to the large scales. This database offers the possibility to realize a wide variety of analyses of fully developed magnetohydrodynamic turbulence from the sub-grid scale filtering up to the validation of an a posteriori LES. TURB-MHD is available for download using the SMART-Turb portal http...//smart-turb.roma2.infn.it.


![[mdfiles/2504.10755.md|2504.10755]]
### AI Justification:
This paper is highly relevant to your research interests as it focuses on "homogeneous magnetohydrodynamic turbulence" which aligns with your interest in "how magnetic fields behave, interact, and amplify" in plasma environments. Additionally, the database offers insights into "the total energy cascade from the large to the small scales," directly addressing your interest in "emergent magnetic dynamics in turbulent plasmas" and scale-dependent structuring.
# (13/382) http://arxiv.org/pdf/2504.09550v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Spatially resolved polarization variation of the Crab Nebula
**Chao Zuo,Fei Xie,Mingyu Ge,Wei Deng,Kuan Liu,Fabio La Monaca,...**


#mhd
### Abstract:
We examined the spatially resolved polarization variations in the Crab Nebula over 2 yr, using observational data from the Imaging X-ray Polarimetry Explorer, and offer key insights into its magnetic field structures and evolution. The results show significant temporal changes in the polarization degree (PD) across three regions of interest in the 2-8 keV energy band. Regions (a) and (b), located in the northern and the southwestern parts of the study area, exhibit PD variations with significance levels greater than 4 sigma and 3 sigma , respectively. Region (c), located in the southwest,shows a notable decrease in PD with a significance greater than 5 sigma. However, no significant variation in the polarization angle was observed. Meanwhile, notable flux variations were detected, likely influenced by dynamic processes such as magnetized turbulence within the nebula.


![[mdfiles/2504.09550.md|2504.09550]]
### AI Justification:
The paper is highly relevant to your research interests as it explores "polarization variations" and "magnetic field structures and evolution" in the Crab Nebula, which aligns closely with your focus on "magnetic dynamics of plasmas in the interstellar medium." Furthermore, the investigation of "dynamic processes such as magnetized turbulence" pertains directly to your interest in "emergent magnetic dynamics in turbulent plasmas."
# (14/382) http://arxiv.org/pdf/2504.06701v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A multi-scale view of the magnetic field morphology in the hot molecular core G31.41+0.31
**C. Y. Law,M. T. Beltran,R. S. Furuya,J. M. Girart,D. Galli,R. Cesaroni,...**


#mhd
### Abstract:
Multiscale studies of the morphology and strength of the magnetic field are crucial to properly unveil its role and relative importance in high-mass star and cluster formation. G31.41+0.31 (G31) is a hub-filament system that hosts a high-mass protocluster embedded in a hot molecular core (HMC). G31 is one of the few sources showing a clear hourglass morphology of the magnetic field on scales between 1000 au and a few 100 au in previous interferometric observations. This strongly suggests a field-regulated collapse. To complete the study of the magnetic field properties in this high-mass star-forming region, we carried out observations with the James Clerk Maxwell Telescope $850 \mu$ m of the polarized dust emission. These observations had a spatial resolution of $\sim$ 0.2 pc at 3.75 kpc. The aim was to study the magnetic field in the whole cloud and to compare the magnetic field orientation toward the HMC from $\sim$ 50,000 au to $\sim$ 260 au scales. The large-scale ( $\sim$ 5 pc) orientation of the magnetic field toward the position of the HMC is consistent with that observed at the core ( $\sim$ 4,000 au) and circumstellar ( $\sim$ 260 au) scales. The self-similarity of the magnetic field orientation at these different scales might arise from the brightest sources in the protocluster, whose collapse is dragging the magnetic field. These sources dominate the gravitational potential and the collapse in the HMC. The cloud-scale magnetic field strength of the G31 hub-filament system, which we estimated using the Davis-Chandrasekhar-Fermi method, is in the range 0.04--0.09 mG. The magnetic field orientation in the star-forming region shows a bimodal distribution, and it changes from an NW--SE direction in the north to an E--W direction in the south [abridged abstract].


![[mdfiles/2504.06701.md|2504.06701]]
### AI Justification:
This paper is highly relevant to your research interests as it discusses "multiscale studies of the morphology and strength of the magnetic field," aligning with your focus on "magnetic dynamics of plasmas in the interstellar medium." Additionally, it addresses "field-regulated collapse," which is critical to understanding the interactions between gravitational forces and magnetic fields, a key aspect of your research on how these forces shape magnetic dynamics.
# (15/382) http://arxiv.org/pdf/2504.07051v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Revisiting X-ray polarization of the shell of Cassiopeia A using spectropolarimetric analysis
**Alessandra Mercuri,Emanuele Greco,Jacco Vink,Riccardo Ferrazzoli,Silvia Perri**


#mhd
### Abstract:
X-ray synchrotron radiation is expected to be highly polarized. Thanks to the Imaging X-ray Polarimetry Explorer (IXPE), it is now possible to evaluate the degree of X-ray polarization in sources such as supernova remnants (SNRs). Jointly using IXPE data and high-resolution Chandra observations, we perform a spatially resolved spectropolarimetric analysis of SNR Cassiopeia A (Cas A). We focus in the 3-6 keV energy band on regions near the shell dominated by nonthermal synchrotron emission. By combining IXPEs polarization sensitivity with Chandras higher spatial and spectral resolution, we constrain the local polarization degree (PD) and polarization angle (PA) across the remnant. Our analysis reveals PD values ranging locally from 10% to 26%, showing significant regional variations that underscore the complex magnetic field morphology of Cas A. The polarization vectors indicate a predominantly radial magnetic field, consistent with previous studies. Thanks to the improved modeling of thermal contamination using Chandra data, we retrieve higher PD values compared to earlier IXPE analysis and more significant detections with respect to the standard IXPEOBSSIM analysis. Finally, we also estimate the degree of magnetic turbulence {\eta} from the measured photon index and PD, under the assumption of an isotropic fluctuating field across the shell of Cas A.


![[mdfiles/2504.07051.md|2504.07051]]
### AI Justification:
The paper is highly relevant to your research interests as it provides insight into "the complex magnetic field morphology" of a supernova remnant, which aligns with your focus on "magnetic dynamics of plasmas" and the "interactions between magnetic, gravitational, and thermal forces." Additionally, the analysis of "magnetic turbulence" and the use of modeling techniques resonates with your interest in theoretical models and studies examining the "multi-scale dynamics of magnetic fields in plasma environments."
# (16/382) http://arxiv.org/pdf/2504.06073v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A Data-constrained Magnetohydrodynamic Simulation of Successive X-class Flares in Solar Active Region 13842 I. Dynamics of the Solar Eruption Associated with the X7.1 Solar Flare
**Keitarou Matsumoto,Satoshi Inoue,Nian Liu,Keiji Hayashi,Ju Jing,Haimin Wang**


#mhd
### Abstract:
We investigated the initiation and the evolution of an X7.1-class solar flare observed in solar active region NOAA 13842 on October 1, 2024, based on a data-constrained magnetohydrodynamic (MHD) simulation. The nonlinear force-free field (NLFFF) extrapolated from the photospheric magnetic field about 1 hour before the flare was used as the initial condition for the MHD simulations. The NLFFF reproduces highly sheared field lines that undergo tether-cutting reconnection in the MHD simulation, leading to the formation of a highly twisted magnetic flux rope (MFR), which then erupts rapidly driven by both torus instability and magnetic reconnection. This paper focuses on the dynamics of the MFR and its role in eruptions. We find that magnetic reconnection in the pre-eruption phase is crucial in the subsequent eruption driven by the torus instability. Furthermore, our simulation indicates that magnetic reconnection also directly enhances the torus instability. These results suggest that magnetic reconnection is not just a byproduct of the eruption due to reconnecting of post-flare arcade, but also plays a significant role in accelerating the MFR during the eruption.


![[mdfiles/2504.06073.md|2504.06073]]
### AI Justification:
The paper is highly relevant to your research interests, particularly in its focus on "magnetic reconnection" and "magnetic flux rope" dynamics, which align with your study of "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas." Additionally, the exploration of how "torus instability" interfaces with magnetic reconnection provides insights into how magnetic fields evolve in plasma environments, crucial for understanding their behavior across various astrophysical scales.
# (17/382) http://arxiv.org/pdf/2504.04742v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Unveiling Physical Conditions and Star Formation Processes in the G47 Filamentary Cloud
**O. R. Jadhav,L. K. Dewangan,A. Haj Ismail,N. K. Bhadari,A. K. Maity,Ram Kesh Yadav,...**


#mhd
### Abstract:
We present a multi-wavelength study of the filamentary cloud G47 (d $\sim$ 4.44 kpc), which hosts the mid-infrared bubbles N98, B1, and B2. The SMGPS 1.3 GHz continuum map detects ionized emission toward all the bubbles, marking the first detection of ionized emission toward the B2 bubble. Analysis of the unWISE 12.0 $\mu$ m image, Spitzer 8.0 $\mu$ m image, and the Herschel column density and temperature maps reveals two previously unreported hub-filament system candidates associated with the HII regions B2 and N98, which are powered by massive OB stars. This indirectly favours the applicability of a global non-isotropic collapse (GNIC) scenario for massive star formation in N98 and B2. The position-position-velocity diagram of FUGIN $^{13}$ CO(1-0) shows significant velocity variations from 61 to 53 km s $^{-1}$ toward areas between B2 and N98, where the magnetic field morphology exhibits significant curvature, and high velocity dispersion (i.e., 2.3--3.1 km s $^{-1}$ ) is observed. This may be explained by the expansion of the HII regions B2 and N98. The energy budget of the cloud, estimated using SOFIA/HAWC+ and molecular line data, suggests that the magnetic field dominates over turbulence and gravity in G47. Furthermore, the radial column density and velocity profiles of G47 display signatures of converging flows in a sheet-like structure. The relative orientations between the magnetic field and local gravity suggest that G47 may undergo gravitational contraction along the magnetic field lines once it becomes magnetically supercritical.


![[mdfiles/2504.04742.md|2504.04742]]
### AI Justification:
The paper is highly relevant to your interests in theoretical astrophysics and plasma physics as it investigates the "magnetic field morphology" in the G47 filamentary cloud, which aligns with your focus on "how magnetic fields behave, interact, and amplify across various scales." Additionally, the finding that "the magnetic field dominates over turbulence and gravity" resonates with your interest in "force interactions shaping magnetic dynamics," offering insights into emergent magnetic behaviors in turbulent plasma environments.
# (18/382) http://arxiv.org/pdf/2504.04648v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Basic Pattern of Three-dimensional Magnetic Reconnection within Strongly Turbulent Current Sheets
**Yulei Wang,Xin Cheng,Mingde Ding**


#mhd
### Abstract:
Magnetic reconnection is a fundamental mechanism of driving eruptive phenomena of different scales and may be coupled with turbulence as suggested by recent remote-sensing and in-situ observations. However, the specific physics behind the complex three-dimensional (3D) turbulent reconnection remains mysterious. Here, we develop a novel methodology to identify and analyze multitudes of multi-scale reconnection fragments within a strongly turbulent current sheet (CS) and apply it to a state-of-the-art numerical simulation of turbulent reconnection for solar flares. It is determined that the reconnection fragments tend to appear as quasi-2D sheets forming along local magnetic flux surfaces, and, due to strong turbulence, their reconnection flow velocities and reconnection rates are significantly broadened statistically but are scale-independent. Each reconnection fragment is found to be surrounded by strongly fluctuated in/out-flows and has a widely distributed reconnection rate, mainly in the range of 0.01-0.1. The results, for the first time, provide quantitative measurements of 3D magnetic reconnection in strongly turbulent flare CSs, offering insights into the cascading laws of 3D reconnection in other turbulent plasmas.


![[mdfiles/2504.04648.md|2504.04648]]
### AI Justification:
This paper is highly relevant to your interests as it directly addresses the dynamics of magnetic fields in the context of "turbulent reconnection," which aligns with your focus on "emergent magnetic dynamics in turbulent plasmas." Moreover, the findings regarding "multi-scale reconnection fragments" and their implications for "strong turbulence" provide valuable insights into how magnetic fields may interact with turbulence, which is a central theme in your research on magnetic dynamics within astrophysical plasmas.
# (19/382) http://arxiv.org/pdf/2503.23634v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic fields in the multiphase interstellar medium of the Milky Way... turbulent kinetic and magnetic energy density relation
**Amit Seta,N. M. McClure-Griffiths**


#mhd
### Abstract:
Magnetic fields are an important component of the interstellar medium (ISM) of galaxies. The thermal gas in the ISM has a multiphase structure, broadly divided into ionised, atomic, and molecular phases. The connection between the multiphase ISM gas and magnetic field is not known and this makes it difficult to account for their impact on star formation and galaxy evolution. Usually, in star formation studies, a relationship between the gas density, $n$ and magnetic field strength, $B$ , is assumed to study magnetic fields impact. However, this requires the knowledge of the geometry of star-forming regions and ambient magnetic field orientation. Here, we use the Zeeman magnetic field measurements from the literature for the atomic and molecular ISM and supplement the magnetic field estimates in the ionised ISM using pulsar observations to find a relation between the turbulent kinetic, $E_{\rm kin}$ , and magnetic, $E_{\rm mag}$ , energy densities. Across all three phases and over a large range of densities ( $10^{-3}\,{\rm cm}^{-3} \lesssim n \lesssim 10^{7}\,{\rm cm}^{-3} $ ), we find $ E_{\rm mag} \propto E_{\rm kin}$ . Furthermore, we use phase-wise probability density functions of density, magnetic fields, and turbulent velocities to show that the magnetic field fluctuations are controlled by both density and turbulent velocity fluctuations. This work demonstrates that a combination of both the density and turbulent velocity determines magnetic fields in the ISM.


![[mdfiles/2503.23634.md|2503.23634]]
### AI Justification:
This paper is highly relevant to my research interests as it investigates "magnetic fields in the multiphase interstellar medium" and addresses the connection between "turbulent kinetic energy" and "magnetic energy density," which directly relates to my focus on the "emergent magnetic dynamics in turbulent plasmas." Furthermore, the exploration of how both "density and turbulent velocity" influence magnetic field behavior aligns closely with my interest in "scale-dependent magnetic structuring" within various plasma environments.
# (20/382) http://arxiv.org/pdf/2503.24154v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Non-linear saturation of gravito-inertial modes excited by tidal resonances in binary neutron stars
**Alexis Reboul-Salze,Aurelie Astoul,Hao-Jui Kuan,Arthur G. Suvorov**


#mhd
### Abstract:
During the last seconds of a binary neutron-star merger, the tidal force can excite stellar oscillation modes to large amplitudes. From the perspective of premerger electromagnetic emissions and next-generation gravitational-wave detectors, gravity ( $g-$ ) modes constitute a propitious class. However, existing estimates for their impact employ linear schemes which may be inaccurate for large amplitudes, as achieved by tidal resonances. With rotation, inertial modes can be excited as well and while their non-linear saturation has been studied, an extension to fully-consistent gravito-inertial modes, especially in the neutron-star context, is an open problem. We study the linear and non-linear saturation of gravito-inertial modes and investigate the astrophysical consequences for binary neutron-star mergers, including the possibility of resonance-induced dynamo activity. A new (non-)linear formulation based on the separation of equilibrium and dynamical tides is developed. Implementing this into the 3D pseudo-spectral code MagIC, a suite of non-linear simulations of tidally-excited flows with an entropy/composition gradient in a stably-stratified Boussinesq spherical-shell are carried out. The new formulation accurately reproduces results of linear calculations for gravito-inertial modes with a free surface for low frequencies. For a constant-density cavity, we show that the axisymmetric differential rotation induced by nonlinear $_2g$ and $_1g$ modes may theoretically be large enough to amplify an ambient magnetic field to $\gtrsim 10^{14}$ G. In addition, rich non-linear dynamics are observed in the form of a parametric instability for the $_1g$ mode. The stars are also spun-up, which extends the resonance window for any given mode.


![[mdfiles/2503.24154.md|2503.24154]]
### AI Justification:
This paper is highly relevant to my research in theoretical astrophysics and plasma physics as it explores the "non-linear saturation of gravito-inertial modes" and the consequent potential for "resonance-induced dynamo activity." The investigation of how these modes can "amplify an ambient magnetic field to $\gtrsim 10^{14}$ G" directly aligns with my interest in magnetic field amplification and the interactions between different forces shaping magnetic dynamics within astrophysical plasmas.
# (21/382) http://arxiv.org/pdf/2503.22553v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Tracing the Heliospheric Magnetic Field via Anisotropic Radio-Wave Scattering
**Daniel L. Clarkson,Eduard P. Kontar,Nicolina Chrysaphi,A. Gordon Emslie,Natasha L. S. Jeffrey,Vratislav Krupar,...**


#mhd
### Abstract:
Astrophysical radio sources are embedded in turbulent magnetised environments. In the 1 MHz sky, solar radio bursts are the brightest sources, produced by electrons travelling along magnetic field lines from the Sun through the heliosphere. We demonstrate that the magnetic field not only guides the emitting electrons, but also directs radio waves via anisotropic scattering from density irregularities in the magnetised plasma. Using multi-vantage-point type III solar radio burst observations and anisotropic radio wave propagation simulations, we show that the interplanetary field structure is encoded in the observed radio emission directivity, and that large-scale turbulent channelling of radio waves is present over large distances, even for relatively weak anisotropy in the embedded density fluctuations. Tracing the radio emission at many frequencies (distances), the effects of anisotropic scattering can be disentangled from the electron motion along the interplanetary magnetic field, and the emission source locations are unveiled. Our analysis suggests that magnetic field structures within turbulent media could be reconstructed using radio observations and is found consistent with the Parker field, offering a novel method for remotely diagnosing the large-scale field structure in the heliosphere and other astrophysical plasmas.


![[mdfiles/2503.22553.md|2503.22553]]
### AI Justification:
The paper is highly relevant to your research interests as it examines how "magnetic field structures within turbulent media" interact with phenomena in plasma environments, aligning with your focus on "emergent magnetic dynamics in turbulent plasmas." Additionally, the novel method proposed for "remotely diagnosing the large-scale field structure" could provide valuable insights into "magnetic field amplification" and interaction forces within astrophysical plasmas, which are critical aspects of your work.
# (22/382) http://arxiv.org/pdf/2503.20721v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Imprints of Stellar Feedback on Magnetic Fields in the Iris Nebula NGC 7023
**Ekta Sharma,Kate Pattle,Di Li,Chang Won Lee,Maheswar Gopinathan,Tao-Chung Ching,...**


#mhd
### Abstract:
We present 850 $\mu$ m polarized continuum observations carried out with the POL-2 polarimeter mounted on the James Clerk Maxwell Telescope (JCMT) towards NGC 7023 located in the Cepheus Flare region. NGC 7023 is a reflection nebula powered by a Herbig Ae Be star HD 200775 and also identified as a hub in the hub-filament cloud, LDN 1172/1174. We detect submillimetre emission well towards the northern (identified as C1) and the eastern region of the reflection nebula. We investigated the polarization structure and the magnetic field (B-field) morphology, which is found to be curved and follows the clump morphology. The comparison of the B-field morphology at the clump scales ( $\sim$ 0.02 pc) with that of the envelope ( $\sim$ 0.5 pc) suggests that the field lines are not preserved from envelope to clump scales, implying that an external factor may be responsible for disturbing the B-field structure. We estimated a magnetic field strength of 179 $\pm$ 50 $\mu$ G in the starless core, 121 $\pm$ 34 $\mu$ G in the protostellar core with a class I source and 150 $\pm$ 42 $\mu$ G in the protostellar core with a class II source using the $N_{2}H^{+}$ (1-0) line observed with 13.7 m single dish radio telescope at Taeduk Radio Astronomy Observatory (TRAO). The stability analysis using these B-field strengths gives magnetically sub-critical values, while the magnetic, gravitational, and outflow kinetic energies are roughly balanced. We also suggest that the reordering of the magnetic field lines could be due to the interaction with the already evolved high-velocity outflow gas around the central star, which hints at the presence of outflow feedback.


![[mdfiles/2503.20721.md|2503.20721]]
### AI Justification:
This paper directly addresses the "magnetic dynamics of plasmas in the interstellar medium" by exploring the "polarization structure and the magnetic field (B-field) morphology" within the Iris Nebula, which aligns closely with your interest in how "magnetic fields behave, interact, and amplify" at different scales. It also investigates the interactions between magnetic fields and "outflow kinetic energies," providing insight into the complex "force interactions shaping magnetic dynamics" that you are focused on in your research.
# (23/382) http://arxiv.org/pdf/2503.19131v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Turbulent dynamos in a collapsing cloud
**Muhammed Irshad P,Pallavi Bhat,Kandaswamy Subramanian,Anvar Shukurov**


#mhd
### Abstract:
The amplification of magnetic fields is crucial for understanding the observed magnetization of stars and galaxies. Turbulent dynamo is the primary mechanism responsible for that but the understanding of its action in a collapsing environment is still rudimentary and relies on limited numerical experiments. We develop an analytical framework and perform numerical simulations to investigate the behavior of small-scale and large-scale dynamos in a collapsing turbulent cloud. This approach is also applicable to expanding environments and facilitates the application of standard dynamo theory to evolving systems. Using a supercomoving formulation of the magnetohydrodynamic (MHD) equations, we demonstrate that dynamo action in a collapsing background leads to a super-exponential growth of magnetic fields in time, significantly faster than the exponential growth seen in stationary turbulence. The enhancement is mainly due to the increasing eddy turnover rate during the collapse, which boosts the instantaneous growth rate of the dynamo. We also show that the final saturated magnetic field strength exceeds the expectation from considerations of pure flux-freezing or energy equipartition with the turbulence, scaling as $B \propto \rho^{5/6}$ , where $\rho$ is the cloud density. Apart from establishing a formal framework for the studies of magnetic field evolution in collapsing (or expanding) turbulent plasmas, these findings have significant implications for early star and galaxy formation, suggesting that magnetic fields can be amplified to dynamically relevant strengths much earlier than previously thought.


![[mdfiles/2503.19131.md|2503.19131]]
### AI Justification:
This paper is highly relevant to your research interests as it explores the "amplification of magnetic fields" through "turbulent dynamos" in a "collapsing turbulent cloud," addressing your focus on how magnetic dynamics evolve and amplify in astrophysical plasmas. Furthermore, the findings on "super-exponential growth" and implications for early star and galaxy formation align closely with your interest in "scale-dependent magnetic structuring" across various astrophysical environments.
# (24/382) http://arxiv.org/pdf/2503.17920v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Linear Analysis and Simulations of the Cosmic-Ray Streaming Instability... the Importance of Oblique Waves
**Shuzhe Zeng,Xue-Ning Bai,Xiaochen Sun**


#mhd
### Abstract:
Cosmic-ray (CR) streaming instability (CRSI) is believed to play an important role in CR transport and CR feedback to galaxies. It drives the growth of magnetohydrodynamic (MHD) waves that scatter CRs, and leads to energy/momentum exchange between CRs and interstellar medium. Despite extensive research on CRSI, its dependence on the thermodynamic state of the gas and its multidimensional effects have not been systematically studied. In this study, we derive the dispersion relation of the CRSI for three types of MHD waves including their dependence on propagation direction and plasma $\beta$ (the ratio of thermal pressure to magnetic pressure). We verify the analytical dispersion relation with one-dimensional and two-dimensional magnetohydrodynamic particle-in-cell simulations. Furthermore, we use 2D simulations to investigate the role of oblique MHD waves in scattering CRs, and find that these waves are important in helping low-energy particles overcome the 90-degree pitch angle barrier. While magnetosonic waves tend to be damped by transit time damping under typical conditions, oblique Alfv\en waves likely play an important role in low- $\beta$ plasmas.


![[mdfiles/2503.17920.md|2503.17920]]
### AI Justification:
This paper is highly relevant to your research interests as it directly addresses “magnetohydrodynamic (MHD) waves” and their impact on cosmic-ray transport within astrophysical plasmas, which aligns with your focus on “magnetic dynamics of plasmas in the interstellar medium.” Additionally, the study's examination of the "dependencies on propagation direction" provides insights into "scale-dependent magnetic structuring," which is crucial for understanding how magnetic fields interact across different cosmic scenarios.
# (25/382) http://arxiv.org/pdf/2503.12682v2


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Dual Theory of MHD Turbulence
**Alexander Migdal**


#mhd
### Abstract:
We present an exact analytic solution for decaying incompressible magnetohydrodynamic (MHD) turbulence. Our solution reveals a dual formulation in terms of two interacting Euler ensembles--one for hydrodynamic and another for magnetic circulation. This replaces empirical scaling laws with an infinite set of power terms with calculable decay exponents, some of which appear as complex-conjugate pairs related to the Riemann zeta function. A key result of our analysis is the explicit dependence of the solution on the Prandtl number ( $\mathrm{Pr} = \nu/\eta$ ), leading to a phase transition at $\mathrm{Pr} = 1$ . In the $\mathrm{Pr}<1$ regime, turbulence is dominated by hydrodynamic fluctuations, while for $\mathrm{Pr}>1$ , two distinct solutions emerge... a metastable one in which magnetic fluctuations grow with $\mathrm{Pr}$ and a stable one where they remain balanced with hydrodynamic fluctuations. We compare our theoretical predictions with recent direct numerical simulations (DNS) and discuss their implications for astrophysical plasmas, fusion devices, and laboratory MHD experiments. Our results provide a rigorous mathematical framework for understanding MHD turbulence and its dependence on fundamental parameters, offering a new perspective on turbulence in highly conducting fluids.


![[mdfiles/2503.12682.md|2503.12682]]
### AI Justification:
This paper is highly relevant to your research interests in theoretical astrophysics and plasma physics, particularly in its exploration of "MHD turbulence" and how magnetic fluctuations interact with hydrodynamic fluctuations. The discussion surrounding the "dependence of the solution on the Prandtl number" and the implications for "astrophysical plasmas" align closely with your focus on magnetic field behavior and interactions within plasma environments across various scales.
# (26/382) http://arxiv.org/pdf/2503.15067v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Exploring magnetised galactic outflows in starburst dwarf galaxies NGC 3125 and IC 4662
**Sam Taziaux,Ancla Muller,Bjorn Adebahr,Aritra Basu,Christoph Pfrommer,Michael Stein,...**


#mhd
### Abstract:
The study of radio emission in starburst dwarf galaxies provides a unique opportunity to investigate the mechanisms responsible for the amplification and transport of magnetic fields. Local dwarfs are often considered proxies for early-Universe galaxies, so this study may provide insights into the role of non-thermal components in the formation and evolution of larger galaxies. By investigating the radio continuum spectra and maps of the starburst dwarf galaxies, we aim to draw conclusions on their magnetic field strengths and configurations, as well as the dynamics of cosmic ray (CR) transport. We perform a radio continuum polarimetry study of two of the brightest starburst IRAS Revised Bright Galaxy Sample (RBGS) dwarf galaxies, NGC 3125 and IC 4662. By combining data of the Australian Telescope Compact Array (2.1 GHz) and MeerKAT (1.28 GHz), we analyse the underlying emission mechanism and the CR transport in these systems. We find flat spectra in those dwarf galaxies over the entire investigated frequency range, which sharply contrasts with observations of massive spiral galaxies. Because the expected cooling time of CR electrons is much shorter than their escape time, we would expect a steepened steady-state CR electron spectrum. The flat observed spectra suggest a substantial contribution from free-free emission at high frequencies and absorption at low frequencies, which may solve this puzzle. For NGC 3125, we measure a degree of polarisation between 0.75% and 2.6%, implying a turbulent field and supporting the picture of a comparably large thermal emission component that could be sourced by stellar radiation feedback and supernovae.


![[mdfiles/2503.15067.md|2503.15067]]
### AI Justification:
This paper is highly relevant to your research interests as it explores the "mechanisms responsible for the amplification and transport of magnetic fields" within starburst dwarf galaxies, which aligns with your focus on "magnetic field amplification" and the "emergent magnetic dynamics in turbulent plasmas." The study's use of "radio continuum polarimetry" and analysis of cosmic ray transport also provides valuable insights into "force interactions shaping magnetic dynamics," making it a strong candidate for contributing to your understanding of complex, multi-scale magnetic behaviors in plasma environments.
# (27/382) http://arxiv.org/pdf/2503.15350v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Connecting a Magnetized Disk to a Convective Low-mass Protostar... A Global Three-dimensional Model of Boundary Layer Accretion
**Shinsuke Takasao,Takashi Hosokawa,Kengo Tomida,Kazunari Iwasaki**


#mhd
### Abstract:
In the early stages of star formation, boundary layer accretion, where protostars accrete material from disks extending down to their surfaces, plays a crucial role. Understanding how a magneto-rotational-instability (MRI)-active disk connects to a protostars surface remains a significant challenge. To investigate the mechanisms of mass and angular momentum transfer, we develop a global, three-dimensional magnetohydrodynamic model of boundary layer accretion around a magnetized, convective low-mass protostar. Our results reveal that angular momentum transport mechanisms transition significantly from the outer MRI-active disk to the protostellar surface. Various mechanisms--MRI, spiral shocks, coronal accretion, jets, and disk winds--contribute to angular momentum transfer, resulting in three distinct disk structures... (1) the MRI-active disk, (2) the transition layer, and (3) the boundary layer. The simulated protostar is strongly magnetized due to the accumulation of the disk fields, wrapping by disk toroidal fields, and stellar dynamo activity. Magnetic concentrations analogous to starspots form on the protostar and interact with the rotating disk gas to generate spiral shocks. These shocks play a key role in driving accretion. These findings demonstrate the necessity of global MHD models for a comprehensive understanding of angular momentum transport. Additionally, we identify explosive events triggered by magnetic reconnection in both the protostar and the disk atmosphere. We also find decretion flows in the disk midplane, which may be important for the radial transport of refractory materials, such as Calcium-Aluminium-rich Inclusions (CAIs) precursor gas, to the outer disk.


![[mdfiles/2503.15350.md|2503.15350]]
### AI Justification:
This paper is highly relevant to your research interests as it explores "magnetic dynamics" in the context of a "magneto-rotational-instability (MRI)-active disk," which fits your focus on "magnetic field amplification" and interactions affecting magnetic structures. The global magnetohydrodynamic model detailed in the study provides insights into "angular momentum transport mechanisms" and their relation to "magnetic reconnection," which resonates with your interest in the role of magnetic fields across varying astrophysical scales.
# (28/382) http://arxiv.org/pdf/2503.14726v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Characterizing Magnetic Properties of Young Protostars in Orion
**Bo Huang,Josep M. Girart,Ian W. Stephens,Philip C. Myers,Qizhou Zhang,Paulo Cortes,...**


#mhd
### Abstract:
The {\em B}-field Orion Protostellar Survey (BOPS) recently obtained polarimetric observations at 870 ${\rm \mu m}$ towards 61 protostars in the Orion molecular clouds with $\sim 1^{\prime\prime}$ spatial resolution using the Atacama Large Millimeter/submillimeter Array. From the BOPS sample, we selected the 26 protostars with extended polarized emission within a radius of $\sim 6^{\prime\prime}$ (2400~au) around the protostar. This allows to have sufficient statistical polarization data to infer the magnetic field strength. The magnetic field strength is derived using the Davis-Chandrasekhar-Fermi method. The underlying magnetic field strengths are approximately 2.0~mG for protostars with a standard hourglass magnetic field morphology, which is higher than the values derived for protostars with rotated hourglass, spiral, and complex magnetic field configurations ( $\lesssim1.0$ ~mG). This suggests that the magnetic field plays a more significant role in envelopes exhibiting a standard hourglass field morphology, and a value of $\gtrsim2.0$ mG would be required to maintain such a structure at these scales. Furthermore, most protostars in the sample are slightly supercritical, with mass-to-flux ratios $\lesssim3.0$ . In particular, the mass-to-flux ratios for all protostars with a standard hourglass magnetic field morphology are lower than 3.0. However, these ratios do not account for the contribution of the protostellar mass, which means they are likely significantly underestimated.


![[mdfiles/2503.14726.md|2503.14726]]
### AI Justification:
This paper is highly relevant to your research interests in theoretical astrophysics and plasma physics, particularly in its focus on “magnetic field strength” and “standard hourglass magnetic field morphology” in protostars within the Orion molecular clouds. It addresses your interest in magnetic field amplification and its role in shaping plasma environments, specifically by using methods like the Davis-Chandrasekhar-Fermi method to characterize these dynamics.
# (29/382) http://arxiv.org/pdf/2503.11776v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Radio study of the colliding wind binary HD93129A near periastron and its surroundings
**Paula Benaglia,Santiago del Palacio,Juliana Saponara,Agustina B. Blanco,Michael De Becker,Benito Marcote**


#mhd
### Abstract:
HD93129A is an O+O stellar system whose CWR has been mapped by high angular resolution observations at cm wavelengths. The synchrotron nature of the radio emission confirms its particle accelerator status. According to astrometric measurements since 1996, the system has an orbital period of ~120 yr and recently went through its periastron passage. We characterize the radio emission during the epoch of periastron passage, when the particle density and the local magnetic energy density in the CWR increase. We monitored HD93129A and surroundings at 2.1, 5.5 and 9 GHz with the ATCA over 17 months, with a ~2-month cadence. Previous ATCA data and data collected using other radio observatories were also included. We obtained radio light curves in subbands per band per epoch. The flux densities show an average rise of a factor four from 2003 to 2018, with the caveat that the 2009-2018 time lapse is devoid of data, and a similar decay between 2018 to 2020. We fit the spectral energy distribution of quasi-simultaneous data at three epochs and find that the magnetic-to-thermal pressure ratio does not remain constant along the orbit, possible suggesting magnetic field amplification close to periastron. In the 2019 epoch, we estimate a magnetic field strength of ~1.1G in the apex of the CWR. The evolution of the SED and spectral index is also presented. By combining ATCA and ASKAP images a spectral index map was obtained in an area of 30 size. The radio emission in the direction of other massive binary systems in the field (WR22, WR25 and HD93250) was measured and briefly discussed. Intensive radio monitoring allows us to track the evolution of physical conditions in the shocks. The general trend of decreasing emission of HD93129A in the high-frequency bands in 2019-2020 suggests that the system is at post-periastron, consistent with model predictions. (Abridged)


![[mdfiles/2503.11776.md|2503.11776]]
### AI Justification:
This paper is highly relevant to your research interests as it discusses the "magnetic-to-thermal pressure ratio" and the possibility of "magnetic field amplification close to periastron," directly aligning with your focus on how "dynamos and other mechanisms drive the amplification and evolution of magnetic fields in astrophysical plasmas." Additionally, the investigation of the "local magnetic energy density" and its changes due to interactions in a stellar system provides valuable insights into the complex "magnetic dynamics of plasmas in the interstellar medium."
# (30/382) http://arxiv.org/pdf/2503.06449v2


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Wind of Change... Faraday Rotation in a Simulated Large Magellanic Cloud
**Hilay Shah,Mark Krumholz,Naomi McClure-Griffiths**


#mhd
### Abstract:
Magnetic fields significantly influence the structure of galaxies interstellar media, but our understanding of magnetic field strengths and structures in external galaxies is severely limited. The Large Magellanic Cloud (LMC) offers a unique opportunity for improvement due to its proximity and large angular size, allowing for various detailed observations, particularly rich datasets of rotation measures and dispersion measures (RM and DM). However, interpreting these measurements is challenging due to the need for assumptions about the 3D structure for which we can only access line-of-sight integrated quantities. To address this, we conduct a suite of high-resolution magnetohydrodynamic (MHD) simulations of the LMC, incorporating star formation, star-by-star feedback, and ram pressure stripping by the Milky Ways circumgalactic medium (CGM), experienced as a circumgalactic wind in the frame of the LMC. Synthetic observations of these simulations allow us to identify parameters that closely match observed RM and DM values. Our best model, which is an excellent match to the real LMC, yields magnetic field strengths of $\sim 1.4~\mu{\rm G} $ (ordered) and $ \sim 1.6~\mu{\rm G}$ (turbulent). In this model, Milky Way CGM wind experienced by the LMC plays a critical role in shaping the RM data, with the bulk of the RM signal arising not from the LMCs plane, but from warm, $\sim 10^4$ K, gas in a Reynolds layer region $\sim 1$ kpc off the plane where relatively dense material stripped from the LMC is partially ionised by hard extragalactic radiation fields. This finding suggests that we should be cautious about generalising inferences from the LMC to other galaxies that may not be shaped by similar interactions.


![[mdfiles/2503.06449.md|2503.06449]]
### AI Justification:
This paper is highly relevant to your research interests in theoretical astrophysics and plasma physics, particularly through its focus on “magnetic fields significantly influence the structure of galaxies” and the presentation of “high-resolution magnetohydrodynamic (MHD) simulations.” The integration of magnetic dynamics, star formation, and feedback mechanisms in the Large Magellanic Cloud (LMC) relates closely to your study of “magnetic field amplification” and elucidates how external forces shape “the structure and behavior of magnetic fields within plasma environments."
# (31/382) http://arxiv.org/pdf/2503.08765v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Detection of magnetic fields in superclusters of galaxies
**G. V. Pignataro,S. P. O'Sullivan,A. Bonafede,G. Bernardi,F. Vazza,E. Carretti**


#mhd
### Abstract:
Magnetic fields in large scale structure filaments beyond galaxy clusters remain poorly understood. Superclusters offer a unique setting to study these low density environments, where weak signals make detection challenging. The Faraday rotation measure (RM) of polarized sources along supercluster lines of sight helps constrain magnetic field properties in these regions. This study aims to determine magnetic field intensity in low density environments within superclusters using RM measurements at different frequencies. We analyzed three nearby (z<0.1) superclusters, Corona Borealis, Hercules, and Leo, where polarization observations were available at 1.4 GHz and 144 MHz. Our catalogue includes 4497 polarized background sources with RM values from literature and unpublished 144 MHz data. We constructed 3D density cubes for each supercluster to estimate density at RM measurement locations. By grouping RM values into three density bins (outskirts, filaments, and nodes) we examined RM variance linked to mean density. We found an RM variance excess of 2.5 \pm 0.5 rad^2 m^{-4} between the lowest-density regions outside the supercluster and the low-density filamentary regions within. This suggests an intervening magnetic field in the supercluster filaments. Modeling the RM variance with a single scale, randomly oriented magnetic field, we constrained the line of sight magnetic field to B_{//} = 19^{+50}_{-8} nG after marginalizing over reversal scale and path length. Our findings align with previous studies of large scale structure filaments, suggesting that adiabatic compression alone (B_{||} \sim 2 nG) cannot fully explain the observed field strengths. Other amplification mechanisms likely contribute to the evolution of magnetic fields in superclusters.


![[mdfiles/2503.08765.md|2503.08765]]
### AI Justification:
This paper is highly relevant to your research interests, as it directly addresses "magnetic fields" in the context of "superclusters" and explores how these fields are detected and measured in low-density environments, aligning with your focus on "magnetic dynamics of plasmas in the interstellar medium." The findings regarding the "magnetic field intensity" and the mention of "amplification mechanisms" provide unique insights into the evolution of magnetic fields, specifically the interactions and structures formed in "magnetic dynamics" that are central to your studies.
# (32/382) http://arxiv.org/pdf/2503.05198v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The JCMT BISTRO Survey... Unveiling the Magnetic Fields around Galactic Center
**Meng-Zhe Yang,Shih-Ping Lai,Janik Karoly,Kate Pattle,Xing Lu,David Eden,...**


#mhd
### Abstract:
We acquired 450 {\mu}m and 850 {\mu}m dust continuum polarization observations toward the inner region of the Central Molecular Zone (CMZ) as part of the B-Fields In Star-Forming Region Observations (BISTRO) survey using the POL-2 polarimeter on the James Clerk Maxwell Telescope. These observations encompassed three dense structures... the 20 km s{^{-1}} cloud (20MC), 50 km s{^{-1}} cloud (50MC), and circumnuclear disk (CND). Our aim is to investigate the magnetic field morphology and strength in the inner region of the CMZ using polarized dust continuum and the Davis-Chandrasekhar-Fermi method. The magnetic field morphology is highly ordered in all three dense regions. The plane-of-sky magnetic field strengths are {\sim}1 mG for the 20MC and the 50MC, and {\sim}2 mG for the CND. We compare the energy contributions of turbulence, gravity, and thermal motion with that of the magnetic field using the plasma {\beta}, mass-to-flux ratio, and Alfv\en Mach number. The outcomes reveal the magnetic field stands out as the predominant factor within the inner region of the CMZ. The dominance of the magnetic field may explain the low star-forming rate in the CMZ. We further investigate the dust grain alignment efficiency by exploring the relationship between polarization fraction and total intensity. The results suggest that dust grains are well aligned with the magnetic fields.


![[mdfiles/2503.05198.md|2503.05198]]
### AI Justification:
This paper is highly relevant to your research interests as it investigates the "magnetic field morphology and strength" in the Central Molecular Zone, which aligns with your focus on "magnetic field amplification" and "force interactions shaping magnetic dynamics." Moreover, the study's exploration of how turbulence, gravity, and thermal motion interact with the magnetic field closely relates to your interest in understanding "complex, emergent magnetic behaviors within plasma structures."
# (33/382) http://arxiv.org/pdf/2503.03493v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Dust Polarisation and Magnetic Field Structure in the Centre of NGC253 with ALMA
**Davide Belfiori,Rosita Paladino,Annie Hughes,Jean-Philippe Bernard,Dana Alina,Ivana Beslic,...**


#mhd
### Abstract:
Magnetic fields have an impact on galaxy evolution at multiple scales. They are particularly important for starburst galaxies, where they play a crucial role in shaping the interstellar medium (ISM), influencing star formation processes and interacting with galactic outflows. The primary aim of this study is to obtain a parsec scale map of dust polarisation and B-field structure within the central starburst region of NGC253. This includes examining the relationship between the morphology of B-fields, galactic outflows and the spatial distribution of super star clusters (SSC), to understand their combined effects on the galaxys star formation and ISM. We used ALMA full polarisation data in Bands 4 (145 GHz) and 7 (345 GHz) with resolution of 25 and 5 pc scale, respectively. According to our SED fitting analysis, the observed Band 4 emission is a combination of dust, synchrotron and free-free, while Band 7 traces only dust. The polarisation fraction (PF) of the synchrotron component is 2%, while that of the dust component is 0.3%. The B-fields orientation maps in both bands at common resolution show that the same B-fields structure is traced by dust and synchrotron emission at scales of 25 pc. The B-field morphology suggests a coupling with the multiphase outflow, while the distribution of PF in Band 7 showed to be correlated with the presence of SSC. We observed a significant anti-correlation between polarisation fraction and column density in both Bands 4 and 7. A negative correlation between PF and dispersion angle function was observed in Band 4 but was nearly absent in Band 7 at native resolution, suggesting that the tangling of B-field geometry along the plane of the sky is the main cause of depolarisation at 25 pc scales, while other factors play a role at 5 pc scales.


![[mdfiles/2503.03493.md|2503.03493]]
### AI Justification:
This paper is highly relevant to your research interests as it examines "magnetic fields" and their influence on the interstellar medium (ISM), particularly in the context of a starburst galaxy, which aligns with your focus on "magnetic dynamics of plasmas in the interstellar medium." Additionally, the study utilizes observational data to analyze the "morphology of B-fields" and their interactions with "galactic outflows," directly corresponding to your interest in "force interactions shaping magnetic dynamics."
# (34/382) http://arxiv.org/pdf/2502.11552v2


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The JCMT BISTRO Survey... Magnetic Fields Align with Orbital Structure in the Galactic Center
**Janik Karoly,Derek Ward-Thompson,Kate Pattle,Steven N. Longmore,James Di Francesco,Anthony Whitworth,...**


#mhd
### Abstract:
We present the magnetic field in the dense material of the Central Molecular Zone (CMZ) of the Milky Way, traced in 850 $\mu$ m polarized dust emission as part of the James Clerk Maxwell Telescope (JCMT) B-fields In STar-forming Region Observations (BISTRO) Survey. We observe a highly ordered magnetic field across the CMZ between Sgr B2 and Sgr C, which is strongly preferentially aligned with the orbital gas flows within the clouds of the CMZ. We find that the observed relative orientations are non-random at a $>$ 99% confidence level and are consistent with models in which the magnetic field vectors are aligned within 30 $^{o}$ to the gas flows in 3D. The deviations from aligned magnetic fields are most prominent at positive Galactic longitudes, where the CMZ clouds are more massive, denser, and more actively forming stars. Our observed strongly preferentially parallel magnetic field morphology leads us to hypothesize that in the absence of star formation, the magnetic field in the CMZ is entrained in the orbital gas flows around Sgr A $^{*}$ , while gravitational collapse and feedback in star-forming regions can locally reorder the field. This magnetic field behavior is similar to that observed in the CMZ of the nuclear starburst galaxy NGC 253. This suggests that despite its current low star formation rate, the CMZ of the Milky Way is analogous to those of more distant, actively star-forming, galaxies.


![[mdfiles/2502.11552.md|2502.11552]]
### AI Justification:
This paper is highly relevant to your work as it investigates "magnetic field amplification" within the complex plasma dynamics of the Central Molecular Zone (CMZ), aligning closely with your interest in the behavior and interaction of magnetic fields in astrophysical plasmas. Additionally, the findings regarding the alignment of magnetic fields with "orbital gas flows" in the CMZ offer valuable insights into the "force interactions shaping magnetic dynamics," thereby directly connecting with the multi-scale magnetic structuring you aim to explore.
# (35/382) http://arxiv.org/pdf/2503.03015v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Non-Linear behavior of the Electron Cyclotron Drift Instability and the Suppression of Anomalous Current
**Aryan Sharma,Andrei Smolyakov,Raymond J. Spiteri**


#mhd
### Abstract:
We present results of one-dimensional collisionless simulations of plasma turbulence and related anomalous electron current of the Electron Cyclotron Drift Instability (ECDI). Our highly resolved, long-term simulations of xenon plasma in the magnetic field performed with the WarpX particle-in-cell (PIC) code show several intermediate non-linear stages before the system enters a stationary state with significantly increased electron temperature and a finite level of energy in the electrostatic fluctuations. In early and intermediate non-linear stages, the fluctuations are driven by the electron cyclotron resonances gradually shifting from higher ( $m>1$ ) modes to the fundamental $m=1$ resonance. Enhanced resonant growth is observed from the point when the cyclotron $m=1$ mode coincides with the most unstable ion-acoustic mode. In the final stage, the anomalous electron current existing in intermediate stages is quenched to zero. Following this quenching, our simulations reveal a transition from ECDI-driven dynamics to saturated ion-acoustic turbulence. The modification of the electron and ion distribution functions and their roles in the non-linear developments and saturation of the instability are analyzed at different non-linear stages. The non-linear development of ECDI driven by the $\mathbf{E} \times \mathbf{B}$ electron drift from the applied current and the ECDI driven by the ion beam perpendicular to the magnetic field are compared and characterized as two perspectives of the instability, observed through different Doppler-shifted frames. An extension of this work incorporating full the dynamics of magnetized ions for ECDI driven by a hydrogen ion beam is shown to develop full beam inversion, with the periodic bursts of growth-saturation cycles of ECDI.


![[mdfiles/2503.03015.md|2503.03015]]
### AI Justification:
This paper is highly relevant to your research interests as it explores the "non-linear stages" of the Electron Cyclotron Drift Instability (ECDI), which relates directly to your focus on the “interaction of turbulent plasmas” and their “complex magnetic dynamics.” The use of "one-dimensional collisionless simulations" to study plasma turbulence and its influence on "anomalous electron current" provides insights into how magnetic fields evolve and interact within plasma environments, aligning well with your interest in "magnetic field amplification" and "scale-dependent magnetic structuring."
# (36/382) http://arxiv.org/pdf/2503.01971v1


### Rating: 9/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 90%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Projection-angle effects when `observing` a turbulent magnetized collapsing molecular cloud. II. Magnetic field
**A. Tritsis,S. Basu,C. Federrath**


#mhd
### Abstract:
Interstellar magnetic fields are thought to play a fundamental role in the evolution of star-forming regions. Polarized thermal dust emission serves as a key probe for understanding the structure of the POS component of the magnetic field. However, inclination effects can significantly influence the apparent morphology of the magnetic field and lead to erroneous conclusions regarding its dynamical importance. Our aim is to investigate how projection-angle effects impact dust polarization maps and to explore new ways for accessing the inclination angle of the mean component of the magnetic field with respect to the POS. We post-processed a 3D ideal MHD simulation of a turbulent collapsing molecular cloud and produced synthetic dust polarization measurements under various projection angles, ranging from `face-on` (i.e., viewed along the mean magnetic field direction) to `edge-on` (perpendicular to the mean magnetic field direction). Additionally, we used synthetic PPV data cubes from the CO (J = 1-0) transition, presented in a companion paper. The projected magnetic-field morphology is found to be highly affected by the projection angle with the hourglass morphology being clearly visible only for projection angles close to edge-on. We find that the direction of the apparent `flow` between successive velocity channels in the simulated PPV data cubes shows an increasing correlation with the synthetic dust polarization observations, as the cloud is observed closer to an edge-on orientation. Based on this property, we developed a new method to probe the inclination angle of the magnetic field relative to the POS. We validated our approach by generating additional synthetic data (PPV cubes and polarization maps) at an earlier stage of the clouds evolution and demonstrated an excellent quantitative agreement between the derived inclination angle and the true observational angle.


![[mdfiles/2503.01971.md|2503.01971]]
### AI Justification:
This paper is highly relevant to your interests as it investigates "the projection-angle effects" on the morphology of magnetic fields within a "turbulent collapsing molecular cloud," aligning well with your focus on "magnetic dynamics" and "force interactions shaping magnetic dynamics." Additionally, the use of "3D ideal MHD simulation" to analyze how inclination affects magnetic field observations touches upon your interest in theoretical models and the multi-scale dynamics of astrophysical plasmas.
# (37/382) http://arxiv.org/pdf/2504.20534v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A polarized view of the young Pulsar Wind Nebula 3C 58 with IXPE
**N. Bucciantini,J. Wong,R. W. Romani,F. Xie,C. -Y. Ng,S. Silvestri,...**


#mhd
### Abstract:
Pulsar Wind nebulae (PWNe), are among the most efficient particle accelerators in the Universe, however understanding the physical conditions and the magnetic geometry in their inner region has always proved elusive. X-ray polarization provides now a unique opportunity to investigate the magnetic field structure and turbulence properties close to where high energy particles are accelerated. Here we report on the recent X-ray polarization measurement of the PWN 3C 58 by the International X-ray Polarimeter Explorer (IXPE). 3C 58 is a young system displaying a characteristic jet-torus structure which, unlike other PWNe, is seen almost edge on. This nebula shows a high level of integrated polarization ~ 22% at an angle ~ 97deg, with an implied magnetic field oriented parallel to the major axis of the inner torus, suggesting a toroidal magnetic geometry with little turbulence in the interior, and an intrinsic level of polarization possibly approaching the theoretical limit for synchrotron emission. No significant detection of a polarized signal from the associated pulsar was found. These results confirm that the internal structure of young PWNe is far less turbulent than previously predicted, and at odds with multidimensional numerical simulations.


![[mdfiles/2504.20534.md|2504.20534]]
### AI Justification:
This paper is relevant to your interests as it explores the "magnetic geometry" and "turbulence properties" within a Pulsar Wind Nebula, which aligns with your focus on how "magnetic fields behave and interact" in various plasma environments. The findings regarding the "toroidal magnetic geometry" and its implications on the turbulence in PWNe provide valuable insights into the "emergent magnetic dynamics in turbulent plasmas," making it a significant addition to your research on magnetic dynamics in astrophysics.
# (38/382) http://arxiv.org/pdf/2502.05268v2


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Zooming In On The Multi-Phase Structure of Magnetically-Dominated Quasar Disks... Radiation From Torus to ISCO Across Accretion Rates
**Philip F. Hopkins,Kung-Yi Su,Norman Murray,Ulrich P. Steinwandel,Nicholas Kaaz,Sam B. Ponnada,...**


#mhd
### Abstract:
Recent radiation-thermochemical-magnetohydrodynamic simulations resolved formation of quasar accretion disks from cosmological scales down to ~300 gravitational radii $R_{g}$ , arguing they were hyper-magnetized (plasma $\beta\ll1$ supported by toroidal magnetic fields) and distinct from traditional $\alpha$ -disks. We extend these, refining to $\approx 3\,R_{g}$ around a $10^{7}\,{\rm M_{\odot}}$ BH with multi-channel radiation and thermochemistry, and exploring a factor of 1000 range of accretion rates ( $\dot{m}\sim0.01-20$ ). At smaller scales, we see the disks maintain steady accretion, thermalize and self-ionize, and radiation pressure grows in importance, but large deviations from local thermodynamic equilibrium and single-phase equations of state are always present. Trans-Alfvenic and highly-supersonic turbulence persists in all cases, and leads to efficient vertical mixing, so radiation pressure saturates at levels comparable to fluctuating magnetic and turbulent pressures even for $\dot{m}\gg1$ . The disks also become radiatively inefficient in the inner regions at high $\dot{m}$ . The midplane magnetic field remains primarily toroidal at large radii, but at super-Eddington $\dot{m}$ we see occasional transitions to a poloidal-field dominated state associated with outflows and flares. Large-scale magnetocentrifugal and continuum radiation-pressure-driven outflows are weak at $\dot{m}<1$ , but can be strong at $\dot{m}\gtrsim1$ . In all cases there is a scattering photosphere above the disk extending to $\gtrsim 1000\,R_{g}$ at large $\dot{m}$ , and the disk is thick and flared owing to magnetic support (with $H/R$ nearly independent of $\dot{m}$ ), so the outer disk is strongly illuminated by the inner disk and most of the inner disk continuum scatters or is reprocessed at larger scales, giving apparent emission region sizes as large as $\gtrsim 10^{16}\,{\rm cm}$ .


![[mdfiles/2502.05268.md|2502.05268]]
### AI Justification:
This paper is relevant to your research interests as it discusses the "formation of quasar accretion disks" within a "magnetically-dominated" context, directly aligning with your focus on magnetic field amplification and dynamics within plasma environments. Additionally, the exploration of "Trans-Alfvenic and highly-supersonic turbulence" connects with your interest in emergent magnetic dynamics influenced by turbulence in astrophysical plasmas.
# (39/382) http://arxiv.org/pdf/2504.18986v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A multi-messenger window into galactic magnetic fields and black hole mergers with LISA
**Anuraag Reddy,Nathan Steinle,Samar Safi-Harb,Jo-Anne Brown**


#mhd
### Abstract:
Large-scale (i.e., $\gtrsim {\rm kpc}$ ) and micro-Gauss scale magnetic fields have been observed throughout the Milky Way and nearby galaxies. These fields depend on the geometry and matter-energy composition, can display complicated behavior such as direction reversals, and are intimately related to the evolution of the source galaxy. Simultaneously, gravitational-wave astronomy offers a new probe into astrophysical systems, for example the Laser Interferometer Space Antenna (LISA) will observe the mergers of massive (i.e., $M ~> 10^6$ M $_{\odot}$ ) black-hole binaries and provide extraordinary constraints on the evolution of their galactic hosts. In this work, we show how galactic, large-scale magnetic fields and their electromagnetic signatures are connected with LISA gravitational-wave observations via their common dependence on the massive black-hole binary formation scenario of hierarchical galaxy mergers. Combining existing codes, we astrophysically evolve a population of massive binaries from formation to merger and find that they are detectable by LISA with signal-to-noise ratio $\sim 10^3$ which is correlated with quantities from the progenitors phase of circumbinary disk migration such as the maximum magnetic field magnitude $|\mathbf{B}| \approx 7 \,\mu$ G, polarized intensity, and Faraday rotation measure. Interesting correlations result between these observables arising from their dependencies on the black-hole binary total mass, suggesting a need for further analyses of the full parameter space. We conclude with a discussion on this new multi-messenger window into galactic magnetic fields.


![[mdfiles/2504.18986.md|2504.18986]]
### AI Justification:
This paper is relevant to your research interests because it discusses "large-scale magnetic fields" and explores their evolution in relation to astrophysical phenomena, aligning with your focus on "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas." Additionally, the connection made between magnetic fields and gravitational wave observations through "hierarchical galaxy mergers" adds a unique perspective on how these forces intersect in shaping magnetic dynamics across different scales.
# (40/382) http://arxiv.org/pdf/2504.18109v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Universal relations between parallel and perpendicular spectral power law exponents in non-axisymmetric magnetohydrodynamic turbulence
**Ramesh Sasmal,Supratik Banerjee**


#mhd
### Abstract:
Following a general heuristic approach, algebraic constraints are established between the parallel and perpendicular power-law exponents of non-axisymmetric, highly aligned magnetohydrodynamic turbulence, both with and without strong imbalance between the Els\`asser variables. Such relations are universal both for the regimes of weak and strong turbulence and are useful to predict the corresponding turbulent power spectra. For scale-dependent alignment, a Boldyrev-type $k^{-3/2}$ perpendicular spectrum emerges transverse to the direction of alignment whereas a $k^{-5/3}$ spectrum is obtained for the same if the alignment becomes scale-independent. However, regardless of the nature of alignment, our analysis consistently yields a $k_{\parallel}^{-2}$ spectrum - commonly observed in both numerical simulations and in-situ data of solar wind. In appropriate limit, previously obtained algebraic relations and power spectra for axisymmetric MHD turbulence (Galtier, Pouquet and Mangeney, Physics of Plasmas, 2005) are successfully recovered. Finally, more realistic relations capturing weak Alfv\enic turbulence (with constant $k_{\parallel}$ ) and the transition to strong turbulence are derived along with their corresponding power spectra.


![[mdfiles/2504.18109.md|2504.18109]]
### AI Justification:
The paper presents universal relations between spectral power law exponents in non-axisymmetric magnetohydrodynamic turbulence, which is directly relevant to my focus on "Emergent Magnetic Dynamics in Turbulent Plasmas." The discussion of "magnetohydrodynamic turbulence" and "power spectra" contributes to understanding how magnetic fields behave and interact within various plasma environments, aligning well with my interest in magnetic field amplification and the role of turbulence in plasma dynamics.
# (41/382) http://arxiv.org/pdf/2504.15335v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Plasma Instabilities Dominate Radioactive Transients Magnetic Fields... The self-confinement of leptons in Type Ia and Core-Collapse Supernovae, and Kilonovae
**Dhvanil D. Desai,Colby C. Haggerty,Benjamin J. Shappee,Michael A. Tucker,Zachary Davis,Chris Ashall,...**


#mhd
### Abstract:
The light curves of radioactive transients, such as supernovae and kilonovae, are powered by the decay of radioisotopes, which release high-energy leptons through $\beta^+$ and $\beta^-$ decays. These leptons deposit energy into the expanding ejecta. As the ejecta density decreases during expansion, the plasma becomes collisionless, with particle motion governed by electromagnetic forces. In such environments, strong or turbulent magnetic fields are thought to confine particles, though the origin of these fields and the confinement mechanism have remained unclear. Using fully kinetic particle-in-cell (PIC) simulations, we demonstrate that plasma instabilities can naturally confine high-energy leptons. These leptons generate magnetic fields through plasma streaming instabilities, even in the absence of pre-existing fields. The self-generated magnetic fields slow lepton diffusion, enabling confinement and transferring energy to thermal electrons and ions. Our results naturally explain the positron trapping inferred from late-time observations of thermonuclear and core-collapse supernovae. Furthermore, they suggest potential implications for electron dynamics in the ejecta of kilonovae. We also estimate synchrotron radio luminosities from positrons for Type Ia supernovae and find that such emission could only be detectable with next-generation radio observatories from a Galactic or local-group supernova in an environment without any circumstellar material.


![[mdfiles/2504.15335.md|2504.15335]]
### AI Justification:
This paper is relevant to your research interests as it addresses the "strong or turbulent magnetic fields" that interact with leptons in "collisionless" plasmas, aligning with your focus on how magnetic fields behave and interact within plasma environments. The use of "fully kinetic particle-in-cell (PIC) simulations" to demonstrate magnetic field self-generation through "plasma streaming instabilities" offers unique insights into the mechanisms of magnetic field amplification and dynamics, particularly in astrophysical contexts like supernovae and kilonovae.
# (42/382) http://arxiv.org/pdf/2504.15069v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Data-constrained Magnetohydrodynamic Simulation of a Filament Eruption in a Decaying Active Region 13079 on a Global Scale
**Yihua Li,Yang Guo,Jinhan Guo,M. D. Ding,Chun Xia,Rony Keppens**


#mhd
### Abstract:
Filaments are special plasma phenomena embedded in the solar atmosphere, characterized by unique thermodynamic properties and magnetic structures. Magnetohydrodynamic (MHD) simulations are useful to investigate the eruption mechanisms of filaments. We conduct a data-constrained zero- $\beta$ MHD simulation in spherical coordinates to investigate a C3.5 class flare triggered by an eruptive filament on 2022 August 15 in a decaying weak active region 13079. We reconstruct the three-dimensional coronal magnetic field using vector magnetograms and synoptic maps from the Solar Dynamics Observatory/Helioseismic and Magnetic Imager (SDO/HMI). We transform vector magnetic field into Stonyhurst heliographic spherical coordinates combined with a synoptic map and constructed a potential field source surface (PFSS) model with a magnetic flux rope (MFR) embedded using the Regularized Biot--Savart Laws (RBSL). Subsequently, we conduct a spherical zero- $\beta$ MHD simulation using the Message Passing Interface Adaptive Mesh Refinement Versatile Advection Code (MPI-AMRVAC) and replicated the entire dynamic process of the filament eruption consistent with observations. With the calculation of time-distance profile, Qusai-Separatrix Layers (QSL), and synthetic radiation from simulated current density, we find a good agreement between our simulation and observations in terms of dynamics and magnetic topology. Technically, we provide a useful method of advanced data-constrained simulation of weak active regions in spherical coordinates. Scientifically, the model allows us to quantitatively describe and diagnose the entire process of filament eruption.


![[mdfiles/2504.15069.md|2504.15069]]
### AI Justification:
This paper is highly relevant to your research because it utilizes magnetohydrodynamic (MHD) simulations to investigate the dynamics of plasma phenomena, particularly focusing on filament eruptions, language that resonates with your interest in "magnetic dynamics of plasmas." Additionally, the study involves a "data-constrained simulation" of magnetic field interactions in the solar atmosphere, which aligns with your emphasis on theoretical models and the amplification and evolution of magnetic fields across different scales.
# (43/382) http://arxiv.org/pdf/2504.13304v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Revealing the Accretion Flow in M87*... Insights from Faraday Rotation
**Constanza Echiburu-Trujillo,Jason Dexter**


#mhd
### Abstract:
The Faraday rotation measure (RM) is a commonly used tool to trace electron number density and magnetic fields in hot accretion flows, particularly in low-luminosity accreting supermassive black holes. We focus on the nuclear region of M87, which was observed at 230 GHz (1.3 mm) by the Event Horizon Telescope in 2019. It remains unclear whether this emission originates from the accretion flow, the jet base, or both. To probe the presence of an accretion flow, we explore the scenario where the linearly polarized emission from the counter-jet, visible at 43 GHz (7 mm), is Faraday-rotated by the accretion flow. We calculate theoretical predictions for counter-jet polarization using analytical and numerical models. In all cases, we find a Faraday-thick flow at 43 GHz (7 mm), with $\mathrm{RM} \sim 10^6$ rad m $^{-2}$ , and a polarization angle that follows a linear relationship with wavelength squared, consistent with external Faraday rotation. The more realistic model, which includes turbulence and magnetic field fluctuations, predicts that the polarization pattern should be time-dependent, and that the counter-jet emission is depolarized due to Faraday depth fluctuations across the accretion flow. Despite the Faraday thick regime and strong depolarization, the linear relationship persists, enabling us to constrain the flows physical properties. Comparing the counter-jet and forward-jet linear polarization states should enable detection of M87s accretion flow and provide lower limits on electron density, magnetic field strength, and mass accretion rate.


![[mdfiles/2504.13304.md|2504.13304]]
### AI Justification:
This paper is relevant to my research interests as it explores "Faraday rotation" to analyze "magnetic fields in hot accretion flows," which aligns with my focus on the behavior and amplification of magnetic fields in astrophysical plasmas. Furthermore, the investigation of how "turbulence and magnetic field fluctuations" affect polarization patterns in the context of M87* can provide valuable insights into emergent magnetic dynamics in turbulent plasma environments, which is a key area of my research.
# (44/382) http://arxiv.org/pdf/2504.12936v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Relative magnetic helicity under turbulent relaxation
**Sauli Lindberg,David MacTaggart**


#mhd
### Abstract:
Magnetic helicity is a quantity that underpins many theories of magnetic relaxation in electrically conducting fluids, both laminar and turbulent. Although much theoretical effort has been expended on magnetic fields that are everywhere tangent to their domain boundaries, many applications, both in astrophysics and laboratories, actually involve magnetic fields that are line-tied to the boundary, i.e. with a non-trivial normal component on the boundary. This modification of the boundary condition requires a modification of magnetic helicity, whose suitable replacement is called relative magnetic helicity. In this work, we investigate rigorously the behaviour of relative magnetic helicity under turbulent relaxation. In particular, we specify the normal component of the magnetic field on the boundary and consider the \emph{ideal limit} of resistivity tending to zero in order to model the turbulent evolution in the sense of Onsagers theory of turbulence. We show that relative magnetic helicity is conserved in this distinguished limit and that, for constant viscosity, the magnetic field can relax asymptotically to a magnetohydrostatic equilibrium.


![[mdfiles/2504.12936.md|2504.12936]]
### AI Justification:
This paper is relevant to your research interests as it explores the dynamics of magnetic helicity under turbulent conditions, a key aspect of how "magnetic fields interact with turbulence" to influence plasma behavior. The focus on "turbulent relaxation" and the implications for magnetic field conservation and evolution directly aligns with your interest in “magnetic field amplification” and the shaping of structures within plasma environments.
# (45/382) http://arxiv.org/pdf/2504.11776v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### ALMASOP. Detection of Turbulence-induced Mass Assembly Shocks in Starless Cores
**Shih-Ying Hsu,Sheng-Yuan Liu,Xunchuan Liu,Pak Shing Li,Tie Liu,Dipen Sahu,...**


#mhd
### Abstract:
Star formation is a series of mass assembly processes and starless cores, those cold and dense condensations in molecular clouds, play a pivotal role as initial seeds of stars. With only a limited sample of known starless cores, however, the origin and growth of such stellar precursors had not been well characterized previously. Meanwhile, the recent discovery of CH $_3$ OH emission, which is generally associated with desorbed icy mantle in warm regions, particularly at the periphery of starless cores also remains puzzling. We present sensitive ALMA (Band~3) observations (at 3~mm) toward a sample of newly identified starless cores in the Orion Molecular Cloud. The spatially resolved images distinctly indicate that the observed CH $_3$ OH and N $_2$ H $^+$ emission associated with these cores are morphologically anti-correlated and kinematically offset from each other. We postulate that the CH $_3$ OH emission highlights the desorption of icy mantle by shocks resulting from gas piling onto dense cores in the filaments traced by N $_2$ H $^+$ . Our magnetohydrodynamic (MHD) simulations of star formation in turbulent clouds combined with radiative transfer calculations and imaging simulations successfully reproduced the observed signatures and reaffirmed the above scenario at work. Our result serves as an intriguing and exemplary illustration, a snapshot in time, of the dynamic star-forming processes in turbulent clouds. The results offer compelling insights into the mechanisms governing the growth of starless cores and the presence of gas-phase complex organic molecules associated with these cores.


![[mdfiles/2504.11776.md|2504.11776]]
### AI Justification:
This paper is relevant to your research interests as it involves magnetohydrodynamic (MHD) simulations to explore the dynamics of magnetic fields in turbulent clouds, aligning with your focus on "the magnetic dynamics of plasmas in the interstellar medium." The investigation of how turbulence induces mass assembly processes, highlighted by the detection of CH $_3$ OH and N $_2$ H $^+$ emissions, provides insights into "emergent magnetic dynamics in turbulent plasmas," which is a key aspect of your research focus.
# (46/382) http://arxiv.org/pdf/2504.05680v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Simultaneous construction of fast equator, poleward meridional flow, and near-surface shear layer in solar magnetohydrodynamic calculation
**H. Hotta**


#mhd
### Abstract:
We carry out an unprecedented high-resolution simulation for the solar convection zone. Our calculation reproduces the fast equator and near-surface shear layer (NSSL) of differential rotation and the near-surface poleward meridional flow simultaneously. The NSSL is located in a complex layer where the spatial and time scales of thermal convection are significantly small compared with the deep convection zone. While there have been several attempts to reproduce the NSSL in numerical simulation, the results are still far from reality. In this study, we succeed in reproducing an NSSL in our new calculation. Our analyses lead to a deeper understanding of the construction mechanism of the NSSL, which is summarized as... 1) rotationally unconstrained convection in the near-surface layer transports the angular momentum radially inward; 2) sheared poleward meridional flow around the top boundary is constructed; 3) the shear causes a positive kinetic $\langle v_r v_\theta\rangle $ and negative magnetic $ \langle B_r B_\theta\rangle$ correlations; and 4) the turbulent viscosity and magnetic tension are latitudinally balanced with the Coriolis force in the NSSL. We emphasize the importance of the magnetic field in the solar convection zone.


![[mdfiles/2504.05680.md|2504.05680]]
### AI Justification:
This paper is highly relevant to your research interests as it explores the role of magnetic fields within the solar convection zone and emphasizes the mechanisms that govern magnetic behaviors, such as "the turbulent viscosity and magnetic tension" and their interactions. The findings regarding the poleward meridional flow and the near-surface shear layer also provide insights into how "magnetic fields behave, interact, and amplify" in a highly dynamic plasma environment relevant to your focus on magnetic dynamics across various scales.
# (47/382) http://arxiv.org/pdf/2504.03874v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Galactic-scale Feeding Reveals Warped Hypermagnetized Multiphase Circumbinary Accretion Around Supermassive Black Hole Binaries
**Hai-Yang Wang,Minghao Guo,Elias R. Most,Philip F. Hopkins,Aretaios Lalakos**


#mhd
### Abstract:
Supermassive black hole (SMBH) binaries in gaseous and stellar environments are prime targets for next-generation space-based gravitational wave detectors. Yet, realistic accretion conditions under which these binary systems evolve are not fully understood. In this work, we demonstrate the hypermagnetized multi-phase nature of the surrounding accretion flow formed by large-scale feeding from a galaxy background. Our simulations indicate that the hypermagnetized circumbinary disk is eccentric and warped, hosting a hot gas core for a parsec-scale separated binary. We also observe collimated bipolar magnetic tower-like outflows launched from each SMBH.


![[mdfiles/2504.03874.md|2504.03874]]
### AI Justification:
This paper is relevant to your research interests as it examines the "hypermagnetized multi-phase nature of the surrounding accretion flow," which aligns with your focus on "magnetic field amplification" and the dynamics of plasmas in astrophysical contexts. Furthermore, the mention of "collimated bipolar magnetic tower-like outflows" suggests an exploration of force interactions and emergent behaviors of magnetic fields, directly reflecting your interest in how these phenomena shape structures in the interstellar medium.
# (48/382) http://arxiv.org/pdf/2504.03385v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Observations of the formation of a proto-spot in a pre-existing field environment
**Mariarita Murabito,Ilaria Ermolli,Salvo L. Guglielmino,Paolo Romano,Fabrizio Giorgi**


#mhd
### Abstract:
Bipolar emerging flux regions (EFRs) form active regions (ARs) that generally evolve in a pre-existing magnetic environment in the solar atmosphere. Reconfiguration of the small- and large-scale magnetic connectivities is invoked to explain a plethora of energy release phenomena observed at the sites of EFRs. These include brightening events, surges, and jets, whose trigger and relationship are still unclear. In this context, we study the formation of a proto-spot in AR NOAA~11462 by analyzing spectropolarimetric and spectroscopic measurements taken by the Interferometric Bidimensional Spectrometer along the Fe~I 630.2~nm and Ca~II 854.2~nm lines on April 17, 2012. We complement these high-resolution data with simultaneous SDO satellite observations. The proto-spot forms from magnetic flux emerged into the photosphere that coalesces following plasma flows in its surrounding. The chromospheric and higher atmosphere observations show that flux emergence occurs in a pre-existing magnetic environment, with small- and large-scale coronal arcades that seemingly shape the proto-spot formation in the upper atmospheric layers. In addition, in the chromosphere we observe an arch filament system and repeated intense brightening events and surges, likely due to magnetic interactions of the new flux with the pre-existing overlying coronal field. These phenomena are observed since early stages of the new flux emergence.


![[mdfiles/2504.03385.md|2504.03385]]
### AI Justification:
The paper discusses the interactions of emerging magnetic flux regions within a pre-existing magnetic environment, which aligns closely with your focus on "how magnetic fields behave, interact, and amplify across various scales." The detailed analysis of magnetic dynamics and the observation of energy release phenomena further resonate with your interest in the "complex, multi-scale dynamics of magnetic fields in plasma environments."
# (49/382) http://arxiv.org/pdf/2504.00864v2


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Role of Magnetic Fields in the Formation of High-Mass Star-Forming Cores
**Katerina Sophia Klos,Ian A. Bonnell,Rowan J. Smith**


#mhd
### Abstract:
Magnetic fields are often invoked as playing a primary role in star formation and in the formation of high-mass stars. We investigate the effect of magnetic fields on the formation of high-mass cores using the 3-dimensional smoothed particle magnetohydrodynamics (SPMHD) code PHANTOM. We follow the collapse of six molecular clouds of mass 1000 M $_{\odot}$ , four of which are initially magnetized with mass-to-flux ratios 3, 5, 10 and 100, respectively, and two purely hydrodynamic clouds with varying initial strengths of turbulence. We then apply an in-house clump-finding algorithm to the 3D SPH data in order to quantify the differences in mass and properties of the cores across the degrees of magnetic and turbulent support. We find that although the magnetic fields cause differences in the global cloud evolution, the masses and properties of the cores which form are broadly similar across the different initial conditions. Cores initially form with masses comparable to the initial thermal Jeans mass of the clouds, and then slowly increase in mass with time. We find that regardless of initial magnetization, the fields become dynamically relevant at densities of $\rho > 1\times10^{-17}$ g cm $^{-3}$ - comparable to core densities - and channel material along the field lines, decreasing the stable magnetic Jeans mass, such that the limiting factor for fragmentation is the thermal Jeans mass. We conclude that magnetic fields are not capable of forming and supporting initially high-mass cores against fragmentation.


![[mdfiles/2504.00864.md|2504.00864]]
### AI Justification:
This paper is relevant to your interests in theoretical astrophysics and plasma physics as it investigates “the role of magnetic fields” in “the formation of high-mass star-forming cores,” directly touching upon aspects of “magnetic field amplification” and “force interactions shaping magnetic dynamics,” as you are concerned with how magnetic fields behave in molecular clouds. The use of a 3-dimensional smoothed particle magnetohydrodynamics (SPMHD) code aligns with your interest in theoretical models and simulations, providing valuable insights into the “complex, multi-scale dynamics” of magnetic fields in plasma environments.
# (50/382) http://arxiv.org/pdf/2504.01099v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Filamentary Hierarchies and Superbubbles I... Characterizing filament properties across a simulated spiral galaxy
**Rachel Pillsworth,Erica Roscoe,Ralph E. Pudritz,Eric W. Koch**


#mhd
### Abstract:
High resolution surveys reveal that the interstellar medium in the Milky Way and nearby galaxies consists of interlinked hierarchies of filamentary structure and superbubbles extending from galactic to subpc scales. The characterization of filament properties across this hierarchy is of fundamental importance for the origin of giant molecular clouds and their star clusters. In this paper we characterize the properties of filaments greater than 25 pc in length that are produced in the multi-scale galactic MHD simulations of Zhao et al. 2024. By adapting the FilFinder algorithm of Koch & Rosolowsky, 2015, we extract over 500 filaments ranging up to 10 kpc scales, to derive the probability distribution functions for filament masses and lengths, magnetic field orientations, and the gravitational stability and fragmentation patterns of filaments. We find power-law distributions for filament masses and lengths. The former has a power law index $\alpha_m = 1.85$ that is nearly identical to that of observed GMC mass functions in extragalactic and Galactic surveys, suggesting that GMC properties are inherited from their host filaments. The fragmentation of magnetized filaments on 200 pc scales or less occurs when they exceed an average critical line mass, as predicted by theory. On larger scales however, kpc filaments form out of the cold neutral medium (CNM) and fragmentation follows local variations in the critical line mass along spiral arms or at the boundaries of superbubbles.


![[mdfiles/2504.01099.md|2504.01099]]
### AI Justification:
The paper's focus on "magnetic field orientations, gravitational stability, and fragmentation patterns of filaments" aligns well with your research interests in "how magnetic fields behave, interact, and amplify" within interstellar plasma environments. Additionally, the examination of "multi-scale galactic MHD simulations" resonates with your emphasis on theoretical models and simulations that explore the complex dynamics of magnetic fields across various scales.
# (51/382) http://arxiv.org/pdf/2502.18379v3


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Galactic foreground emissions randomization due to chaotic/turbulent dynamics of magnetized plasma dominated by magnetic helicity
**A. Bershadskii**


#mhd
### Abstract:
Using results of numerical simulations and astrophysical observations (mainly in the WMAP and Planck frequency bands) it is shown that Galactic foreground emission becomes more sensitive to the mean magnetic field with the frequency, that results in the appearance of two levels of its randomization due to chaotic/turbulent dynamics of magnetized interstellar medium dominated by the magnetic helicity. The galactic foreground emission is more randomized at higher frequencies. The Galactic synchrotron and polarized dust emissions have been studied in detail. It is shown that the magnetic field imposes its level of randomization on the synchrotron and dust emission. The background magnetic field and emission have also been briefly discussed in this context. It is shown that they are considerably less randomized than the foreground ones. The main method for the theoretical consideration used in this study is the Kolmogorov-Iroshnikov phenomenology in the frames of distributed chaos notion. Despite the vast differences in the values of physical parameters and spatio-temporal scales between the numerical simulations and the astrophysical observations, there is a quantitative agreement between the results of the astrophysical observations and the numerical simulations in the frames of the distributed chaos notion.


![[mdfiles/2502.18379.md|2502.18379]]
### AI Justification:
The paper's focus on "chaotic/turbulent dynamics of magnetized plasma dominant by magnetic helicity" aligns well with your interest in "emergent magnetic dynamics in turbulent plasmas," particularly as it discusses how randomization of galactic foreground emissions relates to magnetic fields within the interstellar medium. Additionally, the use of "numerical simulations" and "theoretical consideration" through the Kolmogorov-Iroshnikov phenomenology suggests a methodological approach that aligns with your research on theoretical modeling of magnetic field behavior.
# (52/382) http://arxiv.org/pdf/2503.23202v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Using Wavelet Decomposition to Determine the Dimension of Structures from Projected Images
**Svitlana Mayboroda,David N Spergel**


#mhd
### Abstract:
Mesoscale structures can often be described as fractional dimensional across a wide range of scales. We consider a $\gamma$ dimensional measure embedded in an $N$ dimensional space and discuss how to determine its dimension, both in $N$ dimensions and projected into $D$ dimensions. It is a highly non-trivial problem to decode the original geometry from lower dimensional projection of a high-dimensional measure. The projections are space-feeling, the popular box-counting techniques do not apply, and the Fourier methods are contaminated by aliasing effects. In the present paper we demonstrate that under the `Copernican hypothesis that we are not observing objects from a special direction, projection in a wavelet basis is remarkably simple... the wavelet power spectrum of a projected $\gamma$ dimensional measure is $P_j \propto 2^{-j\gamma}$ . This holds regardless of the embedded dimension, $N$ , and the projected dimension, $D$ . This approach could have potentially broad applications in data sciences where a typically sparse matrix encodes lower dimensional information embedded in an extremely high dimensional field and often measured in projection to a low dimensional space. Here, we apply this method to JWST and Chandra observations of the nearby supernova Cas A. We find that the emissions can be represented by projections of mesoscale substructures with fractal dimensions varying from $\gamma = 1.7$ for the warm CO layer observed by JWST, up to $\gamma = 2.5$ for the hot X-ray emitting gas layer in the supernova remnant. The resulting power law indicates that the emission is coming from a fractal dimensional mesoscale structure likely produced by magneto-hydrodynamical instabilities in the expanding supernova shell.


![[mdfiles/2503.23202.md|2503.23202]]
### AI Justification:
This paper presents relevant insights into the behavior of magnetic fields in astrophysical plasmas, specifically regarding the findings of fractal dimensional structures in the context of supernova remnants, which aligns with your interest in "Emergent Magnetic Dynamics in Turbulent Plasmas." Furthermore, the investigation of magneto-hydrodynamical instabilities and their role in the amplification of emissions from these structures directly connects to your focus on "Magnetic Field Amplification,” making it a valuable addition to your research.
# (53/382) http://arxiv.org/pdf/2503.20899v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### High-Performance Computational Magnetohydrodynamics with Python
**Chris Bard,John Dorelli**


#mhd
### Abstract:
We present the AGATE simulation code, a Python-based framework developed primarily for solving the magnetohydrodynamics (MHD) equations while maintaining adaptability to other equation sets. The code employs a modular, object-oriented architecture that separates interface specifications from numerical implementations, allowing users to customize numerical methods and physics models. Built on a Godunov-type finite-volume scheme, AGATE currently supports the ideal, Hall, and Chew-Goldberger-Low (CGL) MHD equations, with multiple acceleration options ranging from Numpy to GPU-enabled computation via NVIDIA CUDA. Performance testing demonstrates that our GPU implementations achieve 40-60x speedups over CPU versions. Comprehensive validation through established benchmarks confirms accurate reproduction of both linear and nonlinear phenomena across different MHD regimes. This combination of modularity, performance, and extensibility makes AGATE suitable for multiple applications... from rapid prototyping to production simulations, and from numerical algorithm development to physics education.


![[mdfiles/2503.20899.md|2503.20899]]
### AI Justification:
This paper presents the AGATE simulation code, which focuses on solving magnetohydrodynamics (MHD) equations, directly aligning with your research interest in "the magnetic dynamics of plasmas" and "the interactions between magnetic forces" within plasma environments. Its comprehensive validation across "different MHD regimes" and the potential for "numerical algorithm development" provide a valuable resource for theoretical models and simulations relevant to your exploration of magnetic field amplification and dynamics.
# (54/382) http://arxiv.org/pdf/2503.19745v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Stellar-wind feedback and magnetic fields around young compact star clusters... 3D MHD simulations
**Lucia Harer,Thibault Vieu,Brian Reville**


#mhd
### Abstract:
Context... The environments of young star clusters are shaped by the interactions of the powerful winds of massive stars, and their feedback on the cluster birth cloud. Several such clusters show diffuse gamma-ray emission on the degree scale, which hints at ongoing particle acceleration. Aims... To date, particle acceleration and transport in star-cluster environments are not well understood. A characterisation of magnetic fields and flow structures is necessary to progress toward physical models. Previous work has largely focused on 100 pc scale feedback or detailed modelling of wind interaction of just a few stars. We aim to bridge this gap. We focus in particular on compact clusters to study collective effects arising from stellar-wind interaction. Objects in this class include Westerlund 1 and R136. Methods... We perform 3D ideal-MHD simulations of compact, young, massive star clusters. Stellar winds are injected kinetically for 46 individual very massive stars (M > 40 Msun), distributed in a spherical region of radius 0.6 - 1 pc. We include a sub-population of five magnetic stars with increased dipole field strengths of 0.1 - 1 kG. We study the evolving superbubble over several 100 kyrs. Results... The bulk flow and magnetic fields show an intricate, non-uniform morphology, which is critically impacted by the relative position of individual stars. The cluster wind terminates in a strong shock, which is non-spherical and, like the flow, has non-uniform properties. The magnetic field is both composed of highly tangled sections and coherent quasi-radial field-line bundles. Steep particle spectra in the TeV domain arise naturally from the variation of magnetic field magnitude over the cluster-wind termination shock. This finding is consistent with gamma-ray observations. The scenario of PeV particle acceleration at the cluster-wind termination shock is deemed unlikely.


![[mdfiles/2503.19745.md|2503.19745]]
### AI Justification:
This paper is relevant to your research interests as it explores the "interactions of the powerful winds of massive stars" and their impact on magnetic fields within the context of "3D ideal-MHD simulations," which aligns well with your focus on theoretical models and simulations of magnetic dynamics in plasma environments. The study's findings on "intricate, non-uniform morphology" of magnetic fields and their interactions with stellar winds relate directly to your interest in "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas."
# (55/382) http://arxiv.org/pdf/2503.17612v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Evolution of Photospheric Magnetic Field and Electric Currents during the X1.6 Flare in Active Region NOAA 12192
**Partha Chowdhury,Belur Ravindra,Sanjiv Kumar Tiwari**


#mhd
### Abstract:
The dynamics of magnetic fields in the Suns active regions plays a key role in triggering solar eruptions. Studies have shown that changes in the photospheres magnetic field can destabilize large-scale structure of the corona, leading to explosive events such as flares and coronal mass ejections (CMEs). This paper delves into the magnetic field evolution associated with a powerful X1.6 class flare that erupted on October 22nd, 2014, from the flare-rich active region NOAA 12192. We utilized high-resolution vector magnetograms from the Helioseismic and Magnetic Imager (HMI) on NASAs Solar Dynamic Observatory (SDO) to track these changes. Our analysis reveals that a brightening, a precursor to the flare, began near the newly emerged, small-scale bipolar flux regions. During the X1.6 flare, the magnetic flux in both polarities displayed emergence and cancellation. The total current within the active region peaked during the flare. But, it is a non CME event and the ratio of direct to return current value remain close to 1. The large flare in this active region occured when the net current in both polarities attain the same sign. This implies that the Lorentz force, a consequence of the interaction between currents and magnetic fields, would have pushed the field lines together in this scenario. This reconnection of opposing magnetic fields is believed to be the driving force behind major flare occurred in this active region.


![[mdfiles/2503.17612.md|2503.17612]]
### AI Justification:
This paper is highly relevant to your interests as it examines the "magnetic dynamics" during a significant solar flare, which aligns with your focus on "magnetic field amplification" and the "force interactions shaping magnetic dynamics" in plasmas. Additionally, the exploration of "reconnection of opposing magnetic fields" offers insights into how turbulence and magnetic field behaviors can manifest in astrophysical environments, paralleling your interest in emergent magnetic dynamics within plasma structures.
# (56/382) http://arxiv.org/pdf/2503.15977v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Hide and seek with a Neutron Star. Hint of Neutron Star activity in SN 2015ap light curve
**Fabio Ragosta,Giulia Illiano,Andrea Simongini,Matteo Imbrogno,Silvia Piranomonte,Andrea Melandri**


#mhd
### Abstract:
Aims. We present a detailed study of the unique SN 2015ap, a very energetic event, notable for its exceptionally high bolometric peak magnitude if compared to other well-know Type Ib supernovae. We analyzed its multi-wavelength light curve, which exhibited a possible period modulation that could result from a geometrical effect. Methods. We analyzed the modulation present at all available bands in SN 2015aps light curves using a Bayesian approach for measuring the period of variability. Additionally, narrow Ha emission is observed in late-time spectra, exhibiting periodic velocity shifts likely originating from hydrogen gas stripped from a companion and accreted onto the compact remnant. Results. We propose that SN 2015aps significant light curve modulation arise from accretion onto a neutron star as the remnant of SN 2015ap. Our multi-wavelength observations reveal a sinusoidal modulation with a period of 8.4 days, confirmed by periodic variations in the Ha emission lines. Traditional models of circumstellar medium interactions cannot account for these features due to the unusually high ejection rates required. Using the Taylor-Spruit dynamo model, we suggest that the interaction between accreting matter and the neutron stars magnetosphere could account for the observed periodic modulation. This implies assuming an ejecta-companion interaction because the accretion from fallback ejecta alone would not produce the observed modulation. The binary configuration, characterized by a separation of less than 50 Ro, supports a magnetized neutron star central engine as the primary mechanism, rather than models involving circumstellar material interaction.


![[mdfiles/2503.15977.md|2503.15977]]
### AI Justification:
This paper provides insights into magnetic dynamics relevant to my research focus by discussing the "interaction between accreting matter and the neutron star's magnetosphere," which aligns with my interest in the "magnetic dynamics of plasmas" and how "magnetic fields behave" in extreme astrophysical conditions. Furthermore, the use of the "Taylor-Spruit dynamo model" suggests a mechanism for magnetic field amplification, resonating with my exploration of how magnetic fields evolve and interact in the context of plasma environments.
# (57/382) http://arxiv.org/pdf/2503.12702v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Unveiling a New $β$ -Scaling of the Tearing Instability in Weakly Collisional Plasmas
**Gabriel L. Ferreira-Santos,Grzegorz Kowal,Diego A. Falceta-Goncalves**


#mhd
### Abstract:
We investigate the linear tearing instability in weakly collisional, gyrotropic plasmas via a non-ideal CGL-MHD framework. Even for an initially isotropic equilibrium, our analysis reveals a striking dependence of the maximum growth rate on plasma- $\beta$ , with $\gamma_{max}\tau_{A}\propto\beta^{-1/4}$ in the high- $\beta$ regime, thereby challenging the $\beta$ -independence predicted by standard MHD theory. We show that this new scaling emerges from the self-consistent fluctuations in pressure anisotropy, which can suppress or enhance the instability depending on the underlying plasma parameters. Systematic scans of the Lundquist number, magnetic Prandtl number, and anisotropy degree $\Delta\beta$ highlight conditions under which the tearing mode departs significantly from classical behavior. Our findings emphasize that weak collisionality and gyrotropic effects must be considered to accurately capture tearing evolution in high- $\beta$ plasma environments.


![[mdfiles/2503.12702.md|2503.12702]]
### AI Justification:
This paper is highly relevant to your research interests, particularly in its exploration of the "tearing instability in weakly collisional plasmas," which pertains to the "magnetic dynamics of plasmas" you study. The findings about how "self-consistent fluctuations in pressure anisotropy" influence "tearing evolution" connect with your focus on force interactions and emergent behaviors in turbulent plasma environments.
# (58/382) http://arxiv.org/pdf/2503.11344v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Complex Magnetic Field of the Extreme Galactic Center... PRIMA Science Potential
**Dylan M. Pare,David T. Chuss,Kaitlyn Karpovich,Natalie Butterfield,Edward J. Wollack,Mark R. Morris,...**


#mhd
### Abstract:
The Central Molecular Zone (CMZ) of the Galactic Center (GC) region of the Milky Way contains a substantial fraction of the molecular mass of the Galaxy >10e7 solar masses yet exhibits an order of magnitude lower star formation efficiency (SFE) than expected given the high densities found in this region. There are multiple possible explanations for the depressed SFE in the CMZ, like feedback, strong turbulence, longer free-fall timescales, and high magnetic field strengths. It is currently unclear which of these mechanisms is the dominant inhibitor of star formation in the CMZ. It is important to understand the star formation process in the extreme environment of the CMZ because it is the only Galactic nuclear region we are able to study at high spatial resolutions with current observatories. One way to determine the relative importance of the different SFE inhibiting mechanisms is through multi-spatial and multi-frequency polarimetric observations of the CMZ. Such observations will provide insight into the behavior of the magnetic field in this unique environment. These observations will complement radio observations of non-thermal structures revealing the magnetic field morphology and polarization. The PRobe far--Infrared Mission for Astrophysics (PRIMA) will be uniquely capable of contributing to such explorations by providing unique resolutions and frequencies for polarimetric observations. The PRIMAger instrument will yield polarimetric observations covering the wavelength range 80 -- 261 um with beam sizes ranging from 11 -- 28, capabilities that complement existing and upcoming observatories.


![[mdfiles/2503.11344.md|2503.11344]]
### AI Justification:
This paper is relevant to my research interests as it directly addresses the behavior of magnetic fields in the Central Molecular Zone (CMZ) and their role in influencing star formation efficiency (SFE), highlighting the "high magnetic field strengths" present in this highly dynamic area. The mention of "multi-spatial and multi-frequency polarimetric observations" aligns with my interest in using theoretical models and observational data to explore "magnetic field amplification" and the interactions within plasma environments.
# (59/382) http://arxiv.org/pdf/2503.10758v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Parallel Collisionless Shocks in strongly Magnetized Electron-Ion Plasma. I. Temperature anisotropies
**Mohamad Shalaby,Antoine Bret,Federico Fraschetti**


#mhd
### Abstract:
Collisionless electron-ion shocks are fundamental to astrophysical plasmas, yet their behavior in strong magnetic fields remains poorly understood. Using Particle-in-Cell (PIC) simulations with the SHARP-1D3V code, we investigate the role of the ion magnetization parameter $\sigma_i$ in parallel shock transitions. Strongly magnetized converging flows ( $\sigma_i > 1$ ) exhibit lower density compression ratios ( $R \sim 2$ ), smaller entropy jumps, and suppressed particle acceleration, while maintaining pressure anisotropy stability due to conserved perpendicular temperatures across the shock, alongside increased parallel temperatures. In contrast, weakly magnetized shocks drive downstream mirror and firehose instabilities due to ion temperature anisotropy, which are suppressed in strongly magnetized cases. Additionally, weakly magnetized shocks exhibit the onset of a supra-thermal population induced by shock-drift acceleration, with most of the upstream kinetic energy thermalized for both electrons and ions in the downstream region. Our results demonstrate that perpendicular temperatures for both species are conserved in strongly magnetized cases and highlight deviations from standard ideal magnetohydrodynamic (MHD) behavior. These findings provide critical insights into the role of magnetic fields in parallel collisionless astrophysical shocks.


![[mdfiles/2503.10758.md|2503.10758]]
### AI Justification:
This paper is relevant to my research interests because it explores "magnetic dynamics" in the context of "collisionless electron-ion shocks" within "strongly magnetized" environments, aligning well with my focus on the behavior and interactions of magnetic fields in astrophysical plasmas. Furthermore, the discussion of how strong magnetic fields influence shock behavior and "pressure anisotropy stability" provides valuable insights into "magnetic field amplification" and "force interactions" that shape magnetic dynamics at various scales, particularly in turbulent plasma settings.
# (60/382) http://arxiv.org/pdf/2503.10795v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A Hierarchical Shock Model of Ultra-High-Energy Cosmic Rays
**Paul Simeon,Noemie Globus,Kirk S. S. Barrow,Roger Blandford**


#mhd
### Abstract:
We propose that a hierarchical shock model $\unicode{x2014}$ including supernova remnant shocks, galactic wind termination shocks, and accretion shocks around cosmic filaments and galaxy clusters $\unicode{x2014}$ can naturally explain the cosmic ray spectrum from ~1 GeV up to ~200 EeV. While this framework applies to the entire cosmic ray spectrum, in this work, we focus on its implications for ultra-high-energy cosmic rays (UHECRs). We perform a hydrodynamic cosmological simulation to investigate the power processed at shocks around clusters and filaments. The downstream flux from nearby shocks around the local filament accounts for the softer, lower-energy extragalactic component around the ankle, and the upstream escaping flux from nearby clusters accounts for the transition to a hard spectral component at the highest energies. This interpretation is in agreement with UHECR observations. We suggest that a combination of early-Universe galactic outflows, cosmic ray streaming instabilities, and a small-scale turbulent dynamo can increase magnetic fields enough to attain the required rigidities. Our simulation suggests that the available volume-averaged power density of accretion shocks exceeds the required UHECR luminosity density by three orders of magnitude. We show that microgauss magnetic fields at these shocks could explain both the origin of UHECRs and the as-yet unidentified source of the diffuse radio synchrotron background below 10 GHz. The shock-accelerated electrons produce a hard radio background without overproducing diffuse inverse Compton emission. These results motivate further observational tests with upcoming facilities to help distinguish accretion shocks from other UHECR sources.


![[mdfiles/2503.10795.md|2503.10795]]
### AI Justification:
This paper is relevant to your research interests in theoretical astrophysics and plasma physics as it discusses "magnetic fields" in the context of "cosmic rays" and proposes mechanisms involving "cosmic ray streaming instabilities" and a "small-scale turbulent dynamo," which aligns with your focus on "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas." The examination of "accretion shocks" and their role in increasing magnetic fields further supports your interest in the interaction of magnetic dynamics within various plasma environments, particularly in "filaments and galaxy clusters."
# (61/382) http://arxiv.org/pdf/2503.05461v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### CHANG-ES XXXIV... Magnetic Field Structure in Edge-On Galaxies Characterising large-scale magnetic fields in galactic halos
**M. Stein,J. Kleimann,B. Adebahr,R. -J. Dettmar,H. Fichtner,J. English,...**


#mhd
### Abstract:
Understanding galactic magnetic fields is essential for interpreting feedback processes in galaxies. Despite their importance, the exact structure of these fields, particularly in galactic halos, remains unclear. Accurate descriptions are crucial for understanding the interaction between star formation and halo magnetisation. By systematically analysing the polarisation patterns in halos of nearby galaxies, we aim to deepen the understanding of the interplay between galactic magnetic fields and star formation processes. We provide an analytical description of the observed X-shaped halos. Based on radio polarimetry data, we classify the polarisation patterns of a sample of edge-on galaxies, by using a newly introduced three-class system... disc dominated, small-scale, and X-shaped. We then fit X-shaped patterns to the polarisation data for galaxies classified as X-shaped and explore links between the polarisation patterns and other physical properties of these galaxies. The classification process shows that 11 out of 18 analysed galaxies display an X-shaped polarisation pattern. Galaxies classified as disc dominated seem less efficient at forming stars than expected for their stellar mass and rotate faster than galaxies with similarly sized HI-discs. X-shape modelling reveals that the polarisation patterns are best fitted by a constant-angle model, and we observe a correlation between the X-shape opening angle and star formation rate surface density indicating the interplay between the star formation in the disc and the magnetisation of the galactic halo. The analysis of polarisation patterns in nearby galaxies reveals that most exhibit an X-shaped configuration, indicating a common magnetic field structure in galactic halos. The introduced models capture the X-shaped morphology and reveal the link between the X-shapes opening angle and star formation rate surface density.


![[mdfiles/2503.05461.md|2503.05461]]
### AI Justification:
The paper explores "the interplay between galactic magnetic fields and star formation processes," which directly aligns with your interest in how "force interactions shape magnetic dynamics." Additionally, the focus on "polarisation patterns" and "the classification of X-shaped halos" reflects your concern with scale-dependent magnetic structuring and offers valuable insights into the organization of magnetic fields in galactic environments.
# (62/382) http://arxiv.org/pdf/2503.05692v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Global dissipative solutions of the 3D Naiver-Stokes and MHD equations
**Alexey Cheskidov,Zirong Zeng,Deng Zhang**


#mhd
### Abstract:
For any divergence free initial data in $H^\frac12$ , we prove the existence of infinitely many dissipative solutions to both the 3D Navier-Stokes and MHD equations, whose energy profiles are continuous and decreasing on $[0,\infty)$ . If the initial data is only $L^2$ , our construction yields infinitely many solutions with continuous energy, but not necessarily decreasing. Our theorem does not hold in the case of zero viscosity as this would violate the weak-strong uniqueness principle due to Lions. This was achieved by designing a convex integration scheme that takes advantage of the dissipative term.


![[mdfiles/2503.05692.md|2503.05692]]
### AI Justification:
This paper discusses the existence of dissipative solutions to the MHD equations, which is directly relevant to my interest in the "magnetic dynamics of plasmas" and particularly aligns with the concept of "magnetic field amplification." The use of a convex integration scheme to address energy profiles in MHD contributes valuable theoretical insights into the behavior of magnetic fields in astrophysical plasmas, making it a potentially useful addition to my research.
# (63/382) http://arxiv.org/pdf/2503.03219v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Impact of Expanding HII Regions on Filament G37...Curved Magnetic Field and Multiple Direction Material Flows
**Mengke Zhao,Xindi Tang,Keping Qiu,Yuxin He,Dalei Li**


#mhd
### Abstract:
Filament G37 exhibits a distinctive `caterpillar` shape, characterized by two semicircular structures within its 40\,pc-long body, providing an ideal target to investigate the formation and evolution of filaments. By analyzing multiple observational data, such as CO spectral line, the H $\alpha$ \,RRL, and multi-wavelength continuum, we find that the expanding H\,{\scriptsize II} regions surrounding filament G37 exert pressure on the structure of the filament body, which kinetic process present as the gas flows in multiple directions along its skeleton. The curved magnetic field structure of filament G37 derived by employing the Velocity Gradient Technique with CO is found to be parallel to the filament body and keeps against the pressure from expanded H\,{\scriptsize II} regions. The multi-directional flows in the filament G37 could cause the accumulation and subsequent collapse of gas, resulting in the formation of massive clumps. The curved structure and star formation observed in filament G37 are likely a result of the filament body being squeezed by the expanding H\,{\scriptsize II} region. This physical process occurs over a timescale of approximately 5\,Myr. The filament G37 provides a potential candidate for end-dominated collapse.


![[mdfiles/2503.03219.md|2503.03219]]
### AI Justification:
This paper is relevant to your interests as it discusses the "curved magnetic field structure" and how expanding HII regions influence the gas flows, which aligns with your focus on "force interactions shaping magnetic dynamics." Additionally, the paper's exploration of the filament G37's magnetic behavior in response to surrounding environments contributes valuable insights into "emergent magnetic dynamics in turbulent plasmas," a key area of your research.
# (64/382) http://arxiv.org/pdf/2503.01963v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Projection-angle effects when `observing` a turbulent magnetized collapsing molecular cloud. I. Chemistry and line transfer
**A. Tritsis,S. Basu,C. Federrath**


#mhd
### Abstract:
Most of our knowledge regarding molecular clouds and the early stages of star formation stems from molecular spectral-line observations. However, the various chemical and radiative-transfer effects, in combination with projection effects, can lead to a distorted view of molecular clouds. Our objective is to simultaneously study all of these effects by creating synthetic spectral-line observations based on a chemo-dynamical simulation of a collapsing molecular cloud. We performed a 3D ideal MHD simulation of a supercritical turbulent collapsing molecular cloud where the dynamical evolution was coupled to a nonequilibrium gas-grain chemical network consisting of 115 species, the evolution of which was governed by >1600 chemical reactions. We post-processed this simulation with a multilevel non-LTE radiative-transfer code to produce synthetic PPV data cubes of the CO, HCO+, HCN, and N2H+ (J = 1-0) transitions under various projection angles with respect to the mean component of the magnetic field. We find that the chemical abundances of various species in our simulated cloud tend to be over-predicted in comparison to observationally derived abundances and attribute this discrepancy to the fact that the cloud collapses rapidly and therefore the various species do not have enough time to deplete onto dust grains. This suggests that our initial conditions may not correspond to the initial conditions of real molecular clouds and cores. We show that the projection angle has a notable effect on the moment maps of the species for which we produced synthetic observations. Specifically, the integrated emission and velocity dispersion of CO, HCO+, and HCN are higher when the cloud is observed `face on` compared to `edge on,` whereas column density maps exhibit an opposite trend. Finally, we show that only N2H+ is an accurate tracer of the column density of the cloud across all projection angles.


![[mdfiles/2503.01963.md|2503.01963]]
### AI Justification:
This paper is relevant to your research interests as it provides a detailed study of a "turbulent magnetized collapsing molecular cloud" through "3D ideal MHD simulation," which aligns with your focus on the magnetic dynamics of plasmas. The emphasis on the interactions between chemical processes and dynamical projections related to magnetic fields offers valuable insights into "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas."
# (65/382) http://arxiv.org/pdf/2503.01409v1


### Rating: 8/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 80%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetar structure in nonlinear electrodynamics with mixed poloidal-toroidal fields
**Arthur G. Suvorov,Jose A. Pons**


#mhd
### Abstract:
Magnetars have inferred polar field strengths in excess of the Schwinger limit, where nonlinear electromagnetic effects can be significant. Their internal fields may be even stronger, suggesting that Maxwellian characterisations of hydromagnetic structure may require revision. A generalised Grad-Shafranov equation, describing static and axisymmetric fluid stars with mixed poloidal-toroidal fields, is introduced and subsequently solved in a perturbative scheme to calculate quadrupolar deformations. In the Born-Infeld theory, we show that the toroidal field has a maximum strength set by the scale parameter, $b$ , implying an upper limit to the stellar prolateness, $|\epsilon_{\rm max}| \sim 10^{-5} \left(b/10^{16}\text{ G}\right)^2$ , that is independent of field specifics. Observations of magnetar phenomena that are interpreted as evidence for ellipticity, such as precession, can thus implicitly constrain post-Maxwellian parameters in a way that complements terrestrial experiments. Toroidal ceilings also have implications for dynamo theory and gravitational waves, which we revisit together with field evolution in crusts abiding by beyond-Maxwell physics.


![[mdfiles/2503.01409.md|2503.01409]]
### AI Justification:
This paper is relevant to your research interests as it discusses "magnetar phenomena" and addresses the need for "revision" of Maxwellian characterizations in the context of strong magnetic fields, which aligns with your focus on "magnetic field amplification" and the "complex, multi-scale dynamics of magnetic fields." Furthermore, it explores "dynamo theory" and "field evolution," areas that resonate with your interest in the interactions between magnetic and gravitational forces in plasma environments.
# (66/382) http://arxiv.org/pdf/2502.04292v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic Reconnection in a Compact Magnetic Dome... Chromospheric Emissions and High-velocity Plasma Flows
**J. M. da Silva Santos,E. Dunnington,R. Jarolim,S. Danilovic,S. Criscuoli**


#mhd
### Abstract:
Magnetic reconnection at small spatial scales is a fundamental driver of energy release and plasma dynamics in the lower solar atmosphere. We present observations of a brightening in an active region, captured in high-resolution data from the Daniel K. Inouye Solar Telescope (DKIST) using the Visible Broadband Imager (VBI) and the Visible Spectro-Polarimeter (ViSP). The event exhibits Ellerman bomb-like morphology in the H $\beta$ filter, associated with flux cancellation between a small negative polarity patch adjacent to opposite-polarity plage. Additionally, it displays enhanced emissions in Ca II K, hot elongated features containing Alfv\enic plasma flows, and cooler blue-shifted structures. We employ multi-line, non-local thermodynamic equilibrium (non-LTE) inversions of the spectropolarimetric data to infer the stratification of the physical parameters of the atmosphere. Furthermore, we use the photospheric vector magnetogram inferred from the ViSP spectra as a boundary condition for nonlinear force-free field extrapolations, revealing the three-dimensional distribution of squashing factors. We find significant enhancements in temperature, velocity, and microturbulence confined to the upper photosphere and low chromosphere. Our findings provide observational evidence of low-altitude magnetic reconnection along quasi-separatrix layers in a compact fan-spine-type configuration, highlighting the complex interplay between magnetic topology, energy release, and plasma flows.


![[mdfiles/2502.04292.md|2502.04292]]
### AI Justification:
This paper is relevant to your research interests as it delves into "magnetic reconnection" and the "complex interplay between magnetic topology" in plasma dynamics, which aligns with your focus on magnetic field behavior and interactions in astrophysical plasmas. Additionally, the examination of "Alfv\enic plasma flows" relates closely to your interest in force interactions shaping magnetic dynamics within various plasma environments.
# (67/382) http://arxiv.org/pdf/2505.00288v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Nyström Type Exponential Integrators for Strongly Magnetized Charged Particle Dynamics
**Tri P. Nguyen,Ilon Joseph,Mayya Tokman**


#mhd
### Abstract:
Calculating the dynamics of charged particles in electromagnetic fields (i.e. the particle pushing problem) is one of the most computationally intensive components of particle-in-cell (PIC) methods for plasma physics simulations. This task is especially challenging when the plasma is strongly magnetized, since in this case the particle motion consists of a wide range of temporal scales from highly oscillatory fast gyromotion to slow macroscopic behavior and the resulting numerical model is very stiff. Current state-of-the-art time integrators used to simulate particle motion have limitations given the severe numerical stiffness of the problem and more efficient methods are of interest. Recently, exponential integrators have been proposed as a promising new approach for these simulations and shown to offer computational advantages over commonly used schemes. Exponential methods can solve linear problems exactly and are $A$ -stable. In this paper, the standard exponential algorithms framework is extended to derive Nystr\`om-type exponential methods that integrate the Newtonian equations of motion as a second-order differential equation. Specific Nystr\`om-type schemes of second and third orders are derived and applied to strongly magnetized particle pushing problems. Numerical experiments are presented to demonstrate that the Nystr\`om-type exponential integrators can provide significant improvement in computational efficiency over the standard exponential methods.


![[mdfiles/2505.00288.md|2505.00288]]
### AI Justification:
The paper is relevant to your interests as it addresses the computational challenges of simulating the dynamics of strongly magnetized plasmas, which aligns with your focus on "magnetic dynamics of plasmas." The emphasis on numerical methods for particle dynamics in electromagnetic fields provides valuable insights that could support your research in examining "how magnetic fields behave, interact, and amplify" under varying conditions, including rapid oscillations and macroscopic behaviors.
# (68/382) http://arxiv.org/pdf/2504.21640v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Compact stellar systems hosting an intermediate mass black hole... magnetohydrodynamic study of inflow-outflow dynamics
**Matus Labaj,Sean M. Ressler,Michal Zajacek,Tomas Plsek,Bart Ripperda,Florian Peissker**


#mhd
### Abstract:
Intermediate-mass black holes (IMBHs) are a missing link in black hole demographics, with only tentative observational evidence to date. Dense stellar clusters such as IRS 13E near the Galactic Center are promising IMBH hosts, where accretion is likely driven by winds from nearby Wolf-Rayet (WR) stars. Yet, the dynamics of such wind-fed systems remain largely unexplored. We investigate how high-velocity stellar winds, magnetic fields, and metallicity-dependent radiative cooling influence gas dynamics and black hole accretion in compact WR clusters. Using three-dimensional (magneto)hydrodynamic simulations, we model each WR star as a source of mass, momentum, energy, and magnetic flux, and include a cooling function that depends on chemical abundance. We compare isotropic versus disk-like stellar distributions to explore the impact of cluster geometry. Across all models, we find that the accretion rate onto the IMBH is suppressed by up to five orders of magnitude relative to the total stellar mass-loss rate. Turbulent, shock-heated outflows driven by wind-wind collisions dominate the flow, expelling most injected gas. While enhanced cooling in high-metallicity runs promotes the formation of dense clumps, these structures are typically unable to reach the black hole. The systems integrated X-ray luminosity is dominated by colliding WR winds, masking the IMBHs radiative signature. Accretion occurs in short-lived, quasi-periodic episodes triggered by close stellar passages, but even these flares remain difficult to detect against the luminous wind background. Our results naturally explain the low detectability of IMBHs in compact WR clusters and provide theoretical predictions to guide future X-ray and infrared observational strategies.


![[mdfiles/2504.21640.md|2504.21640]]
### AI Justification:
The paper presents a magnetohydrodynamic study that focuses on the influence of magnetic fields and stellar winds on gas dynamics in compact clusters, which aligns with my interest in how "magnetic fields behave, interact, and amplify" in astrophysical environments. The use of "three-dimensional (magneto)hydrodynamic simulations" and the examination of "accretion dynamics," especially regarding the role of turbulence and magnetic forces, directly relates to my focus on the "complex, multi-scale dynamics of magnetic fields in plasma environments."
# (69/382) http://arxiv.org/pdf/2504.20627v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Modeling of the time-resolved spectral energy distribution of blazar OJ 287 from 2008 to 2023... a comprehensive multi-epoch study
**G. Harutyunyan,N. Sahakyan,D. Begue**


#mhd
### Abstract:
We present a comprehensive analysis of the time-resolved spectral energy distributions (SEDs) of the blazar OJ 287 over a 15-year period (2008-2023), using multi-wavelength data. In the $\gamma$ -ray band, multiple flaring episodes were observed, with the strongest flare reaching a peak flux of $(5.60\pm1.11)\times10^{-7}\...{\rm photons\...cm^{-2}\...s^{-1}}$ on MJD 55869.03 (04 November 2011). In the optical/UV band, the source was in an active state between MJD 57360 (04 December 2015) and 57960 (26 July 2017), during which the highest flux of $(1.07\pm0.02)\times10^{-10}\...{\rm erg\...cm^{-2}\...s^{-1}}$ was observed on MJD 57681.23 (20 October 2016). In the X-ray band, both the flux and spectral index exhibit variability. To investigate the origin of the broadband emission from OJ 287, we systematically modeled 739 quasi-simultaneous SEDs using a leptonic model that self-consistently accounts for particle injection and cooling. This analysis is possible thanks to the recent development of a surrogate neural-network-based model, trained on kinetic simulations. This innovative, time-resolved, neural network-based approach overcomes the limitations of traditional single-epoch SED modeling, enabling to explore the temporal evolution of key model parameters, such as the magnetic field strength, Doppler factor, and electron injection distribution, across different states of the source. We identified distinct emission states characterized by unique combinations of magnetic field $ B $ , electron index $ p $ , and Doppler boost $ \delta $ , associated to different underlying mechanisms such as varying acceleration processes (e.g., shocks, turbulence) and magnetic confinement. The analysis provides insights into the jet physics processes, including particle acceleration mechanisms and dynamic changes in the jet structure.


![[mdfiles/2504.20627.md|2504.20627]]
### AI Justification:
The paper discusses the temporal evolution of magnetic fields in relation to particle acceleration and dynamics within astrophysical plasmas, responding directly to my interest in "how magnetic fields interact" and "emergent magnetic dynamics in turbulent plasmas." This investigation of magnetic confinement and its connection with turbulence aligns closely with my research focus on the amplification and behavior of magnetic fields across various scales, adding valuable insights into the interaction of these fields with plasma environments.
# (70/382) http://arxiv.org/pdf/2504.20601v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### How to turn a Supernova into a PeVatron
**Robert Brose,Iurii Sushch,Jonathan Mackey**


#mhd
### Abstract:
Context. It is important to determine which Galactic cosmic-ray sources can accelerate particles to the knee of the cosmic ray spectrum at a few PeV, and in particular whether supernova remnants may contribute. Current models for particle acceleration in very young remnants assume the circumstellar material consists of smooth, freely expanding winds. There is strong evidence that some supernovae expand into much denser circumstellar material including dense shells ejected by eruptions shortly before explosion. Aims. We investigate the effects of dense circumstellar shells on particle acceleration in supernova shocks during the first few years post-explosion, to quantify whether such interaction supernovae may act as PeVatrons. Methods. We used the pion code to model the circumstellar medium around Luminous Blue Variables after having a brief episode with a mass-loss rate of up to dM/dt = 2Msol/yr. Consequently, we performed spherically symmetric 1-D simulations using our time-dependent acceleration-code RATPaC in which we simultaneously solve the transport equations for cosmic-rays, magnetic turbulence, and the hydrodynamical flow of the thermal plasma in the test-particle limit. Results. We find that the interaction with the circumstellar shells can significantly boost the maximum energy by enhancing particle escape during the onset of the shock-shell interaction followed by the reacceleration of the shock propagating into a medium with a pre-amplified field. Early interactions boost the maximum energy to a greater degree and interactions within the first 5 months after explosion can increase Emax to more then 1 PeV.


![[mdfiles/2504.20601.md|2504.20601]]
### AI Justification:
The paper has relevance to my research interests as it investigates "magnetic turbulence" and its interaction with "shock-shell interactions," which aligns with my focus on how magnetic fields behave and interact within plasma environments. The use of "spherically symmetric 1-D simulations" to model the amplification of magnetic fields in relation to particle acceleration connects directly with my interest in "theoretical models" and "multi-scale dynamics" of magnetic fields in the interstellar medium.
# (71/382) http://arxiv.org/pdf/2504.15996v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Small-scale dynamic phenomena associated with interacting fan-spine topologies... quiet-Sun Ellerman bombs, UV brightenings, and chromospheric inverted-Y-shaped jets
**Aditi Bhatnagar,Avijeet Prasad,Daniel Nobrega-Siverio,Luc Rouppe van der Voort,Jayant Joshi**


#mhd
### Abstract:
QSEBs are small-scale magnetic reconnection events in lower solar atmosphere. Sometimes, they exhibit transition region counterparts, known as UV brightenings. Magnetic field extrapolations suggest that QSEBs can occur at various locations of a fan-spine topology, with UV brightening occurring at null point through a common reconnection process. We aim to understand how complex magnetic configurations like interacting fan-spine topologies can cause small-scale dynamic phenomena in lower atmosphere. QSEBs were detected using k-means clustering on Hbeta observations from Swedish 1-m Solar Telescope (SST). Further, chromospheric inverted-Y-shaped jets were identified in the Hbeta blue wing. Magnetic field topologies were determined through potential field extrapolations from photospheric magnetograms using the Fe I 6173 A line. UV brightenings were detected in IRIS 1400 A SJI. We identify two distinct magnetic configurations associated with QSEBs, UV brightenings, and chromospheric inverted-Y-shaped jets. The first involves a nested fan-spine structure where, due to flux emergence, an inner 3D null forms inside fan surface of an outer 3D null with some overlap. QSEBs occur at two footpoints along the shared fan surface, with UV brightening located near the outer 3D null point. The jet originates close to the two QSEBs and follows the path of high squashing factor Q. We discuss a comparable scenario using a numerical simulation. In second case, two adjacent fan-spine topologies share fan footpoints at a common positive polarity patch, with the QSEB, along with a chromospheric inverted-Y-shaped jet, occurring at the intersection having high Q values. This study demonstrates through observational and modelling support that associated QSEBs, UV brightenings, and chromospheric inverted-Y-shaped jets share a common origin driven by magnetic reconnection between interacting fan-spine topologies.


![[mdfiles/2504.15996.md|2504.15996]]
### AI Justification:
This paper explores small-scale magnetic reconnection events and their implications for the dynamics of magnetic fields in the lower solar atmosphere, which aligns with your interest in "how magnetic fields behave, interact, and amplify". The focus on "magnetic configurations like interacting fan-spine topologies" and the examination of dynamics occurring through reconstruction processes can provide insights into the mechanisms driving the amplification and evolution of magnetic fields in astrophysical plasmas.
# (72/382) http://arxiv.org/pdf/2504.19896v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Tracing the ejecta structure of SN 1987A... Insights and diagnostics from 3D MHD simulations
**S. Orlando,M. Miceli,M. Ono,S. Nagataki,M. -A. Aloy,F. Bocchino,...**


#mhd
### Abstract:
Supernova (SN) 1987A provides a unique window into the aftermath of a massive stellar explosion, offering key insights into the ejectas morphology, composition, explosion mechanism, progenitor system, and circumstellar medium (CSM) interaction. We investigate large-scale ejecta asymmetries in SN 1987A. By comparing the simulations with JWST observations and making predictions for XRISM, we aim to refine our understanding of the explosion mechanism and the remnants evolution. We performed 3D MHD simulations that trace the evolution of SN 1987A from the SN to the SNR, extending our predictions up to 5000 years into the future and considering the Ni-bubble effects. The simulation results are compared with JWST observations and used to predict XRISM spectra, to evaluate the accuracy of the modeled ejecta structure. Our simulations reproduce the large-scale Fe-rich ejecta morphology seen by JWST, revealing two clumps suggestive of a bipolar explosion. Ni-bubble effects in the first year boost Fe-rich ejecta expansion and their interaction with the reverse shock. However, discrepancies with JWST observations in clump velocities and spatial distribution suggest stronger explosion asymmetries than modeled. Since 2021, our models predict that shocked ejecta have contributed increasingly to X-ray emission, now rivaling shocked CSM and soon dominating as the latter fades. Future XRISM observations will trace the evolution of these ejecta structures, refining constraints on explosion geometry. Early remnant asymmetries from CSM interaction may persist for at least 100 years. Our results underscore the role of asymmetric core-collapse mechanisms in shaping SN 1987As ejecta and constraining its explosion geometry. Future studies should explore more extreme asymmetries, in neutrino-driven core collapse or magneto-rotational SN models, to identify the origin of its bipolar Fe-rich structure.


![[mdfiles/2504.19896.md|2504.19896]]
### AI Justification:
This paper is relevant to your interests as it utilizes 3D MHD simulations to investigate the magnetic dynamics associated with the ejecta structure of SN 1987A, aligning with your focus on "magnetic dynamics of plasmas" and "emergent magnetic dynamics in turbulent plasmas." Additionally, the findings contribute to understanding how "asymmetric core-collapse mechanisms" influence the behavior of magnetic fields at various scales, potentially offering insights into the amplification and interaction of magnetic fields in astrophysical contexts.
# (73/382) http://arxiv.org/pdf/2504.18987v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Propagation of UHE cosmic rays in the light of f(R) gravity power-law model
**Swaraj Pratim Sarmah**


#mhd
### Abstract:
While the origins of ultra-high energy (UHE) cosmic rays (CRs) remain shrouded in uncertainty, several important milestones have been reached in recent years in the experimental study of CRs with energy above 1018 eV. Within the vast expanse of intergalactic space, turbulent magnetic fields (TMFs) are believed to pervade, and these fields could exert a significant influence on the journey of UHECRs across the expanding Universe, which is currently undergoing acceleration. Thus, it is imperative to incorporate these considerations into our theoretical framework to gain a deeper understanding of the empirical observations related to UHECRs. In light of this, our research delves into the impact of UHE particle diffusion in the presence of TMFs, all within the context of the f(R) gravity power-law model. Based on this f(R) model, we explore the diffusive behavior of UHECR protons, particularly focusing on their density enhancement throughout their propagation and their energy spectrum. We found that the f(R) gravity model considered here plays an effective role in the propagation of CRs and the results have lain within our range of interest. Also, we compare our results for flux with observational data like the Pierre Auger Observatory (PAO) and Telescope Array (TA).


![[mdfiles/2504.18987.md|2504.18987]]
### AI Justification:
This paper examines the influence of turbulent magnetic fields (TMFs) on the diffusion of ultra-high energy cosmic rays (UHECRs), which aligns with my research interest in “magnetic dynamics of plasmas in the interstellar medium.” The focus on how TMFs affect the propagation and density enhancement of UHECRs could provide insights into “emergent magnetic dynamics in turbulent plasmas,” thereby enriching my understanding of complex magnetic interactions in astrophysical environments.
# (74/382) http://arxiv.org/pdf/2504.18761v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Rotation and Dispersion Measure Evolution of Repeating Fast Radio Bursts Propagating through a Magnetar Flare Ejecta
**Di Xiao**


#mhd
### Abstract:
Rotation measure (RM) and dispersion measure (DM) are characteristic properties of fast radio bursts (FRBs) that contain important information of their source environment. The time evolution of RM and DM is more inclined to be ascribed to local plasma in the host galaxy rather than the intergalactic medium or free electrons in the Milky Way. Recently a sudden drastic RM change was reported for an active repeating FRB 20220529, implying that some kind of mass ejection happened near the source. In this work I suggest that magnetar flare ejecta could play this role and give rise to the significant RM change. I introduce a toy structured ejecta model and calculate the contribution to RM and DM by a typical flare event. I find that this model could reproduce the RM behaviour of FRB 20220529 well under reasonable parameters, and similar sudden change is expected as long as this source maintains its activity.


![[mdfiles/2504.18761.md|2504.18761]]
### AI Justification:
The paper discusses the "rotation measure (RM)" and "dispersion measure (DM)" in the context of fast radio bursts (FRBs), which relate to the "magnetic dynamics of plasmas" that are of particular interest in astrophysics. Furthermore, the investigation of "magnetar flare ejecta" in shaping RM demonstrates an exploration of how "force interactions" and localized plasma conditions affect magnetic fields, which aligns with your focus on the behavior and interaction of magnetic fields within plasma environments.
# (75/382) http://arxiv.org/pdf/2504.18859v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quasilinear interaction between Langmuir and Weibel turbulence in a beam-plasma system
**A. A. Kuznetsov,Vl. V. Kocharovsky**


#mhd
### Abstract:
To analyze the joint development of two-stream and filamentation kinetic instabilities in a plasma with a particle beam, a quasilinear approach has been developed that accounts for the integral nonlinear interaction of modes arising from the variation of the spatially averaged velocity distribution function of the particles. On this basis, a numerical study has been carried out within the initial two-dimensional problem for a range of characteristic parameters of the plasma and the beam, focusing on the evolution of Langmuir (two-stream) and Weibel (filamentation) turbulence spectra. It has been established that the evolving Weibel-type magnetic turbulence can significantly reshape the region of the velocity distribution that is resonant with Langmuir waves, thereby strongly influencing the formation and particularly the damping of Langmuir turbulence. In turn, the Langmuir-type quasi-electrostatic turbulence can lead to substantial isotropization of the particle velocity distribution, thus altering the growth rates, evolution, and saturation levels of the Weibel turbulence modes.


![[mdfiles/2504.18859.md|2504.18859]]
### AI Justification:
The paper is relevant to your interests as it investigates the "Weibel (filamentation) turbulence" and its interaction with Langmuir turbulence in a plasma setting, which aligns with your focus on "force interactions shaping magnetic dynamics" and how these effects influence the development of magnetic fields in various plasma environments. Additionally, the discussion on the "evolving Weibel-type magnetic turbulence" offers valuable insights into "emergent magnetic dynamics in turbulent plasmas," particularly regarding how magnetic fields interact with turbulence to shape their properties.
# (76/382) http://arxiv.org/pdf/2504.03199v4


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Spin evolution modeling for a newly-formed white dwarf resulting from binary white dwarf merger
**Yanchang Cheng,Jumpei Takata**


#mhd
### Abstract:
Merger of two white dwarfs (WDs) has been proposed to form an isolated WD having high magnetization and rapid rotation. We study the influence of the magnetohydrodynamic (MHD) wind on spin evolution of the newly-formed merger product. We consider the scenario that the merger product appears as a giant-star-like object with a radius of $> 10^{10}$ cm and a luminosity of the order of an Eddington value. We solve a structure of the merger product under the hydrostatic equilibrium and identify the position of the slow-point in the hot envelope. It is found that if such a giant-star-like object is spinning with an angular speed of the order of the Keplerian value, the MHD wind can be produced. The mass-loss rate is estimated to be of the order of $\sim 10^{20-21}~\mathrm{g~s^{-1}} $ , and the timescale of the spin down is $ \sim 10\text{-}10^{3}$ years, which depends on stellar magnetic field. We discuss that the final angular momentum when the MHD wind is terminated is related to the magnetic flux and initial radiation luminosity of the merger product. We apply our model to three specific magnetic WD sources ZTF J190132.9+145808.7, SDSS J221141.8+113604.4, and PG 1031+234 by assuming that those WDs were as a result of the merger product. We argue that the current periods of ZTF J190132.9+145808.7 and PG 1031+234 that are strongly magnetized WDs are related to the initial luminosity at the giant phase. For SDSS J221141.8+113604.4, which is mildly magnetized WD, its angular momentum was almost determined when the spin-down timescale due to MHD wind is comparable to the cooling timescale in the giant phase.


![[mdfiles/2504.03199.md|2504.03199]]
### AI Justification:
The paper explores the spin evolution and magnetization of newly-formed white dwarfs from binary mergers, which relates to my interest in "magnetic field amplification" and how magnetic dynamics evolve in astrophysical contexts. The investigation of MHD winds and their impact on angular momentum and magnetic fields also connects to my focus on "force interactions shaping magnetic dynamics," underscoring the significance of magnetic fields in stellar environments.
# (77/382) http://arxiv.org/pdf/2504.12745v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### 3D MHD wave propagation and energy transport in a simulated solar vortex
**Samuel Skirvin,Viktor Fedun,Gary Verth,Istvan Ballai**


#mhd
### Abstract:
Magnetic flux tubes in the presence of background rotational flows are abundant throughout the solar atmosphere and may act as conduits for MHD waves to transport energy throughout the solar atmosphere. Here we investigate the contribution from MHD waves to the Poynting flux in a 3D numerical simulation of a realistic solar atmosphere, modelling a structure resembling a solar vortex tube, using the PLUTO code in the presence of different plasma flow configurations. These simulations feature a closed magnetic loop system where a rotational flow is imposed at one foot-point in addition to photospheric perturbations acting as a wave driver mimicking those of p-modes. We find that a variety of MHD waves exist within the vortex tube, including sausage, kink and torsional Alfv\{e}n waves, owing to the photospheric wave driver and the nature of the rotational flow itself. We demonstrate how the visual interpretation of different MHD modes becomes non-trivial when a background rotational flow is present compared to a static flux tube. By conducting a simulation both with and without the rotational plasma flow, we demonstrate how the perturbed Poynting flux increases in the presence of the rotational flow as the waves transport increased magnetic energy. We attribute this increase to the dynamical pressure from the rotational flow increasing the plasma density at the tube boundary, which acts to trap the wave energy more effectively inside the vortex. Moreover, we demonstrate how the Poynting flux is always directed upwards in weakly twisted magnetic flux tubes.


![[mdfiles/2504.12745.md|2504.12745]]
### AI Justification:
This paper is relevant to your research focus as it explores "MHD wave propagation" and the "transport of energy" within a simulated solar vortex, which can provide insights into "magnetic field amplification" mechanisms and the influence of "rotational flows" on magnetic dynamics. The focus on the interaction between "MHD waves" and "rotational flow" aligns with your interest in how various forces shape the structure and behavior of magnetic fields in plasma environments.
# (78/382) http://arxiv.org/pdf/2504.15802v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Cosmic ray neutrons in magnetized astrophysical structures
**Ellis R. Owen,Yoshiyuki Inoue,Tatsuki Fujiwara,Qin Han,Kinwah Wu**


#mhd
### Abstract:
Cosmic rays are often modeled as charged particles. This allows their non-ballistic propagation in magnetized structures to be captured. In certain situations, a neutral cosmic ray component can arise. For example, cosmic ray neutrons are produced in considerable numbers through hadronic pp and p $\gamma$ interactions. At ultrahigh energies, the decay timescales of these neutrons is dilated, allowing them to traverse distances on the scale of galactic and cosmological structures. Unlike charged cosmic rays, neutrons are not deflected by magnetic fields. They propagate ballistically at the speed of light in straight lines. The presence of a neutral baryonic cosmic ray component formed in galaxies, clusters and cosmological filaments can facilitate the escape and leakage of cosmic rays from magnetic structures that would otherwise confine them. We show that, by allowing confinement breaking, the formation of cosmic-ray neutrons by high-energy hadronic interactions in large scale astrophysical structures can modify the exchange of ultra high-energy particles across magnetic interfaces between galaxies, clusters, cosmological filaments and voids.


![[mdfiles/2504.15802.md|2504.15802]]
### AI Justification:
The paper's focus on cosmic ray neutrons and their behavior in magnetized structures aligns with your research interests in "magnetic dynamics of plasmas in the interstellar medium," specifically relating to how "magnetic fields behave and interact" across different scales. Additionally, the exploration of how cosmic-ray neutrons facilitate the "escape and leakage of cosmic rays from magnetic structures" connects to your interest in "force interactions shaping magnetic dynamics," highlighting the complex interplay between various forces in astrophysical contexts.
# (79/382) http://arxiv.org/pdf/2504.16177v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Turbulent heating in collisionless low-beta plasmas... imbalance, Landau damping, and electron-ion energy partition
**T. Adkins,R. Meyrand,J. Squire**


#mhd
### Abstract:
An understanding of how turbulent energy is partitioned between ions and electrons in weakly collisional plasmas is crucial for modelling many astrophysical systems. Using theory and simulations of a four-dimensional reduced model of low-beta gyrokinetics (the `Kinetic Reduced Electron Heating Model), we investigate the dependence of collisionless heating processes on plasma beta and imbalance (normalised cross-helicity). These parameters are important because they control the helicity barrier, the formation of which divides the parameter space into two distinct regimes with remarkably different properties. In the first, at lower beta and/or imbalance, the absence of a helicity barrier allows the cascade of injected power to proceed to small (perpendicular) scales, but its slow cascade rate makes it susceptible to significant electron Landau damping, in some cases leading to a marked steepening of the magnetic spectra on scales above the ion Larmor radius. In the second, at higher beta and/or imbalance, the helicity barrier halts the cascade, confining electron Landau damping to scales above the steep `transition-range spectral break, resulting in dominant ion heating. We formulate quantitative models of these processes that compare well to simulations in each regime, and combine them with results of previous studies to construct a simple formula for the electron-ion heating ratio as a function of beta and imbalance. This model predicts a `winner takes all picture of low-beta plasma heating, where a small change in the fluctuations properties at large scales (the imbalance) can cause a sudden switch between electron and ion heating.


![[mdfiles/2504.16177.md|2504.16177]]
### AI Justification:
This paper is relevant to your research interests as it investigates "the dependence of collisionless heating processes on plasma beta and imbalance," which could relate to the "interactions between magnetic, gravitational, and thermal forces" in plasma environments that you are studying. Additionally, the exploration of heating dynamics and the resulting effects on magnetic spectra provides critical insights into "emergent magnetic dynamics in turbulent plasmas," which aligns well with your focus on how these dynamics evolve across various scales.
# (80/382) http://arxiv.org/pdf/2504.14000v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Modeling transport in weakly collisional plasmas using thermodynamic forcing
**Prakriti Pal Choudhury,Archie F. A. Bott**


#mhd
### Abstract:
How momentum, energy, and magnetic fields are transported in the presence of macroscopic gradients is a fundamental question in plasma physics. Answering this question is especially challenging for weakly collisional, magnetized plasmas, where macroscopic gradients influence the plasmas microphysical structure. In this paper, we introduce thermodynamic forcing, a new method for systematically modeling how macroscopic gradients in magnetized or unmagnetized plasmas shape the distribution functions of constituent particles. In this method, we propose to apply an anomalous force to those particles inducing the anisotropy that would naturally emerge due to macroscopic gradients in weakly collisional plasmas. We implement thermodynamic forcing in particle-in-cell (TF-PIC) simulations using a modified Vay particle pusher and validate it against analytic solutions of the equations of motion. We then carry out a series of simulations of electron-proton plasmas with periodic boundary conditions using TF-PIC. First, we confirm that the properties of two electron-scale kinetic instabilities -- one driven by a temperature gradient and the other by pressure anisotropy -- are consistent with previous results. Then, we demonstrate that in the presence of multiple macroscopic gradients, the saturated state can differ significantly from current expectations. This work enables, for the first time, systematic and self-consistent transport modeling in weakly collisional plasmas, with broad applications in astrophysics, laser-plasma physics, and inertial confinement fusion.


![[mdfiles/2504.14000.md|2504.14000]]
### AI Justification:
This paper is relevant to my research interests in theoretical astrophysics and plasma physics, particularly through its focus on "how momentum, energy, and magnetic fields are transported in the presence of macroscopic gradients." The introduction of "thermodynamic forcing" and the systematic modeling of interactions in weakly collisional, magnetized plasmas aligns with my focus on the "interactions between magnetic, gravitational, and thermal forces" that shape the behavior of magnetic fields in plasma environments.
# (81/382) http://arxiv.org/pdf/2504.13384v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Formation of Magnetic Switchbacks via expanding Alfvén Waves
**Trevor A. Bowen,Alfred Mallet,Corina I. Dunn,Jonathan Squire,Benjamin D. G. Chandran,Romain Meyrand,...**


#mhd
### Abstract:
Context. Large-amplitude inversions of the solar winds interplanetary magnetic field have long been documented; however, observations from the Parker Solar Probe (PSP) mission have renewed interest in this phenomenon as such features, often termed switchbacks, may constrain both the sources of the solar wind as well as in-situ nonlinear dynamics and turbulent heating. Aims. We aim to show that magnetic field fluctuations in the solar wind are consistent with Alfv\enic fluctuations that naturally form switchback inversions in the magnetic field through expansion effects. Methods. We examine PSP observations of the evolution of a single stream of solar wind in a radial scan from PSPs tenth perihelion encounter from approximately 15-50 solar radii. We study the growth and radial scaling of normalized fluctuation amplitudes in the magnetic field, $\delta B/B$ , within the framework of spherical polarization. We compare heating rates computed via outer-scale decay from consideration of wave-action to proton heating rates empirically observed through considering adiabatic expansion. Results. We find that the magnetic field fluctuations are largely spherically polarized and that the normalized amplitudes of the magnetic field, $\delta B/B$ , increases with amplitude. The growth of the magnetic field amplitude leads to switchback inversions in the magnetic field. While the amplitudes do not grow as fast as predicted by the conservation of wave action, the deviation from the expected scaling yields an effective heating rate, which is close to the empirically observed proton heating rate. Conclusions. The observed scaling of fluctuation amplitudes is largely consistent with a picture of expanding Alfv\en waves that seed turbulence leading to dissipation. The expansion of the waves leads to the growth of wave-amplitudes, resulting in the formation of switchbacks.


![[mdfiles/2504.13384.md|2504.13384]]
### AI Justification:
The paper is relevant to your research interests as it explores "the growth and radial scaling of normalized fluctuation amplitudes in the magnetic field" within a framework that connects to "turbulence" and "nonlinear dynamics," directly correlating with your focus on how "magnetic fields behave, interact, and amplify across various scales." Furthermore, the examination of "switchbacks" and their formation through "Alfv\enic fluctuations" provides insight into mechanisms of magnetic field amplification that can enrich your understanding of dynamics in astrophysical plasma environments.
# (82/382) http://arxiv.org/pdf/2504.14111v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Impact of Azimuthal Magnetic Field Inhomogeneity on Hall Thruster high-frequency azimuthal instability via 2D radial-azimuthal PIC simulations
**Zhijun Zhou,Xin Luo,Yinjian Zhao,Daren Yu**


#mhd
### Abstract:
For the SPT-type Hall thrusters, the magnetic structure with magnetic conductive columns leads inherent to azimuthally inhomogeneous magnetic configurations. This azimuthal magnetic inhomogeneity may impact electron azimuthal closed-drift motion and cross-field transport characteristics. This study systematically investigates the effects of azimuthal magnetic field gradient on high frequency azimuthal instability and associated anomalous electron transport through 2D radial-azimuthal Particle-in-Cell (PIC) simulations. The results reveal dual mechanisms of magnetic inhomogeneity on electron cyclotron drift instability (ECDI) characteristics... (1) The azimuthal drift velocity distribution becomes modulated by the magnetic field inhomogeneity, with increased average drift velocity enhancing ECDI intensity under stronger inhomogeneity; (2) Simultaneously, the ECDI wavenumber spectrum broadens with elevated magnetic inhomogeneity, reducing discrete ECDI spectral peaks. Under the dual influence of magnetic field inhomogeneity, when the inhomogeneity level is below 5%, the ECDI saturation amplitude and electron cross field mobility remains largely unchanged. However, a notable reduction of 13.4% in ECDI saturation intensity and a 15.7% decrease in electron mobility are observed when magnetic field inhomogeneity reaches 10%.


![[mdfiles/2504.14111.md|2504.14111]]
### AI Justification:
The paper's focus on "azimuthal magnetic field inhomogeneity" and its effects on "electron azimuthal closed-drift motion" aligns with my interest in the "interactions between magnetic, gravitational, and thermal forces" that shape magnetic dynamics. Furthermore, the examination of high-frequency azimuthal instability provides insights that could relate to "emergent magnetic dynamics in turbulent plasmas," making it potentially valuable for understanding complex behaviors in astrophysical contexts.
# (83/382) http://arxiv.org/pdf/2504.13009v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Sequential ejections of plasma blobs due to unbraiding of tangled loops in the solar atmosphere
**Xiuhui Zuo,Zhenghua Huang,Hengyuan Wei,Chao Zhang,Boyu Sun,Youqian Qi,...**


#mhd
### Abstract:
Nanoflares, which are consequences of braids in tangled magnetic fields, are an important candidate to heat the solar corona to million degrees. However, their observational evidence is sparse and many of their observational characteristics are yet to be discovered. With the high-resolution observations taken by the Extreme Ultraviolet Imager onboard the Solar Orbiter, here we study a series of ejections of plasma blobs resulted from a braided magnetic loops in the upper transition region and reveal some critical characteristics of such processes. The cores of these ejections have a size of about 700\,km, a duration less than 1 minute and a speed of about 90\,\kms. An important characteristic is that these plasma blobs are apparently constrained by the post-reconnection magnetic loops, along which they show an extension of up to about 2\,000\,km. The propagation of unbraiding nodes along the main axis of the tangled loops has a speed of about 45\,\kms. The separation angles between the post-reconnection loops and the main axis of the tangled loops are about 30\degree. The observations from the Atmospheric Imaging Assembly reveal that the braiding loops are upper transition region structures. Based on these observations, the typical magnetic free energy producing a blob is estimated to be about $3.4\times10^{23}$ \,erg, well in the nano-flare regime, while the kinematic energy of a blob is about $2.3\times10^{23}$ \,erg, suggesting that a majority of magnetic free energy in a magnetic braid is likely transferred into kinematic energy.


![[mdfiles/2504.13009.md|2504.13009]]
### AI Justification:
This paper discusses the interaction of magnetic fields with plasma in the solar atmosphere, particularly through "braided magnetic loops," which aligns with my interest in "magnetic dynamics of plasmas" and mechanisms for "magnetic field amplification." The observations of how "plasma blobs" are constrained by post-reconnection magnetic loops provide insights into "force interactions shaping magnetic dynamics," which is central to my research focus on the behavior of magnetic fields across different scales.
# (84/382) http://arxiv.org/pdf/2504.11886v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Detection of wave activity within a realistic 3D MHD quiet sun simulation
**George Cherry,Boris Gudiksen,Adam J. Finley**


#mhd
### Abstract:
Context. Tracing wave activity from the photosphere to the corona has important implications for coronal heating and prediction of the solar wind. Despite extensive theory and simulations, the detection of waves in realistic MHD simulations still presents a large challenge due to wave interaction, mode conversion, and damping mechanisms. Aims. We conducted this study to detect localised wave activity within a realistic MHD simulation of the solar atmosphere by the Bifrost code. Methods. We present a new method of detecting the most significant contributions of wave activity within localised areas of the domain, aided by Discrete Fourier Transforms and frequency filtering. We correlate oscillations in the vertical & horizontal magnetic field, velocities parallel & perpendicular to the magnetic field, and pressure to infer the nature of the dominant wave modes. Results. Our method captures the most powerful frequencies and wavenumbers, as well as providing a new diagnostic for damping processes. We infer the presence of magnetoacoustic waves in the boundaries of prominent chromospheric/coronal swirling features. We find these waves are likely damped by viscous heating in the swirl boundaries, contributing to heating in the upper atmosphere. Conclusions. Using the most significant frequencies decomposition, we highlight that energy can be transported from the lower atmosphere to the upper atmosphere through waves and fluctuations along the swirl boundaries. Although further analysis is needed to confirm these findings, our new method provides a path forward to investigate wave activity in the solar atmosphere


![[mdfiles/2504.11886.md|2504.11886]]
### AI Justification:
The paper's focus on "detecting wave activity within a realistic 3D MHD simulation" is relevant to my interest in "magnetic dynamics of plasmas" as it addresses wave interaction and the implications for magnetic field behavior in the solar atmosphere. The mention of "correlating oscillations in the vertical & horizontal magnetic field" aligns with my research on how magnetic fields interact across scales, particularly how these wave phenomena can influence the dynamics within plasma environments.
# (85/382) http://arxiv.org/pdf/2504.11414v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A magnetar powers the luminous supernova 2023pel, associated with a long gamma-ray burst
**L. M. Roman Aguilar,M. M. Saez,K. Ertini,M. C. Bersten**


#mhd
### Abstract:
We explore SN 2023pel, the most recent event associated with gamma-ray bursts (GRBs), specifically GRB 230812B. SN 2023pel has a high luminosity and low expansion velocities compared to other GRB-SNe. These properties seem difficult to reconcile with a single nickel power source. We searched for models that can explain the properties of this event. We calculated a grid of hydrodynamic models based on pre-SN structures derived from evolutionary calculations. We compared our models with observations of SN~2023pel and selected our preferred model using statistical analysis, taking both light curves and expansion velocities into account. This allowed us to derive a set of physical properties for SN~2023pel. Our models suggest that the most probable scenario involves a millisecond magnetar as the primary power source, supplemented by energy from radioactive decay. Our preferred model has a spin period of P = 3.2 ms, a magnetic field of B = 28 x 10^14 G, an explosion energy of 2.3 foe, a nickel mass of M_Ni= 0.24 solar masses, and an ejected mass of 3.4 solar masses. Alternatively, we find that a purely nickel-powered model also provides a good match with the observations, though M_Ni > 0.8 solar masses are always required. However, the combination of such high values of M_Ni and low M_ej is difficult to reconcile, indicating that this scenario is less probable. We have also identified a specific region within the peak luminosity-velocity plane where an additional energy source beyond nickel may be necessary to power SNe with characteristics similar to SN~2023pel. Our study indicates that an additional energy source beyond radioactive decay is essential to explain the high brightness and relatively low expansion velocities of SN 2023pel. A magnetar-powered model, similar to the models proposed for the very luminous GRB-SN 2011kl, aligns well with these characteristics.


![[mdfiles/2504.11414.md|2504.11414]]
### AI Justification:
This paper is relevant to your research interests as it discusses the role of a millisecond magnetar, with a high magnetic field, as the primary energy source in shaping the dynamics of supernova SN 2023pel, indicating that magnetic fields play a crucial role in astrophysical phenomena, aligning with your focus on "magnetic dynamics of plasmas" and "magnetic field amplification." The exploration of how magnetic fields influence the energy output and characteristics of supernovae provides valuable insight into the interactions between "magnetic" and "gravitational forces," which is crucial for your studies in plasma physics within the interstellar medium.
# (86/382) http://arxiv.org/pdf/2504.11265v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Evidence of Nonlinear Signatures in Solar Wind Proton Density at the L1 Lagrange point
**Dario Javier Zamora,Facundo Abaca,Bruno Zossi,Ana Georgina Elias**


#mhd
### Abstract:
The solar wind is a medium characterized by strong turbulence and significant field fluctuations on various scales. Recent observations have revealed that magnetic turbulence exhibits a self-similar behavior. Similarly, high-resolution measurements of the proton density have shown comparable characteristics, prompting several studies into the multifractal properties of these density fluctuations. In this work, we show that low-resolution observations of the solar wind proton density over time, recorded by various spacecraft at Lagrange point L1, also exhibit non-linear and multifractal structures. The novelty of our study lies in the fact that this is the first systematic analysis of solar wind proton density using low-resolution (hourly) data collected by multiple spacecraft at the L1 Lagrange point over a span of 17 years. Furthermore, we interpret our results within the framework of non-extensive statistical mechanics, which appears to be consistent with the observed nonlinear behavior. Based on the data, we successfully validate the q-triplet predicted by non-extensive statistical theory. To the best of our knowledge, this represents the most rigorous and systematic validation to date of the q-triplet in the solar wind.


![[mdfiles/2504.11265.md|2504.11265]]
### AI Justification:
This paper is relevant to your research interests as it examines "strong turbulence" within the solar wind, tying into your focus on how magnetic fields behave and interact under complex plasma conditions. Moreover, by uncovering "non-linear and multifractal structures" in the proton density, it provides insights into the "interactions between magnetic, gravitational, and thermal forces," which is a key theme in your study of magnetic dynamics across various scales.
# (87/382) http://arxiv.org/pdf/2504.11432v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Analysis of Preheat Propagation in MagLIF-like Plasmas
**Fernando Garcia-Rubio,Scott Davidson,C. Leland Ellison,Nathan B. Meezan,Douglas S. Miller,Nantas Nardelli,...**


#mhd
### Abstract:
The preheat and pre-magnetization of the fuel are essential steps in the design of Magnetized Liner Inertial Fusion (MagLIF) configurations. Typically, the energy of the preheat laser is deposited in a central region of the fuel and propagates outward generating magneto-hydrodynamic structures that impact the fuel mass distribution and magnetic flux compression during the subsequent implosion. We present a theoretical analysis of preheat propagation in a magnetized plasma under conditions typical for MagLIF. The analysis is based on the acoustic time scale for the propagation of pressure disturbances being much shorter than the conductive time scale for heat diffusion. In this regime, the preheat-driven expansion induces the stratification of fuel mass and magnetic field, which accumulate in a dense outer shelf bounded by the leading shock. We derive self-similar solutions of the mathematical model that describe the hydrodynamic profiles of the expansion, and evaluate the evolution of the magnetic field in this configuration. The model is supported by FLASH simulations of preheat propagation. Our analysis shows that the regions where the magnetization of the fuel is significant tend to become localized asymptotically in time at the interface separating the outer shelf from the inner hot core. We assess the implications of this stratification on the magnetic flux conservation and performance of fully integrated MagLIF FLASH simulations.


![[mdfiles/2504.11432.md|2504.11432]]
### AI Justification:
This paper is relevant to your research focus as it investigates "magneto-hydrodynamic structures" and the "evolution of the magnetic field" in a plasma configuration, aligning with your interest in magnetic field amplification and dynamics. Additionally, the use of FLASH simulations to model "self-similar solutions" and "stratification of fuel mass and magnetic field" could provide insights into complex, emergent magnetic behaviors in astrophysical plasmas.
# (88/382) http://arxiv.org/pdf/2504.10382v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Why Cold BGK Modes Are So Cool... Dispersion Relations from Orbit-Constrained Distribution Functions
**Mikael Tacu**


#mhd
### Abstract:
We derive analytic dispersion relations for cold, orbitally constrained systems governed by the Vlasov equation. For magnetized plasmas, we obtain the first explicit relation for two-dimensional anisotropic BGK modes with finite magnetic field, showing that only a finite number of angular modes can become unstable and identifying a magnetic-field threshold for stabilization. In the gravitational case, we establish a bound on the growth rate of core perturbations, set by the potentials curvature. These results clarify how orbital constraints shape the spectrum and growth of kinetic instabilities in cold, collisionless media.


![[mdfiles/2504.10382.md|2504.10382]]
### AI Justification:
This paper is relevant to your research interests as it discusses "analytic dispersion relations for cold, orbitally constrained systems" in magnetized plasmas, aligning with your focus on the "interaction between magnetic, gravitational, and thermal forces." Additionally, the findings on "kinetic instabilities" and their dependence on magnetic fields provide insights into how magnetic dynamics behave and may amplify within plasma environments, which is integral to your exploration of magnetic field amplification and force interactions.
# (89/382) http://arxiv.org/pdf/2504.10599v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Dust continuum radiation maps from MHD simulations of accretion-ejection systems around single and binary stars
**Somayeh Sheikhnezami,Christian Fendt,Sareh Ataiee**


#mhd
### Abstract:
We study the launching of magnetized jets from a resistive circumstellar disk within a binary system, employing a unique combination of 3D MHD jet launching simulations (PLUTO code) and post-processed 3D radiative transfer modeling (RADMC-3D code). Our findings reveal a well-defined jet originating from the inner region of the disk, extending to a larger disk area. While the model attains steady states for a single star, a binary system leads to the emergence of tidal effects such as the formation of ``spiral arms in the disk and inside the jet. Here we have consistently implemented a time-dependent Roche potential for the gravity of the binary. As a major step forward, we further present the first 3D radiation maps of the dust continuum for the disk-jet structure. In principle, this allows us to compare MHD simulation results to observed disk-outflow features. We, therefore, present convolved images of the dust continuum emission, employing exemplary point spread functions of the MIRI instrument (5~ $\mu m$ band) and the ALMA array (320~ $\mu m$ band). In these bands, we identify distinguishable features of the disk-jet structure, such as `spiral arms,` which we have also seen in the MHD dynamics.For gas density increased by an order of magnitude, the disk become optically thick at 5~ $\mu m $ , but remains bright at 320~ $ \mu $ m. At this wavelength, 320~ $ \mu$ m, enhanced structural features in the disk and the base of the wind become more pronounced and are well resolved in the convolved image.


![[mdfiles/2504.10599.md|2504.10599]]
### AI Justification:
The paper presents a study on the magnetic dynamics of jets launched from magnetized disks in binary star systems, which is relevant to my focus on **magnetic field amplification and the interactions between magnetic, gravitational, and thermal forces**. The use of **3D MHD simulations** aligns well with my interest in theoretical models exploring how magnetic fields evolve and interact across different astrophysical scales.
# (90/382) http://arxiv.org/pdf/2504.10154v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The energy content of Alfven waves in the stratified solar atmosphere
**Roberto Soler**


#mhd
### Abstract:
Alfven waves propagating in a vertically stratified plasma, such as those travelling from the solar photosphere to the corona, are partially reflected due to the gradient in the Alfven speed. Wave reflection naturally results in the superposition of upward- and downward-propagating waves. A simple analytic model demonstrates that this superposition leads to the non-equipartition of kinetic and magnetic energies in the Alfven wave perturbations and slows down the net energy transport. A numerical model of Alfven wave propagation in the lower solar atmosphere reveals significant wave reflection below the transition region, leading to highly variable kinetic and magnetic energy content in the lower chromosphere. At higher altitudes, the kinetic energy eventually dominates, depending on the wave frequency. The velocity at which net energy propagates upward is significantly smaller than the local Alfven speed throughout the chromosphere. Consequently, the commonly used expression for unidirectional Alfven waves in a uniform plasma, which relates the energy flux to the kinetic energy density, is not generally applicable in the stratified lower solar atmosphere and cannot be reliably used to estimate the energy content of observed waves. A generalized expression is given, incorporating correction factors that account for wave reflection and energy non-equipartition. The applicability of the expression is discussed.


![[mdfiles/2504.10154.md|2504.10154]]
### AI Justification:
The paper discusses "Alfven waves" and their behavior in stratified plasma, which aligns with my research interest in "magnetic dynamics of plasmas" and "how magnetic fields behave." The focus on wave reflection and energy transport in the context of a stratified environment can provide insights into "magnetic field amplification" mechanisms relevant to astrophysical plasmas.
# (91/382) http://arxiv.org/pdf/2504.09701v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Modeling Local Bubble analogs II... Synthetic Faraday rotation maps
**Efrem Maconi,Stefan Reissl,Juan D. Soler,Philipp Girichidis,Ralf S. Klessen,Andrea Bracco,...**


#mhd
### Abstract:
Faraday rotation describes the change of the linear polarization angle of radiation passing through a magnetized plasma and it is quantified by the rotation measure (RM), which is related to the line-of-sight (LOS) magnetic field component and the thermal electron density traversed by light along its path toward the observer. However, it is challenging to disentangle the signal from different LOS portions and separate the contribution from the local ISM. This is particularly relevant since the Sun is located within the Local Bubble (LB), a low-density and hot cavity formed by past SN events, making it essential to investigate how this environment may influence the observed RM values. The present study investigates the imprint of the local environment on the synthetic RM signal, as measured by an observer within a LB-like cavity. The RM derived from diffuse polarized synchrotron radiation produced by CR electrons at decimeter wavelengths is also analyzed. We produce synthetic RM maps for an observer placed inside a LB candidate, selected from a MHD simulation that resembles the properties of the ISM in the Solar vicinity. Using the capabilities of the radiative transfer code POLARIS, we study the imprint of the cavity walls on the RM signal. As the MHD simulation does not account for CR diffusion, we develop a CR toy-model to study the Faraday rotation of the diffuse polarized synchrotron radiation. We find that (i) the imprint of local structures, such as the walls of the LB candidate and the edges of other supernovae blown cavities, is of fundamental importance for interpreting the global Faraday sky; (ii) the LB has a non negligible contribution to the sinusoidal patterns of RM as a function of Galactic longitude seen in observations; and (iii) the RM signal from diffuse synchrotron emission shows a strong correspondence with the RM signal generated by the LB candidate walls.


![[mdfiles/2504.09701.md|2504.09701]]
### AI Justification:
This paper is relevant to my research interests in that it investigates the "imprint of local structures" on the Faraday rotation signal in a "Local Bubble," which pertains to the broader dynamics of magnetic fields in the interstellar medium. The study employs MHD simulations and explores how the magnetic field interacts with "local ISM" conditions, aligning well with my focus on the interactions between magnetic dynamics and their plasma environments across various astrophysical scales.
# (92/382) http://arxiv.org/pdf/2504.08521v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Sunward Flows in the Magnetosheath Associated with Magnetic Pressure Gradient and Magnetosheath Expansion
**H. Madanian,Y. Pfau-Kempf,R. Rice,T. Liu,T. Karlsson,S. Raptis,...**


#mhd
### Abstract:
A density structure within the magnetic cloud of an interplanetary coronal mass ejection impacted Earth and caused significant perturbations in plasma boundaries. We describe the effects of this structure on the magnetosheath plasma downstream of the bow shock using spacecraft observations. During this event, the bow shock breathing motion is evident due to the changes in the upstream dynamic pressure. A magnetic enhancement forms in the inner magnetosheath and ahead of a plasma compression region. The structure has the characteristics of a fast magnetosonic shock wave, propagating earthward and perpendicular to the background magnetic field further accelerating the already heated magnetosheath plasma. Following these events, a sunward motion of the magnetosheath plasma is observed. Ion distributions show that both the high density core population as well as the high energy tail of the distribution have a sunward directed flow indicating that the sunward flows are caused by magnetic field line expansion in the very low $\beta$ magnetosheath plasma. Rarefaction effects and enhancement of the magnetic pressure in the magnetosheath result in magnetic pressure gradient forcing that drives the expansion of magnetosheath magnetic field lines. This picture is supported by a reasonable agreement between the estimated plasma accelerations and the magnetic pressure gradient force.


![[mdfiles/2504.08521.md|2504.08521]]
### AI Justification:
This paper is relevant to your interests as it discusses "magnetic pressure gradient forcing" and "magnetic field line expansion," which relate directly to your focus on "magnetic field amplification" and "force interactions shaping magnetic dynamics." The abstract examines the interaction of magnetic fields in a plasma environment, specifically in the magnetosheath, and provides insights into how these dynamics shape the behavior of magnetic fields, aligning with your interest in emergent magnetic dynamics within astrophysical plasmas.
# (93/382) http://arxiv.org/pdf/2504.08447v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Tayler instability as possible reason for the period changes in Ap star 56 Ari
**I. S. Potravnov,L. L. Kitchatinov**


#mhd
### Abstract:
The physical mechanism responsible for the photometric period changes in chemically peculiar star 56 Ari was searched. It was previously shown that rate of the stars period increase is few orders of magnitude larger than the rates expected from the evolutionary changes of the angular momentum or due to magnetic braking. Also no secular changes were detected in the surface structure or visibility of chemical spots which are responsible for the rotational modulation of stellar brightness. We hypothesise that period changes in 56 Ari are caused by the drift of surface magnetic and associated abundance structures as a result of the kink-type (Tayler) instability of the background magnetic field in the radiative zone of the star. Results of the numerical simulation presented in the paper yield growth and drift rates of the most rapidly developing non-axisymmetric mode of the instability, consistent with the observed rate of period changes in 56 Ari. The surface geometry of the 56 Ari magnetic field is also reproduces in the calculations. The proposed mechanism may also be used to explain the character of period changes in other Ap/Bp stars demonstrating such an effect.


![[mdfiles/2504.08447.md|2504.08447]]
### AI Justification:
The paper discusses the Tayler instability of magnetic fields, which directly relates to my interest in "Magnetic Field Amplification" and "Force Interactions Shaping Magnetic Dynamics" within plasma environments. Furthermore, the focus on the magnetic dynamics in stellar environments and their implications on period changes provides insights into how magnetic fields behave and interact across astrophysical scales, which is relevant to my research on the interstellar medium.
# (94/382) http://arxiv.org/pdf/2504.06234v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Observing radio transients with Phased ALMA... Pulses from the Galactic Centre magnetar
**J. Vera-Casanova,M. Cruces,K. Liu,J. Wongphechauxsorn,C. A. Braga,M. Kramer,...**


#mhd
### Abstract:
Radio transients, such as pulsars and Fast Radio Bursts (FRBs), are primarily detected at centimetre radio wavelengths, where higher luminosities are found. However, observations of sources in dense environments are heavily affected by propagation effects which may hinder a detection. Millimetre wave observations bypass this complication but require the largest radio telescopes to compensate for the lower flux densities. When used in phased mode, the ALMA radio telescope provides an equivalent dish size of 84m, being the most sensitive instrument at mm/sub mm. With its high time resolution it offers a unique opportunity to study radio transients in an unexplored window. We study the Galactic Centre (GC) magnetar, PSR J1745 $-$ 2900, as a laboratory for magnetars in complex magneto-turbulent environments and to link with FRBs. We showcase the potential of ALMA in phased mode to observe radio transients and to achieve, for some sources, the first ever detections outside the cm wave range. We studied the GC magnetar using ALMA archival data of Sgr A* at Band 3 from the 2017 GMVA campaign. We searched in intensity and classified the pulses based on their circular and linear polarisation properties and arrival phase. We detected eight pulses with energies in the range of 10 $^{29}$ erg. We constructed its cumulative energy distribution and we fit a power law, where the event rate scales with energy as $R \propto E^{\gamma}$ . The result is an exponent of $\gamma = -2.4 \pm 0.1$ . With the $\gamma -$ value and the system properties of phased ALMA, we estimate that over 160 known pulsars could be detected by ALMA. For repeating FRBs, observing during their peak activity window could lead to several detections. We expect that ALMAs lower frequency bands with polarisation capabilities, will serve as a pioneer on mm wave searches for pulsars and to study complex environments involving radio transients.


![[mdfiles/2504.06234.md|2504.06234]]
### AI Justification:
This paper presents a study of the Galactic Centre magnetar and positions it within "complex magneto-turbulent environments,” aligning well with your interest in how “magnetic fields behave, interact, and amplify.” The use of ALMA to observe radio transients provides an innovative approach to exploring “emergent magnetic dynamics” in turbulent plasma environments and ensures relevance to your focus on the multi-scale dynamics of magnetic fields in astrophysical settings.
# (95/382) http://arxiv.org/pdf/2504.07223v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic Webs in Stellar Radiative Zones
**Valentin A. Skoutnev,Andrei M. Beloborodov**


#mhd
### Abstract:
Rotational evolution of stellar radiative zones is an old puzzle. We argue that angular momentum (AM) transport by turbulent processes induced by differential rotation is insufficient, and propose that a key role is played by ``magnetic webs.` We define magnetic webs as stable magnetic configurations that enforce corotation of their coupled mass shells. Stable magnetic configurations naturally form through relaxation of helical magnetic fields deposited in parts of radiative zones. We discuss the conditions for a magnetic configuration to be sufficiently sturdy to prevent the build up of differential rotation, and conclude that these conditions are easily met in stellar interiors. Low mass stars on the red giant branch (RGB) likely have their compact cores coupled to the lower part of their extended radiative mantle by a magnetic web that was deposited by the receding zone of core convection on the main sequence. This results in moderate core rotation that is broadly consistent with asteroseismic observations, as we illustrate with a stellar evolution model with mass $1.6M_\odot$ . Evolving massive stars host more complicated patterns of convective zones that may leave behind many webs, transporting AM towards the surface. Efficient web formation likely results in most massive stars dying with magnetized and slowly rotating cores.


![[mdfiles/2504.07223.md|2504.07223]]
### AI Justification:
This paper is relevant to your research interests, as it discusses the stability of "magnetic configurations" and their role in angular momentum transport, which aligns with your focus on "magnetic dynamics" and the "interactions between magnetic, gravitational, and thermal forces." Additionally, the exploration of how "stable magnetic configurations" emerge in stellar interiors resonates with your interest in "emergent magnetic dynamics in turbulent plasmas," especially in the context of astrophysical scales.
# (96/382) http://arxiv.org/pdf/2504.07311v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Scenarios for magnetic X-point collapse in 2D incompressible dissipationless Hall magnetohydrodynamics
**Alain J. Brizard**


#mhd
### Abstract:
The equations of 2D incompressible dissipationless Hall magnetohydrodynamics (HMHD), which couple the fluid velocity ${\bf V} = \wh{\sf z}\btimes\nabla\phi + V_{z}\,\wh{\sf z} $ with the magnetic field $ {\bf B} = \nabla\psi\btimes\wh{\sf z} + B_{z}\,\wh{\sf z}$ , are known to support solutions that exhibit finite-time singularities associated with magnetic X-point collapse in the plane $(B_{x} = \partial\psi/\partial y, B_{y} = -\,\partial\psi/\partial x)$ . Here, by adopting a 2D self-similar model for the four HMHD fields $(\phi,\psi,V_{z},B_{z})$ , which retains finite electron inertia, we obtain five coupled ordinary differential equations that are solved in terms of the Jacobi elliptic functions based on an orbital classification associated with particle motion in a quartic potential. Excellent agreement is found when these analytical solutions are compared with numerical solutions, including the precise time of a magnetic X-point collapse.


![[mdfiles/2504.07311.md|2504.07311]]
### AI Justification:
The paper discusses the behavior of magnetic fields in the context of 2D incompressible Hall magnetohydrodynamics, which aligns with my focus on "magnetic dynamics of plasmas in the interstellar medium." The exploration of "finite-time singularities" and "magnetic X-point collapse" contributes valuable insights into "scale-dependent magnetic structuring" and the interactions between magnetic and fluid dynamics, making it relevant for my research on magnetic field amplification and emergent behaviors in turbulent environments.
# (97/382) http://arxiv.org/pdf/2504.05600v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A universal natal spin in stellar-mass black holes
**Shu-Xu Yi,Tian-Yong Cao,Shuang-Nan Zhang**


#mhd
### Abstract:
A stellar mass black hole (BH) is believed to be formed as the result of the core collapse of a massive star at the end of its evolution. For a class of Gamma-Ray Bursts (GRBs), it is widely believed that their centre engines are just these stellar-mass BHs, which accrete the collapsing matter in hyper-accretion mode. In such systems, a popular scenario is that the magnetic field supported in the accretion disk extracts the rotational energy of the spinning BH and launch a jet on one hand, and the accretion of the infalling matter of the collapse will increase the BHs rotational energy on the other hand. However, the detailed physical processes of the above scenario are still not well understood. Here we report that when the accretion process is dominated by a Magnetically-Arrested-Disk (MAD), the above mentioned two competing processes link to each other, so that the spin evolution of the BH can be written in a simple form. Most interestingly, when the total accreted mass is enough, the BH spin will always reach to an equilibrium value peaked at $\chi\sim0.88$ . This value does not depend on the initial mass and spin of the BH, as well as the history of accretion. This model predicts that there is a population of stellar-mass BH which possess a universal spin at the end of the collapsing accretion. We test this prediction against the 3rd gravitational wave (GW) catalogue (GWTC-3) and found that the distribution of the spin of the secondary BH is centred narrowly around $0.85\pm 0.05$ as predicted. Applying this model to the parameters of observed parameters in GWTC-3 and further GW catalogues, it is possible to infer the initial mass and spin distributions of the binary BHs detected with GW.


![[mdfiles/2504.05600.md|2504.05600]]
### AI Justification:
The paper presents a model of how magnetic fields influence black hole (BH) spin dynamics, particularly in Magnetically-Arrested-Disk (MAD) scenarios, which aligns with my interest in "magnetic dynamics of plasmas" as it explores the interaction between magnetic forces and gravitational dynamics during black hole formation. Additionally, the findings regarding the "universal spin" of stellar-mass black holes could provide insights into the broader implications of magnetic field structuring in stellar environments, enhancing our understanding of "scale-dependent magnetic structuring" in astrophysical plasmas.
# (98/382) http://arxiv.org/pdf/2503.24077v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Dust in the wind of outbursting young stars
**Kundan Kadam,Eduard Vorobyov,Peter Woitke,Manuel Gudel**


#mhd
### Abstract:
Context. Young Stellar Objects (YSOs) are observed to undergo powerful accretion events known as FU Orionis outbursts (FUors). Such events of episodic accretion are now considered to be common during low mass star formation, wherein the accretion onto the protostar occurs through a surrounding centrifugal disk. Increasing evidence suggests that the magnetic disk winds are crucial for driving disk accretion, as they carry both mass and momentum away from the disk. Aims. We aim to investigate the phenomenon of the ejection of magnetic disk winds during episodic accretion, with a focus on the dust contained within these winds. Methods. We conduct magnetohydrodynamic (MHD) simulations of formation and evolution of protoplanetary disk (PPD) in the thin-disk limit. We include evolution of dust with two populations and a realistic prescription for viscosity during outbursts, which depends on the local thermal ionization fraction. The disk evolves with the concurrent action of viscosity, self-gravity and magnetic disk winds. Results. The simulated disk displays outbursting behavior in the early stages, with the duration and frequency of the bursts, their rise times, and brightness amplitudes resembling the observations of FUors. We find that during the outbursts, the winds are over an order of magnitude more dusty, as compared to in quiescence. However, despite this increased dust content, the winds are still dust-depleted as the dust-to-gas ratio is about an order of magnitude lower than the canonical interstellar value of 0.01. The results of our numerical experiments are in general agreement with the available observational findings and they shed a light on the mechanism behind production of dusty winds during outbursting events in YSOs.


![[mdfiles/2503.24077.md|2503.24077]]
### AI Justification:
This paper is relevant to your interests as it investigates the role of magnetic disk winds in the context of young stellar objects and their accretion processes, aligning with your focus on the "magnetic dynamics of plasmas in the interstellar medium." Furthermore, the use of magnetohydrodynamic (MHD) simulations to study "the evolution of dust" within a "magnetic disk" directly relates to your interest in theoretical models and simulations of magnetic field interactions in plasma environments.
# (99/382) http://arxiv.org/pdf/2504.05396v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quiet Sun Ellerman bombs as a possible proxy for reconnection-driven spicules
**Mats Ola Sand,Luc H. M. Rouppe van der Voort,Jayant Joshi,Souvik Bose,Daniel Nobrega-Siverio,Ana Belen Grinon-Marin**


#mhd
### Abstract:
Spicules are elongated, jet-like structures that populate the solar chromosphere and are rooted in the photosphere. In recent years, high-resolution observations and advanced numerical simulations have provided insights into their properties, structures, and dynamics. However, the formation mechanism of spicules, particularly the more dynamic type II spicules, which are primarily found in the quiet Sun and coronal holes, remains elusive. This study explores whether quiet Sun Ellerman bombs (QSEBs), which are ubiquitous small-scale magnetic reconnection events in the lower atmosphere, are linked to the formation of type II spicules. We analysed a high-quality 40-minute time sequence acquired with the Swedish 1-m Solar Telescope. H-beta data were used to observe QSEBs and spicules, while spectropolarimetric measurements in the photospheric Fe i 6173 A line provided line-of-sight magnetic field information. We employed k-means clustering to automatically detect QSEBs and explored their potential association with spicules. We identified 80 clear cases where spicules occurred soon after the QSEB and not later than 30 s after the ending of the QSEBs. All events involved type II spicules, rapidly fading from the images. The footpoints of the spicules seemed to be rooted in QSEBs, where the onset of QSEBs often preceded the formation of the associated spicules. Additionally, we found around 500 other events that hinted at a connection but with some ambiguities. The combined clear and ambiguous cases constitute 34% of the total detected QSEBs and a smaller percentage of the spicules in our dataset. Our findings suggest that a fraction of type II spicules originate from QSEBs, supporting magnetic reconnection as a potential driving mechanism. In this context, QSEBs and spicules represent the conversion of magnetic energy into thermal and kinetic energy, respectively.


![[mdfiles/2504.05396.md|2504.05396]]
### AI Justification:
The paper is relevant to your interests as it investigates the link between small-scale magnetic reconnection events (Ellerman bombs) and the formation of spicules, which directly pertains to your focus on "magnetic dynamics of plasmas" and "force interactions shaping magnetic dynamics." Furthermore, the study's exploration of how QSEBs might drive spicule formation through magnetic reconnection aligns with your interest in "magnetic field amplification" and the influence of magnetic fields in plasma structures.
# (100/382) http://arxiv.org/pdf/2504.05502v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Non-Maxwellianity of Ion Velocity Distributions in the Earths Magnetosheath
**Louis Richard,Sergio Servidio,Ida Svenningsson,Anton V. Artemyev,Kristopher G. Klein,Emiliya Yordanova,...**


#mhd
### Abstract:
We analyze the ion velocity distribution function (iVDF) deviations from local thermodynamic equilibrium (LTE) in collisionless plasma turbulence. Using data from the Magnetospheric Multiscale (MMS) mission, we examine the non-Maxwellianity of 441,577 iVDFs in the Earths magnetosheath. We find that the iVDFs anisotropy is overall limited, while high-order non-LTE features can be significant. Our results show that the complexity of the iVDFs is strongly influenced by the ion plasma beta and the turbulence intensity, with high-order non-LTE features emerging with large-amplitude magnetic field fluctuations. Furthermore, our analysis indicates that turbulence-driven magnetic curvature contributes to the isotropization of the iVDFs by scattering the ions, emphasizing the complex interaction between turbulence and the velocity distribution of charged particles in collisionless plasmas.


![[mdfiles/2504.05502.md|2504.05502]]
### AI Justification:
This paper is relevant to your research interests as it explores the "complex interaction between turbulence and the velocity distribution of charged particles in collisionless plasmas," aligning with your focus on "emergent magnetic dynamics in turbulent plasmas." Furthermore, the examination of the "non-Maxwellianity of ion velocity distributions" and the relationship to "magnetic field fluctuations" provides insights into how turbulence may shape the dynamics and structure of magnetic fields within plasma environments, reflecting your interest in the broader implications of these interactions.
# (101/382) http://arxiv.org/pdf/2504.04282v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Semi-Lagrangian methods of a plasma hybrid model with multi-species kinetic ions and massless electrons
**Yingzhe Li,Philip J. Morrison,Stefan Possanner,Eric Sonnendrucker**


#mhd
### Abstract:
The semi-Lagrangian methods with the improved number of one-dimensional advections are proposed for a plasma hybrid model with kinetic ions and mass-less electrons. Two subsystems with mass, momentum, and energy conservation are obtained by a Poisson bracket-based splitting method. For the subsystem in which the distribution functions and the fields are coupled, the second order and reversible modified implicit mid-point rule is used in time with the specially designed mean velocity. The distribution functions are not involved in the iterations and are solved by exact splittings with only one dimensional advections, which makes the proposed schemes efficient. The cancellation problem is overcome by the numerical schemes constructed. Moreover, for the case with a periodic boundary condition, the magnetic field obtained is divergence free, mass, momentum, and energy are conserved. The methods can be extended to cases with multiple ion species.


![[mdfiles/2504.04282.md|2504.04282]]
### AI Justification:
This paper is relevant to your interests because it explores "semi-Lagrangian methods" in the context of a "plasma hybrid model," which could provide insights into "magnetic field amplification" through its focus on magnetic dynamics within plasma environments. Additionally, the attention to conservation of mass, momentum, and energy suggests a relevance to understanding the "force interactions shaping magnetic dynamics" that you are investigating in various plasma scales.
# (102/382) http://arxiv.org/pdf/2504.03919v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetized ICF implosions... ignition at low laser energy using designs with more ablator mass remaining
**C. A. Walsh,S. T. O'Neill,D. J. Strozzi,L. S. Leal,R. Spiers,A. J. Crilly,...**


#mhd
### Abstract:
This paper is the first work to redesign a spherical ICF implosion to best utilize the benefits of applying an external magnetic field. The sub-ignition experiment N170601 is taken as the baseline design, which used 1.57MJ of laser energy. The optimum magnetized design benefits from increasing the shell thickness by 14 $\mu$ m and decreasing the ice thickness by 18 $\mu$ m, resulting in a neutron yield of 8.9 $\times$ 10 $^{17}$ . This is 34 $\times$ greater than the unmagnetized simulation of the same design, and 18.5 $\times$ the greatest unmagnetized simulation across all designs simulated. The resultant implosion velocity for the magnetized design is lower, which would also reduce ablation front instability growth. This design was found by using a simplified 1D magnetization model, then validated against full 2D extended-MHD capsule simulations with radiation asymmetries applied to correct the shape.


![[mdfiles/2504.03919.md|2504.03919]]
### AI Justification:
This paper demonstrates significant insights into "magnetic field amplification" through its exploration of a "magnetized ICF implosion," which aligns with my interest in the evolution of magnetic fields in plasma environments. The study's focus on how modifying design parameters can influence "magnetization" and neutron yield offers a practical example of "force interactions shaping magnetic dynamics," which is critical to my research on magnetic structures across various scales.
# (103/382) http://arxiv.org/pdf/2504.02185v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Multiwavelength observation of a candidate pulsar halo LHAASO J0621+3755 and the first X-ray detection of PSR J0622+3749
**C. B. Adams,A. Archer,P. Bangale,J. T. Bartkoske,W. Benbow,J. H. Buckley,...**


#mhd
### Abstract:
Pulsar halos are regions around middle-aged pulsars extending out to tens of parsecs. The large extent of the halos and well-defined central cosmic-ray accelerators make this new class of Galactic sources an ideal laboratory for studying cosmic-ray transport. LHAASO J0621+3755 is a candidate pulsar halo associated with the middle-aged gamma-ray pulsar PSR J0622+3749. We observed LHAASO J0621+3755 with VERITAS and XMM-Newton in the TeV and X-ray bands, respectively. For this work, we developed a novel background estimation technique for imaging atmospheric Cherenkov telescope observations of such extended sources. No halo emission was detected with VERITAS (0.3--10 TeV) or XMM-Newton (2--7 keV) within 1 degree and 10 arcmin around PSR J0622+3749, respectively. Combined with the LHAASO-KM2A and Fermi-LAT data, VERITAS flux upper limits establish a spectral break at ~1--10 TeV, a unique feature compared with Geminga, the most studied pulsar halo. We model the gamma-ray spectrum and LHAASO-KM2A surface brightness as inverse Compton emission and find suppressed diffusion around the pulsar, similar to Geminga. A smaller diffusion suppression zone and harder electron injection spectrum than Geminga are necessary to reproduce the spectral cutoff. A magnetic field <= 1 uG is required by our XMM-Newton observation and synchrotron spectral modeling, consistent with Geminga. Our findings support slower diffusion and lower magnetic field around pulsar halos than the Galactic averages, hinting at magnetohydrodynamic turbulence around pulsars. Additionally, we report the detection of an X-ray point source spatially coincident with PSR J0622+3749, whose periodicity is consistent with the gamma-ray spin period of 333.2 ms. The soft spectrum of this source suggests a thermal origin.


![[mdfiles/2504.02185.md|2504.02185]]
### AI Justification:
This paper discusses "magnetohydrodynamic turbulence around pulsars," aligning well with my research interest in how "magnetic fields behave, interact, and amplify across various scales" in plasma environments. The focus on "suppressed diffusion" and required magnetic fields adds value to my exploration of "magnetic field amplification and the interactions shaping magnetic dynamics" within the interstellar medium.
# (104/382) http://arxiv.org/pdf/2504.02729v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Vortex Flows in the Solar Atmosphere... Detection and Heating Mechanisms in 3D MHD Numerical Simulations
**M. Koll Pistarini,E. Khomenko,T. Felipe**


#mhd
### Abstract:
Vortex flows are structures associated with the rotation of the plasma and/or the magnetic field that are present throughout the solar atmosphere. In recent years, their study has become increasingly important, as they are present on a wide variety of temporal and spatial scales and can connect several layers of the solar atmosphere. In this work, we focused on the detection and analysis of these structures in an automatic way. We use realistic 3D MHD numerical simulations obtained with the Mancha3D code at different magnetic field configurations and spatial resolutions. The vortex detection has been performed using the novel SWIRL code. We have been able to determine multiple structures associated with small and large scale vortices that extend in height in our simulations. We performed a statistical analysis of these structures, quantifying their number and typical sizes, as well as their temperature and heating profiles, confirming their importance in the energy transport.


![[mdfiles/2504.02729.md|2504.02729]]
### AI Justification:
This paper is relevant to your research interests because it investigates the "vortex flows" and their relationship with the "magnetic field" in the solar atmosphere, which aligns with your focus on "magnetic dynamics of plasmas." Furthermore, the use of "3D MHD numerical simulations" to analyze these structures supports your interest in theoretical models that explore how interactions between magnetic fields and plasma behaviors emerge at various scales.
# (105/382) http://arxiv.org/pdf/2504.00680v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Twisted magnetar magnetospheres... a class of semi-analytical force-free non-rotating solutions
**Guillaume Voisin**


#mhd
### Abstract:
Magnetospheric twists, that is magnetospheres with a toroidal component, are under scrutiny due to the key role the twist is believed to play in the behaviour of neutron stars. Notably, its dissipation is believed to power magnetar activity, and is an important element of the evolution of these stars. We exhibit a new class of twisted axi-symmetric force-free magnetospheric solutions. We solve the Grad-Shafranov equation by introducing an ansatz akin to a multipolar expansion. We obtain a hierarchical system of ordinary differential equations where lower-order multipoles source the higher-order ones. We show that analytical approximations can be obtained, and that in general solutions can be numerically computed using standard solvers. We obtain a class of solutions with a great flexibility in initial conditions, and show that a subset of these asymptotically tend to vacuum. The twist is not confined to a subset of field lines. The solutions are symmetric about the equator, with a toroidal component that can be reversed. This symmetry is supported by an equatorial current sheet. We provide a first-order approximation of a particular solution that consists in the superposition of a vacuum dipole and a toroidal magnetic field sourced by the dipole, where the toroidal component decays as $1/r^4$ . As an example of strongly multipolar solution, we also exhibit cases with an additional octupole component.


![[mdfiles/2504.00680.md|2504.00680]]
### AI Justification:
The paper presents a new class of twisted magnetospheric solutions, which could provide insights into "magnetic field amplification" in neutron stars, aligning with your interest in the behaviors of magnetic fields within plasma environments. The description of force-free solutions and the role of twists in magnetosphere dynamics may also extend to your examination of how "magnetic fields behave" across different astrophysical scales, contributing relevant methodologies and findings.
# (106/382) http://arxiv.org/pdf/2504.00495v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Early Planet Formation in Embedded Disks (eDisk) XXI... Limited role of streamers in mass supply to the disk in the Class 0 protostar IRAS 16544-1604
**Miyu Kido,Hsi-Wei Yen,Jinshi Sai,Shigehisa Takakuwa,Nagayoshi Ohashi,Yuri Aikawa,...**


#mhd
### Abstract:
Asymmetric and narrow infalling structures, often called streamers, have been observed in several Class 0/I protostars, which is not expected in the classical star formation picture. Their origin and impact on the disk formation remain observationally unclear. By combining data from the James Cleark Maxwell Telescope (JCMT) and Atacama Large Millimeter/submillimeter Array (ALMA), we investigate the physical properties of the streamers and parental dense core in the Class 0 protostar, IRAS 16544 $-$ 1604. Three prominent streamers associated to the disk with lengths between 2800 to 5800 au, are identified on the northern side of the protostar in the C $^{18}$ O emission. Their mass and mass infalling rates are estimated to be in the range of (1-4) $\times$ 10 $^{-3}$ $M_\odot$ and (1-5) $\times$ 10 $^{-8}$ $M_\odot$ yr $^{-1}$ , respectively. Infall signatures are also observed in the more diffuse extended protostellar envelope observed with the ALMA from the comparison to the infalling and rotating envelope model. The parental dense core detected by the JCMT observation has a mass of $\sim$ 0.5 $M_\odot$ , sub to transonic turbulence of $\mathcal{M}$ $=$ 0.8-1.1, and a mass-to-flux ratio of 2-6. Our results show that the streamers in IRAS 16544-1604 only possess 2% of the entire dense core mass and contribute less than 10% of the mass infalling rate of the protostellar envelope. Therefore, the streamers in IRAS 16544-1604 play a minor role in the mass accretion process onto the disk, in contrast to those streamers observed in other sources and those formed in numerical simulations of collapsing dense cores with similar turbulence and magnetic field strengths.


![[mdfiles/2504.00495.md|2504.00495]]
### AI Justification:
This paper is relevant to your research interests as it examines the dynamics of mass infall and the interaction of structures such as streamers in the protostellar environment, which relates to your focus on "force interactions shaping magnetic dynamics." Additionally, the study's exploration of "turbulence" and its effects on mass accretion gives insight into the "emergent magnetic dynamics in turbulent plasmas," aligning well with your interest in multi-scale magnetic field behaviors in plasma environments.
# (107/382) http://arxiv.org/pdf/2503.08520v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Observation of Alfven solitons in the solar corona using Parker Solar Probe (PSP) and Solar and Heliospheric Observatory (SOHO)
**Murchana Khusroo,Ankita Thapa**


#mhd
### Abstract:
Solitons are predominantly observed in near-earth plasmas as well as planetary magnetospheres; however, their existence in the solar corona remains largely unexplored, despite theoretical investigations. This study aims to address this gap by examining the presence and dynamics of solitons in the solar corona, particularly in the context of coronal heating. Utilizing observational data from the Parker Solar Probe (PSP) and Solar and Heliospheric Observatory (SOHO) during the onset of a strong Coronal Mass Ejection (CME) event, the analyses reveal a train of aperiodic solitons with increasing amplitude preceding the eruption. A key finding of this study is that the observed aperiodic soliton train serves as a potential candidate in facilitating energy transfer through dissipation within the coronal plasma, hereby, influencing the initiation of solar eruptive events such as a CME. A defining characteristic of this solitary train is its hypersonic and super-Alfvenic nature, evident from the presence of high Mach numbers that reinforces its role in plasma energy equilibration in the solar corona, thereby contributing to plasma heating.


![[mdfiles/2503.08520.md|2503.08520]]
### AI Justification:
This paper is relevant to your research interests as it explores the dynamics of solitons in the solar corona, which aligns with your focus on "the magnetic dynamics of plasmas in the interstellar medium." Additionally, the observational study's examination of solitons as a mechanism for energy transfer and their hypersonic and super-Alfvenic characteristics provides valuable insight into "how magnetic fields behave, interact, and amplify across various scales," particularly in the context of coronal heating.
# (108/382) http://arxiv.org/pdf/2503.01965v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### X-ray cavities in TNG-Cluster... a direct comparison to observations
**Marine Prunier,Annalisa Pillepich,Julie Hlavacek-Larrondo,Dylan Nelson**


#mhd
### Abstract:
The TNG-Cluster magnetohydrodynamic cosmological simulations, produce a diverse population of X-ray cavities in the intracluster medium (ICM) of simulated galaxy clusters. These arise from episodic, high velocity, kinetic energy injections from the central active supermassive black hole (AGN, SMBH). Here, we present the first comprehensive comparative analysis of X-ray cavities in TNG-Cluster with observational data. First, we select a volume-limited sample of 35 real clusters ( $z \leq 0.071$ , M $_\text{500c}$ = 10 $^{14-14.8}$ M $_\odot$ ) observed with the Chandra X-ray Observatory, identify 3 analogs for each in TNG-Cluster (total of 105) and generate mock Chandra images using same exposure times as their observed counterparts. We identify X-ray cavities and measure their properties in both datasets using identical techniques, ensuring a direct, apples-to-apples comparison. Our analysis reveals that both samples have a similar fraction of X-ray cavities (35-43 per cent). They exhibit comparable sizes and morphologies, although the sizes of simulated X-ray cavities still attached to the SMBH are somewhat larger in TNG-Cluster -- a scarcity at $< 10$ kpc. The area of TNG X-ray cavities increases as they rise in the ICM, consistent with the trend seen in the observational sample. The cavity powers, estimated using observational techniques, show good agreement between the two samples (10 $^{42-45}$ erg.s $^{-1}$ ), suggesting that X-ray cavities in the simulation are an important heating mechanism in cluster cores. Overall, the rather simple AGN feedback model of TNG, with no model choices made to reproduce X-ray morphological features, and without cosmic rays, creates a quantitatively realistic population of X-ray cavities at cluster scales.


![[mdfiles/2503.01965.md|2503.01965]]
### AI Justification:
This paper is relevant to your research interests as it explores the interactions between magnetic fields and plasma dynamics in the intercluster medium, particularly through the study of X-ray cavities and their relation to active galactic nuclei (AGN) feedback mechanisms. The focus on "magnetic dynamics" and "intracluster medium" aligns well with your interest in the "scale-dependent magnetic structuring" and the role of forces affecting magnetic behavior in astrophysical plasmas.
# (109/382) http://arxiv.org/pdf/2503.22245v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### First snapshot of a magnetosphere around a Herbig Ae/Be star
**S. P. Jarvinen,S. Hubrig,M. Kuker,U. Ziegler,I. Ilyin,M. Scholler,...**


#mhd
### Abstract:
The Herbig Ae/Be star HD190073 is one of the very few magnetic Herbig Ae/Be stars for which close low-mass companions have been reported. Previously published magnetic field measurements indicated an annual change in the field configuration. We aim to study in detail the spectral and magnetic variability of this star and characterise its magnetosphere for the first time. Newly acquired and archival spectropolarimetric observations are combined to determine a more precise magnetic period and to constrain the geometry of the magnetic field. The variability of hydrogen line profiles is studied using dynamical spectra. Archival X-shooter observations of the He I 10830 ang triplet are used to characterise its variability over the rotation cycle. Further, we carry out 2D magnetohydrodynamical simulations of the magnetosphere using the Nirvana code. From the spectropolarimetric observations, we determine for HD190073 a magnetic period P=51.70 d. We estimate a magnetic obliquity angle 82.9 degr and a dipole strength 222 G. Our dynamical spectra constructed for the hydrogen line profiles observed during 2011 clearly reveal a ringlike magnetospheric structure appearing at the rotation phase of best visibility of the positive magnetic pole. These spectra present the first snapshot of a magnetosphere around a Herbig Ae/Be star. 2D MHD simulations involving nonisothermal gas show that the magnetosphere is compact, with a radius of about $3\,R_*$ , and that the wind flow extends over tens of $R_*$ . With a reported radius of the accretion disk of 1.14 au around HD190073, the distance between the star and the disk is about 25 $R_*$ . The detection of a magnetosphere around HD190073, and the possible presence of lower-mass companions at different distances, make this system a valuable laboratory for studying the magnetic interaction between the host star, its companions, and the accretion disk.


![[mdfiles/2503.22245.md|2503.22245]]
### AI Justification:
This paper is relevant to your research interests as it involves the characterization of magnetic fields and their interactions within a magnetosphere, specifically through the use of "2D magnetohydrodynamical simulations" and "spectropolarimetric observations," aligning well with your focus on magnetic field amplification and interactions in plasma environments. The study of the "magnetic variability" and structure of the magnetosphere surrounding a Herbig Ae/Be star also touches on your interest in how magnetic fields behave and evolve in astrophysical plasmas across different scales.
# (110/382) http://arxiv.org/pdf/2503.21492v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### 3D MHD simulations of runaway pulsars in core collapse supernova remnants
**D. M. A. Meyer,D. F. Torres,Z. Meliani**


#mhd
### Abstract:
Pulsars are one of the possible final stages in the evolution of massive stars. If a supernova explosion is anisotropic, it can give the pulsar a powerful kick, propelling it to supersonic speeds. The resulting pulsar wind nebula is significantly reshaped by its interaction with the surrounding medium as the pulsar moves through it. First, the pulsar crosses the supernova remnant, followed by the different layers of circumstellar medium formed during different stages of the progenitor star s evolution. We aim to investigate how the evolutionary history of massive stars shapes the bow shock nebulae of runaway kicked pulsars, and how these influences in turn affect the dynamics and non-thermal radio emission of the entire pulsar remnant. We perform three-dimensional magnetohydrodynamic simulations using the PLUTO code to model the pulsar wind nebula generated by a runaway pulsar in the supernova remnant of a red supergiant progenitor, and derive its non-thermal radio emission. The supernova remnant and the pre-supernova circumstellar medium of the progenitor strongly confine and reshape the pulsar wind nebula of the runaway pulsar, bending its two side jets inwards and giving the nebula an arched shape for an observer perpendicular to the jets and the propagation direction, as observed around PSR J1509 5850 and Gemina. We perform the first classical 3D model of a pulsar moving inward through its supernova ejecta and circumstellar medium, inducing a bending of its polar jet that turns into characteristic radio synchrotron signature. The circumstellar medium of young runaway pulsars has a significant influence on the morphology and emission of pulsar wind nebulae, whose comprehension requires a detailed understanding of the evolutionary history of the progenitor star.


![[mdfiles/2503.21492.md|2503.21492]]
### AI Justification:
The paper's focus on "three-dimensional magnetohydrodynamic simulations" directly ties to your interest in "theoretical models" and "simulations" addressing magnetic dynamics in plasma environments. Additionally, the investigation of how "the circumstellar medium of young runaway pulsars has a significant influence on the morphology and emission of pulsar wind nebulae" complements your focus on "scale-dependent magnetic structuring" and the role of magnetic fields in shaping structures across various astrophysical scales.
# (111/382) http://arxiv.org/pdf/2503.21344v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### X-ray Polarization of the High-Synchrotron-Peak BL Lacertae Object 1ES 1959+650 during Intermediate and High X-ray Flux States
**Luigi Pacciani,Dawoon E. Kim,Riccardo Middei,Herman L. Marshall,Alan P. Marscher,Ioannis Liodakis,...**


#mhd
### Abstract:
We report the Imaging X-ray Polarimetry Explorer (IXPE) polarimetric and simultaneous multiwavelength observations of the high-energy-peaked BL Lacertae (HBL) object 1ES 1959+650, performed in 2022 October and 2023 August. In 2022 October IXPE measured an average polarization degree $\Pi_{\rm X}=9.4\;\!\%\pm 1.6\;\!\% $ and an electric-vector position angle $ \psi_{\rm X}=53^{\circ}\pm 5^{\circ}$ . The polarized X-ray emission can be decomposed into a constant component, plus a rotating component, with rotation velocity $\omega_{\rm EVPA}=(-117\;\!\pm\;\!12) $ $ {\rm deg}\;\!{\rm d}^{-1}$ . In 2023 August, during a period of pronounced activity of the source, IXPE measured an average $\Pi_{\rm X}=12.4\;\!\%\pm0.7\;\!\%$ and $\psi_X=20^{\circ}\pm2^{\circ}$ , with evidence ( $\sim$ 0.4 $\;\!\%$ chance probability) for a rapidly rotating component with $\omega_{\rm EVPA}=(1864\;\!\pm\;\!34)$ ${\rm deg}\;\!{\rm d}^{-1}$ . These findings suggest the presence of a helical magnetic field in the jet of 1ES 1959+650 or stochastic processes governing the field in turbulent plasma. Our multiwavelength campaigns from radio to X-ray reveal variability in both polarization and flux from optical to X-rays. We interpret the results in terms of a relatively slowly varying component dominating the radio and optical emission, while rapidly variable polarized components dominate the X-ray and provide minor contribution at optical wavelengths. The radio and optical data indicate that on parsec scales the magnetic field is primarily orthogonal to the jet direction. On the contrary, X-ray measurements show a magnetic field almost aligned with the parsec jet direction. Confronting with other IXPE observations, we guess that the magnetic field of HBLs on sub-pc scale should be rather unstable, often changing its direction with respect to the VLBA jet.


![[mdfiles/2503.21344.md|2503.21344]]
### AI Justification:
This paper is relevant to your interests in theoretical astrophysics and plasma physics, particularly due to its findings on "the presence of a helical magnetic field in the jet" and the mention of "stochastic processes governing the field in turbulent plasma," which directly relates to your focus on emergent magnetic dynamics in turbulent plasmas. Additionally, the analysis of magnetic field orientation on "parsec scales" aligns with your interest in scale-dependent magnetic structuring, helping to elucidate how magnetic fields behave within various astrophysical environments.
# (112/382) http://arxiv.org/pdf/2503.20740v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The effect of shear flow on the resistive tearing instability
**Alfred Mallet,Stefan Eriksson,Marc Swisdak,James Juno**


#mhd
### Abstract:
We develop a new scaling theory for the resistive tearing mode instability of a current sheet with a strong shear flow across the layer. The growth rate decreases with increasing flow shear and is completely stabilized as the shear flow becomes Alfv\enic... both in the constant- $\Psi$ regime, as in previous results, but we also show that the growth rate is in fact suppressed more strongly in the nonconstant- $\Psi$ regime. As a consequence, for sufficiently large flow shear, the maximum of the growth rate is always affected by the shear suppression, and the wavenumber at which this maximum growth rate is attained is an increasing function of the strength of the flow shear. These results may be important for the onset of reconnection in imbalanced MHD turbulence.


![[mdfiles/2503.20740.md|2503.20740]]
### AI Justification:
The paper explores "the resistive tearing mode instability" and its interactions with "shear flow," which aligns with your interest in "magnetic dynamics" and "force interactions" in plasmas. Furthermore, the focus on how flow shear affects the instability growth rate could provide insights into "emergent magnetic dynamics" within turbulent plasmas, thus offering a relevant perspective on the multi-scale behavior of magnetic fields in your research area.
# (113/382) http://arxiv.org/pdf/2503.19956v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Go with the Flow... The Self-Similar and Non-Linear Behaviour of Large-Scale In- and Outflows and the Impact of Accretion Shocks from Galaxies to Galaxy Clusters
**Benjamin A. Seidel,Rhea-Silvia Remus,Lucas M. Valenzuela,Lucas C. Kimmig,Klaus Dolag**


#mhd
### Abstract:
From the scale-free nature of gravity, the structure in the universe is expected to be self-similar on large scales. However, this self-similarity will eventually break down due to small-scale gas physics such as star formation, AGN and stellar feedback as well as non-linear effects gaining importance relative to linear structure formation. In this work we investigate the large-scale matter flows that connect collapsed structures to their cosmic environments specifically for their agreement with self-similarity in various properties. For this purpose we use the full power of the hydrodynamical cosmological simulation suite Magneticum Pathfinder to calculate the in- and outflow rates for haloes on a large range of masses and redshifts. We find a striking self-similarity across the whole mass range and cosmic epochs that only breaks in the outflowing regime due to the different outflow driving mechanisms for galaxies vs. galaxy clusters. Geometrical analysis of the patterns of in vs. outflow demonstrate how the inflows organize into anisotropic filaments driven by the tidal environment, while the outflows are isotropic due to their thermal nature. This also manifests in the thermal and chemical properties of the gas... While the inflowing gas is pristine and colder, encountering the accretion shocks and entering the influence region of AGN and stellar feedback heats the gas up into a diffuse, metal enriched and hot atmosphere. Overall the differences between outflowing and infalling gas are enhanced at the galaxy cluster scale compared to the galaxy scale due to the accretion shocks that reach out to large radii for these objects. An individual study of the gas motions in the outskirts of one of the most massive clusters in the simulations illustrates these results... Gas found in the outer hot atmosphere at z=0 falls in and is completely enriched early before being shock heated and expanding.


![[mdfiles/2503.19956.md|2503.19956]]
### AI Justification:
This paper is relevant to your interests as it explores the "large-scale matter flows" and their impact on structures, aligning with your focus on "scale-dependent magnetic structuring" and the interactions of various forces in plasma environments. Additionally, the investigation of "accretion shocks" and their influence on gas dynamics resonates with your interest in "force interactions shaping magnetic dynamics," providing potential insights into how these phenomena affect magnetic field behaviors in astrophysical settings.
# (114/382) http://arxiv.org/pdf/2503.19905v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Helmet streamer influence on the evolution of magnetic flux ropes
**M. Cecere,P. F. Wyper,G. Krause,A. Sahade,O. E. K. Rice**


#mhd
### Abstract:
Context... Solar eruptions are crucial for space weather studies. Understanding the mechanisms influencing their evolution is key to improving predictions of their geoeffectiveness. Helmet streamers (HSs) are persistent structures in the solar corona, present in both minimum and maximum solar activity periods. These structures contain a current sheet of low magnetic energy, where coronal mass ejections (CMEs) tend to deflect. However, they also feature a closed magnetic field region beneath this sheet, often confining eruptions. Their complexity makes predicting eruptions challenging. Aims... This study examines how HSs influence the evolution and potential confinement of magnetic flux ropes (MFRs). We explore magnetic configurations where the MFR is more likely to rise through the overlying field, aiming to establish simple parameters that help predict whether an MFR will ascend or remain confined. Methods... Using 2.5D MHD simulations, we model MFR dynamics in the presence of an HS, analyzing different magnetic configurations and focusing on the mechanisms that enable ascent or confinement. Results... Null-point reconnection plays a key role in MFR dynamics. Depending on the initial configuration, it can either disrupt the MFR, preventing ascent, or reduce the strapping flux, facilitating upward motion. We identify a critical threshold... if the strapping flux above the MFR is less than two-thirds of its poloidal flux, the MFR ascends successfully. Conclusions... Our simulations show that null-point reconnection significantly impacts MFR ascent. A key predictor of successful rise is the initial ratio of the MFRs poloidal flux to the strapping flux above it.


![[mdfiles/2503.19905.md|2503.19905]]
### AI Justification:
This paper is relevant to your research interests as it explores "magnetic configurations" and how "magnetic flux ropes" (MFRs) interact with surrounding magnetic fields, aligning with your focus on "magnetic dynamics" and "interactions between magnetic forces." The use of "2.5D MHD simulations" to examine the "ascent or confinement" of MFRs could provide valuable insights into the mechanisms driving "magnetic field amplification" in astrophysical plasmas, particularly within the context of solar phenomena.
# (115/382) http://arxiv.org/pdf/2503.14842v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Comparative Analysis of Hall Effect Implementations in Hall-Magnetohydrodynamics
**Kazunari Iwasaki,Kengo Tomida**


#mhd
### Abstract:
There is no standard numerical implementation of the Hall effect, which is one of the non-ideal magnetohydrodynamic (MHD) effects. Numerical instability arises when a simple implementation is used, in which the Hall electric field is added to the electric field to update magnetic fields without further modifications to the numerical scheme. In this paper, several implementations proposed in the literature are compared to identify an approach that provides stable and accurate results. We consider two types of implementations of the Hall effect. One is a modified version of the Harten-Lax-van Leer method (Hall-HLL) in which the phase speeds of whistler waves are adopted as the signal speeds; the other involves adding a fourth-order hyper-resistivity to a Hall-MHD code. Based on an extensive series of test calculations, we found that hyper-resistivity yields more accurate results than the Hall-HLL, particularly in problems where the whisler-wave timescale is shorter than the the timescale of physical processes of interest. Through both von Neumann stability analysis and numerical experiments, an appropriate coefficient for the hyper-resistivity is determined.


![[mdfiles/2503.14842.md|2503.14842]]
### AI Justification:
The paper focuses on the Hall effect in Hall-Magnetohydrodynamics (MHD) and its implications for numerical stability and accuracy, which is crucial for theoretical simulations in astrophysics. This aligns with your interest in “how magnetic fields behave, interact, and amplify” as it explores a mechanism related to magnetic dynamics in interstellar plasmas, particularly in the context of improving simulations to better understand the evolution of these fields.
# (116/382) http://arxiv.org/pdf/2503.13876v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On Using Gradient Dynamic Spectra (GraDS) to Study Type-II Solar Radio Bursts
**Puja Majee,Devojyoti Kansabanik,Divya Oberoi**


#mhd
### Abstract:
Solar type-II radio bursts are coherent plasma emissions arising from magnetohydrodynamic shocks produced by either coronal mass ejections (CMEs) or flares. Type-II bursts sometimes show split-band emissions in the dynamic spectrum. When these split-band emissions come from regions just upstream and downstream of the shock, type-II band-splitting can be used as an important tool for estimating magnetic fields at the shock front. Earlier studies have shown that only $\sim$ 20\% of the type-IIs show morphologically similar split-bands. Imaging studies can unambiguously identify such instances, though they remain very rare. Here we suggest a useful approach to augment dynamic spectra-based studies by also examining the Gradient Dynamic Spectra (GraDS) of type-II emission. We also verified the conclusions of this approach against those from an imaging study.


![[mdfiles/2503.13876.md|2503.13876]]
### AI Justification:
The paper explores "magnetohydrodynamic shocks" associated with "type-II solar radio bursts," directly tying into your interest in the behavior and evolution of magnetic fields in plasma environments. The proposed method using Gradient Dynamic Spectra (GraDS) to estimate magnetic fields at the shock front aligns with your focus on magnetic field amplification and shaping structures within astrophysical plasmas.
# (117/382) http://arxiv.org/pdf/2503.14455v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Origin of holes and rings in the Green Monster of Cassiopeia A... Insights from 3D magnetohydrodynamic simulations
**S. Orlando,H. -T. Janka,A. Wongwathanarat,F. Bocchino,I. De Looze,D. Milisavljevic,...**


#mhd
### Abstract:
[Abridged] Cassiopeia A (Cas A) provides a unique opportunity to study supernova (SN) dynamics and interactions with the circumstellar medium (CSM). Recent JWST observations revealed the `Green Monster` (GM), a structure with a likely CSM origin. We investigate its pockmarked morphology, characterized by circular holes and rings, by examining the role of small-scale ejecta structures interacting with a dense circumstellar shell. We adopted a neutrino-driven SN model to trace the evolution of its explosion from core collapse to the age of the Cas A remnant using high-resolution 3D magnetohydrodynamic simulations. Besides other processes, the simulations include self-consistent calculations of radiative losses, accounting for deviations from electron-proton temperature equilibration and ionization equilibrium, as well as the ejecta composition derived from the SN. The GMs morphology is reproduced by dense ejecta clumps and fingers interacting with an asymmetric, forward-shocked circumstellar shell. The clumps and fingers form by hydrodynamic instabilities growing at the interface between SN ejecta and shocked CSM. Radiative cooling accounting for effects of non-equilibrium of ionization enhances the ejecta fragmentation, forming dense knots and thin filamentary structures that penetrate the shell, producing a network of holes and rings with properties similar to those observed. The origin of the holes and rings in the GM can be attributed to the interaction of ejecta with a shocked circumstellar shell. By constraining the timing of this interaction and analyzing the properties of these structures, we provide a distinction of this scenario from an alternative hypothesis, which attributes these features to fast-moving ejecta knots penetrating the shell ahead of the forward shock.


![[mdfiles/2503.14455.md|2503.14455]]
### AI Justification:
This paper is relevant to your research interests because it employs "3D magnetohydrodynamic simulations," aligning with your focus on "theoretical models and simulations" in plasma environments. Additionally, the study examines the interactions between supernova ejecta and the circumstellar medium, which may provide insights into "magnetic field amplification" and the "role of magnetic fields in organizing structures" within astrophysical plasmas.
# (118/382) http://arxiv.org/pdf/2503.13800v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Minifilament Eruptions as the Last Straw to Break the Equilibrium of a Giant Solar Filament
**Hechao Chen,Hui Tian,Quanhao Zhang,Chuan Li,Chun Xia,Xianyong Bai,...**


#mhd
### Abstract:
Filament eruptions are magnetically driven violent explosions commonly observed on the Sun and late-type stars, sometimes leading to monster coronal mass ejections that directly affect the nearby planets environments. More than a century of research on solar filaments suggests that the slow evolution of photospheric magnetic fields plays a decisive role in initiating filament eruptions, but the underlying mechanism remains unclear. Using high-resolution observations from the \textit{Chinese H $\alpha$ Solar Explorer}, the \textit{Solar Upper Transition Region Imager}, and the \textit{Solar Dynamics Observatory}, we present direct evidence that a giant solar filament eruption is triggered by a series of minifilament eruptions occurring beneath it. These minifilaments, which are homologous to the giant filament but on a smaller tempo-spatial scale, sequently form and erupt due to extremely weak mutual flux disappearance of opposite-polarity photospheric magnetic fields. Through multi-fold magnetic interactions, these erupting minifilaments act as the last straw to break the force balance of the overlying giant filament and initiate its ultimate eruption. The results unveil a possible novel pathway for small-scale magnetic activities near the stellar surface to initiate spectacular filament eruptions, and provide new insight into the magnetic coupling of filament eruptions across different tempo-spatial scales.


![[mdfiles/2503.13800.md|2503.13800]]
### AI Justification:
This paper is relevant to your research interests as it discusses "magnetically driven violent explosions" and the role of "photospheric magnetic fields" in filament eruptions, directly relating to your focus on "magnetic field amplification" and "scale-dependent magnetic structuring." Additionally, the exploration of "multi-fold magnetic interactions" provides insight into how magnetic dynamics operate across different scales, aligning well with your interest in emergent behaviors in turbulent plasma environments.
# (119/382) http://arxiv.org/pdf/2503.00636v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Simons Observatory... Science Goals and Forecasts for the Enhanced Large Aperture Telescope
**The Simons Observatory Collaboration,M. Abitbol,I. Abril-Cabezas,S. Adachi,P. Ade,A. E. Adler,...**


#mhd
### Abstract:
We describe updated scientific goals for the wide-field, millimeter-wave survey that will be produced by the Simons Observatory (SO). Significant upgrades to the 6-meter SO Large Aperture Telescope (LAT) are expected to be complete by 2028, and will include a doubled mapping speed with 30,000 new detectors and an automated data reduction pipeline. In addition, a new photovoltaic array will supply most of the observatorys power. The LAT survey will cover about 60% of the sky at a regular observing cadence, with five times the angular resolution and ten times the map depth of Planck. The science goals are to... (1) determine the physical conditions in the early universe and constrain the existence of new light particles; (2) measure the integrated distribution of mass, electron pressure, and electron momentum in the late-time universe, and, in combination with optical surveys, determine the neutrino mass and the effects of dark energy via tomographic measurements of the growth of structure at $z < 3$ ; (3) measure the distribution of electron density and pressure around galaxy groups and clusters, and calibrate the effects of energy input from galaxy formation on the surrounding environment; (4) produce a sample of more than 30,000 galaxy clusters, and more than 100,000 extragalactic millimeter sources, including regularly sampled AGN light-curves, to study these sources and their emission physics; (5) measure the polarized emission from magnetically aligned dust grains in our Galaxy, to study the properties of dust and the role of magnetic fields in star formation; (6) constrain asteroid regoliths, search for Trans-Neptunian Objects, and either detect or eliminate large portions of the phase space in the search for Planet 9; and (7) provide a powerful new window into the transient universe on time scales of minutes to years, concurrent with observations from Rubin of overlapping sky.


![[mdfiles/2503.00636.md|2503.00636]]
### AI Justification:
The paper outlines objectives related to the "properties of dust and the role of magnetic fields in star formation," which resonates with your interest in understanding "how magnetic fields behave, interact, and amplify across various scales." Additionally, the mention of "polarized emission from magnetically aligned dust grains" suggests an exploration of magnetic dynamics within plasma environments, aligning well with your focus on magnetic field amplification and emergent magnetic behaviors.
# (120/382) http://arxiv.org/pdf/2503.11875v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Galactic population of magnetars ... a simulation-based inference study
**Matteo Sautron,Alexander Eli McEwen,George Younes,Jerome Petri,Paz Beniamini,Daniela Huppenkothen**


#mhd
### Abstract:
Population synthesis modeling of the observed dynamical and physical properties of a population is a highly effective method for constraining the underlying birth parameters and evolutionary tracks. In this work, we apply a population synthesis model to the canonical magnetar population to gain insight into the parent population. We utilize simulation-based inference to reproduce the observed magnetar population with a model which takes into account the secular evolution of the force-free magnetosphere and magnetic field decay simultaneously and self-consistently. Our observational constraints are such that no magnetar is detected through their persistent emission when convolving the simulated populations with the XMM-Newton EPIC-pn Galactic plane observations, and that all of the $\sim$ 30 known magnetars are discovered through their bursting activity in the last $\sim50$ years. Under these constraints, we find that, within 95 % credible intervals, the birth rate of magnetars to be $1.8^{+2.6}_{-0.6}$ kyr $^{-1}$ , and lead to having $10.7^{+18.8}_{-4.4}$ % of neutron stars born as magnetars. We also find a mean magnetic field at birth ( $\mu_b$ is in T) $\log\left(\mu_b\right) = 10.2^{+0.1}_{-0.2} $ , a magnetic field decay slope $ \alpha_d = 1.9 ^{+0.9}_{-1.3} $ , and timescale $ \tau_d = 17.9^{+24.1}_{-14.5}$ kyr, in broad agreement with previous estimates. We conclude this study by exploring detection prospects... an all-sky survey with XMM-Newton would potentially allow to get around 7 periodic detections of magnetars, with approximately 150 magnetars exceeding XMM-Newtons flux threshold, and the upcoming AXIS experiment should allow to double these detections.


![[mdfiles/2503.11875.md|2503.11875]]
### AI Justification:
This paper's relevance to your research interests lies in its exploration of magnetic dynamics, particularly in the context of magnetars and their evolution, which aligns with your focus on “magnetic field behavior” and the “amplification and evolution of magnetic fields in astrophysical plasmas.” Additionally, the study employs simulation-based methods to analyze magnetic field decay and evolution, providing insights into the “complex, multi-scale dynamics” of magnetic fields within plasma environments, which is central to your research goals.
# (121/382) http://arxiv.org/pdf/2503.11530v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Validating and improving two-fluid simulations of the magnetic field evolution in neutron star cores
**F. Castillo,N. A. Moraga,M. E. Gusakov,J. A. Valdivia,A. Reisenegger**


#mhd
### Abstract:
This paper addresses the evolution of an axially symmetric magnetic field in the core of a neutron star. The matter in the core is modeled as a system of two fluids, namely neutrons and charged particles, with slightly different velocity fields, controlled by their mutual collisional friction. This problem was addressed in our previous work through the so-called ``fictitious friction approach. We study the validity of our previous work and improve it by comparing the fictitious friction approach to alternatives, making approximations that allow it to be applied to arbitrary magnetic field strengths and using realistic equations of state. We assume the neutron star crust to be perfectly resistive, so its magnetic field reacts instantaneously to changes in the core, in which we neglect the effects of Cooper pairing. We explore different approaches to solve the equations to obtain the velocities and chemical potential perturbations induced by a given, fixed magnetic field configuration in the core. We also present a new version of our code to perform time-evolving simulations and discuss the results obtained with it. Our calculations without fictitious friction further confirm that bulk velocity is generally much greater than ambipolar velocity, leading to faster evolution. These findings align with those with fictitious friction, validating this approach. We also find that, in the long term, the star evolves towards a barotropic ``Grad-Shafranov equilibrium, where the magnetic force is fully balanced by charged particle fluid forces. Qualitatively, the evolution and the final equilibrium are independent of the magnetic field strength $B$ and the equation of state considered. The timescale to reach this equilibrium is proportional to $B^{-2}$ and becomes shorter for equations of state with a smaller gradient of the ratio between the densities of protons and neutrons.


![[mdfiles/2503.11530.md|2503.11530]]
### AI Justification:
This paper is relevant to your research interests in theoretical astrophysics and plasma physics as it examines the "evolution of an axially symmetric magnetic field" in a plasma environment, which aligns with your focus on the "magnetic dynamics of plasmas." Additionally, the study's exploration of magnetic force balance and its dependence on "bulk velocity" reflects your interest in "force interactions shaping magnetic dynamics," contributing to a deeper understanding of how magnetic fields behave within astrophysical plasmas.
# (122/382) http://arxiv.org/pdf/2503.11380v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Data-constrained 3D MHD Simulation of a Spiral Jet Caused by an Unstable Flux Rope Embedded in Fan-spine Configuration
**Z. F. Li,J. H. Guo,X. Cheng,M. D. Ding,L. P. Chitta,H. Peter,...**


#mhd
### Abstract:
Spiral jets are impulsive plasma ejections that typically show an apparent rotation motion. Their generation, however, is still nont understood thoroughly. Based on a high-resolution vector magnetogram form the Polarimetric and Helioseismic Imager onboard Solar Orbiter, we constrcut a data-constrained three-dimensional (3D) MHD model, aiming to disclose the eruption mechanism of a tiny spiral jet at a moss region observed on March 3 2022. The initial configuration of the simulation consists of an extrapolated coronal magnetic field based on the vector magnetogram and an inserted unstable flux rope constructed by the Regularized Biot-Savart Laws method. Our results highlight the critical role of the fan-spine configuration in forming the spiral jet and confirm the collapse of the pre-existing magnetic null to a curved 3D current sheet where external reconnection takes places. It is further disclosed that the flux rope quickly moves upward, reconnecting with the field lines near the outer spine, thereby enabling the transfer of twist and cool material from the flux rope to the open field, giving rise to the tiny spiral jet we observed. The notable similarities between these characteristics and those for larger-scale jets suggest that spiral jets, regardless of their scale, essentially share the same eruption mechanism.


![[mdfiles/2503.11380.md|2503.11380]]
### AI Justification:
This paper is relevant to my research interests as it explores the dynamics of magnetic fields through a data-constrained 3D MHD model, linking to my focus on "magnetic field amplification" and the "interactions between magnetic, gravitational, and thermal forces." The paper's findings on how the "critical role of the fan-spine configuration" shapes magnetic structures and jet dynamics contribute to understanding "scale-dependent magnetic structuring" in plasma environments.
# (123/382) http://arxiv.org/pdf/2503.09599v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Hints of Primordial Magnetic Fields at Recombination and Implications for the Hubble Tension
**Karsten Jedamzik,Levon Pogosian,Tom Abel**


#mhd
### Abstract:
Primordial Magnetic Fields (PMFs), long studied as potential relics of the early Universe, accelerate the recombination process and have been proposed as a possible way to relieve the Hubble tension. However, previous studies relied on simplified toy models. In this study, for the first time, we use the recent high-precision evaluations of recombination with PMFs, incorporating full magnetohydrodynamic (MHD) simulations and detailed Lyman-alpha radiative transfer, to test PMF-enhanced recombination ( $b\Lambda$ CDM) against observational data from the cosmic microwave background (CMB), baryon acoustic oscillations (BAO), and Type Ia supernovae (SN). Focusing on non-helical PMFs with a Batchelor spectrum, we find a preference for present-day total field strengths of approximately 5-10 pico-Gauss. Depending on the dataset combination, this preference ranges from mild ( $\sim 1.8\sigma$ with Planck + DESI) to moderate ( $\sim 3\sigma$ with Planck + DESI + SH0ES-calibrated SN) significance. The $b\Lambda$ CDM has Planck + DESI $\chi^2$ values equal or better than those of the $\Lambda$ CDM model while predicting a higher Hubble constant. The favored field strengths align closely with those required for cluster magnetic fields to originate entirely from primordial sources, without the need for additional dynamo amplification or stellar magnetic field contamination. Future high-resolution CMB temperature and polarization measurements will be crucial for confirming or further constraining the presence of PMFs at recombination.


![[mdfiles/2503.09599.md|2503.09599]]
### AI Justification:
The paper’s examination of Primordial Magnetic Fields (PMFs) aligns with my interest in "Magnetic Field Amplification," as it discusses the potential for these fields to affect astrophysical processes such as recombination and their implications for the Hubble tension. Furthermore, the use of "full magnetohydrodynamic (MHD) simulations" resonates with my focus on theoretical models and the role of magnetic dynamics in structured plasma environments.
# (124/382) http://arxiv.org/pdf/2503.09379v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Secondary black hole-induced magnetic reconnection in OJ 287... Implications for X-ray and radio emission
**S. Boula,A. Nathanail**


#mhd
### Abstract:
OJ 287, a nearby blazar, has exhibited remarkable variability in its optical light curve since 1888, characterized by ~12-year quasi-periodic outbursts. These events are attributed to the orbital dynamics of a supermassive binary black hole system at the heart of the blazar. This study explores the role of magnetic reconnection and the formation of plasmoid chains in driving the energetic processes responsible for OJ 287s variability. We propose that the passage of the secondary black hole through the magnetic field of the primary black holes accretion disk triggers magnetic reconnection, which contributes to the observed X-ray and radio emission features in OJ 287. We explore the connection between binary black hole interactions, accretion disk dynamics, and the formation of plasmoid chains as the secondary black hole passes through the magnetic field forest from the accretion disk and the jet of the primary. Our approach relies on numerical simulations to understand the formation of plasmoid chains resulting from black hole interactions and accretion disk dynamics. Based on such results, we employ simulation outcomes to examine the potential contribution to observed emissions, validating our assumptions about plasmoid chain creation. With this idea, we aim to establish a direct link between numerical simulations and observed emission, particularly in the case of OJ 287. Our findings confirm that the formation of plasmoid chains coincides with specific anomalous emission events observed in OJ 287. Notably, the radio emission patterns cannot be explained by a single blob model, as the necessary size to mitigate synchrotron self-absorption would be too large. This highlights the complexity of the emission processes and suggests that plasmoid chains could contribute to additional emission components beyond the steady jet.


![[mdfiles/2503.09379.md|2503.09379]]
### AI Justification:
The paper explores the role of magnetic reconnection and the dynamics of magnetic fields in the context of a blazar, which relates to your research focus on "Magnetic Field Amplification" and "Emergent Magnetic Dynamics in Turbulent Plasmas." Particularly, the investigation of "plasmoid chains" and their contribution to X-ray and radio emission provides insights into complex magnetic interactions that could be relevant to understanding magnetic behaviors on various scales in astrophysical plasmas.
# (125/382) http://arxiv.org/pdf/2503.08875v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Taylor-Couette flow with split endcaps... preparatory hydrodynamic study for upcoming DRESDYN-MRI experiment
**A. Mishra,P. Personnettaz,G. Mamatsashvili,V. Galindo,F. Stefani**


#mhd
### Abstract:
Magnetorotational instability (MRI) is of great importance in astrophysical disks, driving angular momentum transport and accretion of matter onto a central object. A Taylor-Couette (TC) flow between two coaxial cylinders subject to an axial magnetic field is a preferred setup for MRI-experiments. A main challenge in those experiments has been to minimize the effects of axial boundaries, or endcaps, which substantially alter the flow structure compared to the axially unbounded idealized case. Understanding the influence of endcaps on the flow stability is crucial for the unambiguous experimental identification of MRI. In this paper, we examine the hydrodynamic evolution of a TC flow in the presence of split endcap rims up to Reynolds number $Re =$ $2\times 10^5$ . At this $Re$ , the flow deviates from the ideal TC flow profile, resulting in about $15\%$ deviation in angular velocity at the mid-height of the cylinders. Aside from turbulent fluctuations caused by shearing instability at the endcaps, the bulk flow remains axially independent and exhibits Rayleigh stability. We characterize the scaling of the Ekman and Stewartson boundary layer thickness with respect to $Re$ . We also study the effect of changing the rotation ratio of the cylinders $\mu$ on the flow at large $Re$ and show that TC experiments can be conducted for larger $\mu \sim 0.5$ to safely ensure the hydrodynamic stability of the flow in the upcoming DRESDYN-MRI experiment. In all configurations considered, the modification of the flow profile by the endcaps further decreases the required critical threshold for the onset of MRI that can facilitate its detection in future experiments.


![[mdfiles/2503.08875.md|2503.08875]]
### AI Justification:
This paper discusses the **magnetorotational instability (MRI)**, which is a critical mechanism driving **angular momentum transport** in astrophysical plasmas, aligning with your interest in **magnetic dynamics**. Additionally, the examination of **flow stability** and its implications for upcoming experiments may provide insights into the **emergent magnetic dynamics** in turbulent plasma environments, thereby enhancing your understanding of how **magnetic fields interact** with flow structures in the interstellar medium.
# (126/382) http://arxiv.org/pdf/2503.06906v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Kinetic model and numerical method for multispecies radiation hydrodynamic system with multiscale nonequilibrium transport
**Mingyu Quan,Kun Xu**


#mhd
### Abstract:
This paper presents a comprehensive numerical framework for simulating radiation-plasma systems. The radiative transfer process spans multiple flow regimes due to varying fluid opacity across different regions, necessitating a robust numerical approach. We employ the multiscale unified gas-kinetic scheme (UGKS), which accurately captures photon transport phenomena from free streaming to diffusive wave propagation. The UGKS is also applied to the fluid model to address the significant mass disparity between electrons and ions, and their associated transport characteristics in both equilibrium continuum and non-equilibrium rarefied regimes. Our model explicitly incorporates momentum and energy exchanges between radiation and fluid fields in the coupled system, enabling detailed analysis of the complex interactions between electromagnetic and hydrodynamic phenomena. The developed algorithm successfully reproduces both optically thin and optically thick radiation limits while capturing the complex multiscale nonequilibrium dynamics of the coupled system. This unified treatment eliminates the need for separate numerical schemes in different regimes, providing a consistent and computationally effcient approach for the entire domain. The effectiveness and versatility of this approach are demonstrated through extensive numerical validation across a wide range of physical parameters and flow conditions.


![[mdfiles/2503.06906.md|2503.06906]]
### AI Justification:
This paper is relevant to your research interests as it explores "complex interactions between electromagnetic and hydrodynamic phenomena," which ties into your focus on how magnetic fields behave and evolve in astrophysical plasmas. The use of a "multiscale unified gas-kinetic scheme" for capturing "multiscale nonequilibrium dynamics" aligns well with your interest in the "scale-dependent magnetic structuring" and "emergent magnetic dynamics in turbulent plasmas."
# (127/382) http://arxiv.org/pdf/2503.05302v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Turbulence Induced Non-Gaussian Spectral Distortion in the Microwave Sky from Photon-Axion Conversion in Galaxy Clusters
**Harsh Mehta,Suvodip Mukherjee**


#mhd
### Abstract:
The conversion of CMB photons to axions (or axion-like particles (ALPs)) can lead to a unique spectral distortion in the temperature and polarization sky which can be explored in upcoming CMB experiments. In this work we have developed a numerical simulation-based technique of photons to ALPs conversion in the galaxy clusters and show for the first time that this physical process can lead to large non-Gaussian signal in the temperature and polarization field, which is impacted by the presence of inhomogeneities and turbulence in the electron density and magnetic field. Our simulation-based technique can simulate the theoretical signal for different scenarios of cluster electron density and magnetic field turbulence and provides testable predictions to discover ALPs from galaxy clusters using spatially non-Gaussian and anisotropic spectral distortion of the microwave sky. We show that the presence of turbulence in the magnetic field and electron density can impact the Gaussian part of the signal captured in terms of the angular power spectra of the signal by more than an order of magnitude. Also, the presence of turbulence in different clusters will lead the temperature and polarization fluctuations around the cluster region to have varying non-Gaussian distribution, with peaks and tails different from the Gaussian statistics of the CMB anisotropy. This new numerical technique has made it possible to calculate also the non-Gaussian signals and can be used in future CMB analysis in synergy with X-ray and radio observations to unveil ALPs coupling with photons in the currently unexplored ranges, for the masses between about $10^{-14}$ eV-- $10^{-11}$ eV.


![[mdfiles/2503.05302.md|2503.05302]]
### AI Justification:
This paper is relevant to your research interests in theoretical astrophysics and plasma physics as it discusses the impacts of turbulence within magnetic fields on signal distortion, which aligns with your focus on "Emergent Magnetic Dynamics in Turbulent Plasmas." Moreover, it incorporates numerical simulations that examine "their interactions shaping magnetic dynamics," particularly how inhomogeneities in the electron density and magnetic field influence the behavior of the cosmic microwave background (CMB) signals.
# (128/382) http://arxiv.org/pdf/2503.03820v2


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Leaking Outside the Box... Kinetic Turbulence with Cosmic-Ray Escape
**Evgeny A. Gorbunov,Daniel Groselj,Fabio Bacchini**


#mhd
### Abstract:
We study particle acceleration in strongly turbulent pair plasmas using novel 3D Particle-in-Cell simulations, featuring particle injection from an external heat bath and diffusive escape. We demonstrate the formation of steady-state, nonthermal particle distributions with maximum energies reaching the Hillas limit. The steady state is characterized by the equilibration of plasma kinetic and magnetic pressures, which imposes upper limits on the acceleration rate. With growing cold plasma magnetization $\sigma_0$ , nonthermal power-law spectra become harder, and the fraction of energy channeled into escaping cosmic rays increases. At $\sigma_0 \gtrsim 1$ , the escaping cosmic rays amount to more than 50% of the dissipated energy. Our method allows for kinetic studies of particle acceleration under steady-state conditions, with applications to a variety of astrophysical systems.


![[mdfiles/2503.03820.md|2503.03820]]
### AI Justification:
The paper discusses "steady-state, nonthermal particle distributions" and the interplay between "plasma kinetic and magnetic pressures," which aligns with my interest in "magnetic dynamics" and "force interactions shaping magnetic dynamics" in astrophysical plasmas. Additionally, the focus on "kinetic studies of particle acceleration" in turbulent environments adds value to my research on "emergent magnetic dynamics in turbulent plasmas."
# (129/382) http://arxiv.org/pdf/2503.04727v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### An active repeating fast radio burst in a magnetized eruption environment
**Y. Li,S. B. Zhang,Y. P. Yang,C. W. Tsai,X. Yang,C. J. Law,...**


#mhd
### Abstract:
Fast radio bursts (FRBs) are millisecond-duration radio bursts with unidentified extra-galactic origin. Some FRBs exhibit mild magneto-ionic environmental variations, possibly attributed to plasma turbulence or geometric configuration variation in a binary system. Here we report an abrupt magneto-ionic environment variation of FRB 20220529, a repeating FRB from a disk galaxy at redshift 0.1839. Initially, its Faraday rotation measure (RM) was $21 \pm 96~{\rm rad~m^{-2}}$ over 17 months. In December 2023, it jumped to $1976.9~{\rm rad~m^{-2}}$ , exceeding twenty times of the standard deviation of the previous RM variation, and returned to the typical values within two weeks. Such a drastic RM variation suggests a dense magnetized clump moving across the line of sight, possibly due to coronal mass ejection associated with a stellar flare. It indicates that the FRB likely has a companion star that produced the stellar flare.


![[mdfiles/2503.04727.md|2503.04727]]
### AI Justification:
This paper's exploration of "magneto-ionic environmental variations" in the context of the fast radio burst (FRB) relates to my research focus on the "interaction between magnetic, gravitational, and thermal forces" in plasma environments. The significant change in the Faraday rotation measure suggests an intriguing case of "magnetic dynamics" influencing radio emissions, potentially revealing insights into the "scale-dependent magnetic structuring" prevalent in astrophysical plasmas.
# (130/382) http://arxiv.org/pdf/2503.03863v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Testing the Flux Rope Paradigm for Coronal Mass Ejections Using a Three Spacecraft Encounter Event
**Brian E. Wood,Phillip Hess**


#mhd
### Abstract:
We present a 3-D morphological and field reconstruction of a coronal mass ejection (CME) from 2023 November 28, which hits three spacecraft near 1 au... Wind at Earths L1 Lagrange point; STEREO-A with a longitudinal separation of $6.5^{\circ}$ west of Earth; and Solar Orbiter (SolO) at $10.7^{\circ}$ east of Earth. The reconstruction assumes a magnetic flux rope (MFR) structure for the CME. With this event, we test whether field tracings observed by a spacecraft passing near the central axis of a CME MFR (STEREO-A) can be used to successfullly predict the field behavior seen by a spacecraft $17^{\circ}$ away (SolO), which has a more grazing encounter with the CME. We find that the MFR model does have significant success in simultaneously reproducing the field signs and rotations seen at STEREO-A, Wind, and SolO. This provides support for the MFR paradigm for CME structure. However, the SolO measurements, which are farthest from the central axis of the MFR, show less defined MFR signatures, presumably due to a greater degree of erosion and degradation of the MFR structure far from its central axis.


![[mdfiles/2503.03863.md|2503.03863]]
### AI Justification:
This paper is relevant to your interests in theoretical astrophysics and plasma physics as it explores the magnetic dynamics of coronal mass ejections (CMEs) and employs a magnetic flux rope model, closely related to your focus on "magnetic field amplification" and "force interactions shaping magnetic dynamics." The study highlights the predictive capabilities of magnetic field behaviors, which aligns well with your interest in the interactions and structures of magnetic fields within plasma environments at varied scales.
# (131/382) http://arxiv.org/pdf/2503.03711v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The shear Alfvén continuum of quasisymmetric stellarators. Part 1. Perturbation theory
**Elizabeth J. Paul,Abdullah Hyder,Eduardo Rodriguez,Rogerio Jorge,Alexey Knyazev**


#mhd
### Abstract:
The shear Alfv\en wave (SAW) continuum plays a critical role in the stability of energetic particle-driven Alfv\{e}n eigenmodes. We develop a theoretical framework to analyze the SAW continuum in three-dimensional quasisymmetric magnetic fields, focusing on its implications for stellarator design. By employing a near-axis model and degenerate perturbation theory, the continuum equation is solved, highlighting unique features in 3D configurations, such as the interactions between spectral gaps. Numerical examples validate the theory, demonstrating the impact of flux surface shaping and quasisymmetric field properties on continuum structure. The results provide insights into optimizing stellarator configurations to minimize resonance-driven losses of energetic particles. This work establishes a basis for incorporating Alfv\enic stability considerations into the stellarator design process, demonstrated through optimization of a quasihelical configuration to avoid high-frequency spectral gaps.


![[mdfiles/2503.03711.md|2503.03711]]
### AI Justification:
This paper is relevant to your research interests as it explores the theoretical underpinnings of shear Alfvén waves in quasisymmetric magnetic fields, which connects to your focus on "how magnetic fields behave, interact, and amplify" in plasma environments. Furthermore, the implications for stellarator design and stability relate to "interactions between magnetic, gravitational, and thermal forces," providing valuable insights into optimizing magnetic configurations that could inform your studies on magnetic dynamics across scales.
# (132/382) http://arxiv.org/pdf/2503.02066v1


### Rating: 7.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 75%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Global Hall-magnetohydrodynamic simulations of transition disks
**Eleftheria Sarafidou,Oliver Gressel,Barbara Ercolano**


#mhd
### Abstract:
Context. Transition disks (TDs) are a type of protoplanetary disk characterized by a central dust and gas cavity. The processes behind how these cavities are formed and maintained, along with their observed high accretion rates of $10^{-8} -10^{-7} \, M_{\odot} \, \mathrm{yr}^{-1}$ , continue to be subjects of active research. Aims. This work aims to investigate how the inclusion of the Hall effect (HE) alongside Ohmic resistivity (OR) and ambipolar diffusion (AD) affects the structure of the TD. Of key interest is the dynamical evolution of the cavity and whether it can indeed produce transonic accretion, as predicted by theoretical models in order to account for the observed high accretion rates despite the inner disks low density. Methods. We present our results of 2D axisymmetric global radiation magnetohydrodynamic (MHD) simulations of TDs for which all three non-ideal MHD effects are accounted. We used the NIRVANA-III fluid code and initialized our model with a disk cavity reaching up to $R=8~\mathrm{au}$ with a density contrast of $10^5$ . We performed three runs, one with only OR and AD, and one for each of the two configurations that arise when additionally including the HE, that is, with the field aligned (anti-aligned) with respect to the rotation axis. Results. For all three runs, our models maintain an intact inner cavity and an outer standard disk. MHD winds are launched both from the cavity and from the disk. Notably, when the HE is included, ring-like structures develop within the cavity. We moreover obtain accretion rates of $3 - 8 \times 10^{-8} \, M_{\odot} \, \mathrm{yr}^{-1}$ , comparable to typical values seen in full disks. Importantly, we clearly observe transonic accretion ( $v_{\mathrm{acc}} \gtrsim c_{s}$ ) in the cavity. Additionally, outward magnetic flux transport occurs in all three runs.


![[mdfiles/2503.02066.md|2503.02066]]
### AI Justification:
This paper is relevant to your research interests as it investigates how the Hall effect and other non-ideal MHD effects influence magnetic field dynamics within the context of transition disks. The focus on “MHD winds” and “outward magnetic flux transport” aligns well with your interest in “magnetic field amplification” and the interactions between magnetic and accretion processes in plasma environments, providing insights that may inform your studies on the interaction of magnetic fields across various scales.
# (133/382) http://arxiv.org/pdf/2504.02469v2


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### An MHD Simulation of the Possible Modulations of Stellar CMEs Radio Observations by an Exoplanetary Magnetosphere
**Soumitra Hazra,Ofer Cohen,Igor V. Sokolov**


#mhd
### Abstract:
Type II radio bursts are the indicator of adverse space weather in a stellar system. These radio bursts are the consequence of shock wave acceleration due to the coronal mass ejection (CME). In this study, we conduct a series of magnetohydrodynamic (MHD) simulations of CME-driven star-planet systems to investigate how close-in exoplanets modulate radio burst characteristics. We use a model for the stellar wind with a close-in exoplanet, and a CME model based on the eruption of a flux rope. We are able to generate synthetic radio burst images from our MHD simulations. We find that radio burst like phenomena is most likely to be observed for moderately active solar like stars and close-in exoplanetary systems have significant influence on the nature of radio burst spectrum. We find that when the exoplanets magnetic field is relatively weak, its magnetosphere compresses the CME plasma, increasing local density and shifting the radio emission to higher frequencies. Conversely, a strong planetary magnetic field results in a large magnetosphere that prevents effective CME-shock development, producing weaker radio emission concentrated at lower frequencies, particularly at the flanks of the CME. For highly active solar-like stars, strong overlying stellar magnetic fields suppress the CME shock, greatly diminishing radio burst visibility. For HD 189733 (moderate stellar field), only intensity difference is visible when the CME arrives the planet. We also do not find significant modulation in the radio emission by a close-in exoplanet system when the stellar magnetic field is complex. In summary, our findings highlight that the nature of the radio burst spectrum is strongly dependent on both the topology of the stellar magnetic field and the magnetic strength of close-in exoplanets.


![[mdfiles/2504.02469.md|2504.02469]]
### AI Justification:
The paper addresses magnetic dynamics in the context of coronal mass ejections (CMEs) and their interaction with exoplanetary magnetospheres, which relates to your interest in "magnetic field amplification" and "force interactions shaping magnetic dynamics." The use of magnetohydrodynamic (MHD) simulations to explore how "the topology of the stellar magnetic field" influences the behavior of magnetic fields aligns with your research on scale-dependent magnetic structuring and complex dynamics within plasma environments.
# (134/382) http://arxiv.org/pdf/2504.20962v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A Novel Method of Modeling Extended Emission of Compact Jets... Application to Swift J1727.8-1613
**Andrzej A. Zdziarski,Callan M. Wood,Francesco Carotenuto**


#mhd
### Abstract:
Flat radio spectra of compact jets launched by both supermassive and stellar-mass black holes are explained by an interplay of self-absorbed synchrotron emission up to some distance along the jet and optically thin synchrotron at larger distances (Blandford & Konigl 1979). Their spatial structure is usually studied using core shifts, in which the position of the peak (core) of the emission depends on the frequency. Here, we propose a novel method to fit the spatial dependence of the flux density at a given frequency of the jet and counterjet (when observed) using the theoretical spatial dependencies, which we provide as simple analytical formulae. We apply our method to the spatial structure of the jets in the luminous hard spectral state of the black-hole X-ray binary Swift J1727.8--1613. It was the most resolved continuous jet from an X-ray binary ever observed. We find that the observed approaching jet is significantly intrinsically stronger than the receding one, which we attribute to an increase in the emission of both jets with time (observationally confirmed), together with the light travel effect, causing the receding jet to be observed at an earlier epoch than the approaching one. The jets are relatively slow, with the velocity $\sim(0.3$ -- $0.4)c$ . Our findings imply that the magnetic field strength increased with time. Also, the magnetic flux is much lower than in jets launched by `Magnetically Arrested Disks. Our method is general, and we propose that it be applied to jets launched by stellar-mass and supermassive black holes.


![[mdfiles/2504.20962.md|2504.20962]]
### AI Justification:
This paper has relevance to your interests as it discusses the dynamics of jets produced by black holes, specifically addressing how magnetic fields evolve and amplify in astrophysical plasmas. The phrase "the magnetic field strength increased with time" directly pertains to your focus on "Magnetic Field Amplification" and suggests insights into the force interactions that shape magnetic dynamics in complex environments, potentially informing your studies on scale-dependent structuring in plasma scenarios.
# (135/382) http://arxiv.org/pdf/2504.20856v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Wave Particle Interaction in the Upstream of ICME Shocks
**Shanwlee Sow Mondal,Aveek Sarkar,Sofiane Bourouaine**


#mhd
### Abstract:
Shocks associated with Interplanetary Coronal Mass Ejections are known to energize charged particles and give rise to Solar Energetic Particles. Many of these energetic particles move ahead of the shock to create a foreshock region. The foreshock region primarily consists of solar wind plasma, exhibiting turbulent velocity and magnetic fields. Such turbulent behavior results from inherent solar wind turbulence modified by energetic particles. We analyze magnetic field data from six such ICME shocks observed by the Wind spacecraft. The analysis of the shock upstream shows that the magnetic power spectral density (PSD) maintains a power-law slope of $-5/3$ . We also identify clear intermittent peaks in the PSD. After characterizing these peaks, we investigate various possibilities for their generation. Our analysis indicates that these peaks in the PSD are due to the resonant interaction of Alfv\en waves with the bulk solar wind protons and protons with energy up to $10$ ~keV. However, evidence of Alfv\en wave interaction with highly energetic protons is not evident in our analysis, and we anticipate that such evidence is obscured by the prevailing solar wind turbulence in the shock upstream.


![[mdfiles/2504.20856.md|2504.20856]]
### AI Justification:
This paper has relevance to your research interests, particularly in the way it examines "turbulent velocity and magnetic fields" in the context of Interplanetary Coronal Mass Ejections (ICMEs), which aligns with your focus on "emergent magnetic dynamics in turbulent plasmas." The analysis of the magnetic power spectral density (PSD) and its implications for wave-particle interactions also provides insight into "magnetic field amplification" through resonant interactions, indicating a connection to your interest in how magnetic fields evolve within plasma environments.
# (136/382) http://arxiv.org/pdf/2504.17931v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Formation of chromospheric fan-shaped jets through magnetic reconnection
**Annu Bura,Tanmoy Samanta,Avijeet Prasad,Ronald L. Moore,Alphonse C. Sterling,Vasyl Yurchyshyn,...**


#mhd
### Abstract:
Recurrent chromospheric fan-shaped jets highlight the highly dynamic nature of the solar atmosphere. They have been named as light walls or peacock jets in high-resolution observations. In this study, we examined the underlying mechanisms responsible for the generation of recurrent chromospheric fan-shaped jets utilizing data from the Goode Solar Telescope (GST) at Big Bear Solar Observatory, along with data from the Atmospheric Imaging Assembly (AIA) and the Helioseismic and Magnetic Imager (HMI) onboard the Solar Dynamic Observatory (SDO). These jets appear as dark elongated structures in H $\alpha$ wing images, persist for over an hour, and are located in the intergranular lanes between a pair of same-polarity sunspots. Our analysis reveals that magnetic flux cancellation at the jet base plays a crucial role in their formation. HMI line-of-sight magnetograms show a gradual decrease in opposite-polarity fluxes spanning the sequence of jets in H $\alpha$ - 0.8 angstrom images, suggesting that recurrent magnetic reconnection, likely driven by recurrent miniature flux-rope eruptions that are built up and triggered by flux cancellation, powers these jets. Additionally, magnetic field extrapolations reveal a 3D magnetic null-point topology at the jet formation site $\sim$ 1.25 Mm height. Furthermore, we observed strong brightening in AIA 304 angstrom channel above the neutral line. Based on our observations and extrapolation results, we propose that these recurrent chromospheric fan-shaped jets align with the minifilament eruption model previously proposed for coronal jets. Though our study focuses on fan-shaped jets in between same-polarity sunspots, similar mechanism might be responsible for light bridge-associated fan-shaped jets.


![[mdfiles/2504.17931.md|2504.17931]]
### AI Justification:
This paper is relevant to your research interests as it explores **magnetic reconnection** and its role in the generation of **recurrent magnetic jets**, which relates to your focus on **magnetic field amplification** and the interactions of magnetic forces in plasma environments. The study's emphasis on **3D magnetic null-point topology** and the dynamics in the solar atmosphere also provides insights into **scale-dependent magnetic structuring**, relevant to understanding magnetic fields across various astrophysical contexts.
# (137/382) http://arxiv.org/pdf/2504.17774v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Collisionless ion-electron energy exchange in magnetized shocks
**Y. Zhang,P. V. Heuer,H. Wen,J. R. Davies,C. Ren,D. B. Schaeffer,...**


#mhd
### Abstract:
Energy partition between ions and electrons in collisionless shocks has long been an unsolved fundamental physical problem. We show that kinetic simulations of moderate Alfv\enic Mach number, magnetized, collisionless shocks reveal rapid, faster-than-Coulomb, energy exchange between ions and electrons when the plasma is sufficiently magnetized. Using kinetic and multi-fluid models with counter-streaming ions, we identify resonances between electron whistler and ion magnetohydrodynamic waves that account for this rapid energy exchange.


![[mdfiles/2504.17774.md|2504.17774]]
### AI Justification:
This paper is relevant to your research interests as it investigates the behavior of magnetic fields in collisionless shocks, which aligns with your focus on "magnetic dynamics of plasmas." The mention of "kinetic simulations" and interactions between waves suggests an exploration of how "force interactions" shape magnetic dynamics, offering insights that could relate to your study of emergent behaviors in turbulent plasma environments.
# (138/382) http://arxiv.org/pdf/2504.16849v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetorotational instability in a solar mean-field dynamo
**Axel Brandenburg,Gustav Larsson,Fabio Del Sordo,Petri J. Kapyla**


#mhd
### Abstract:
We address the question whether the magneto-rotational instability (MRI) can operate in the near-surface shear layer (NSSL) of the Sun and how it affects the interaction with the dynamo process. Using hydromagnetic mean-field simulations of $\alpha\Omega$ -type dynamos in rotating shearing-periodic boxes, we show that for negative shear, the MRI can operate above a certain critical shear parameter. This parameter scales inversely with the equipartition magnetic field strength above which $\alpha$ quenching set in. Like the usual $\Omega$ effect, the MRI produces toroidal magnetic field, but in our Cartesian cases it is found to reduce the resulting magnetic field strength and thus to suppress the dynamo process. In view of the application to the solar NSSL, we conclude that the turbulent magnetic diffusivity may be too large for the MRI to be excited and that therefore only the standard $\Omega$ effect is expected to operate.


![[mdfiles/2504.16849.md|2504.16849]]
### AI Justification:
This paper relates well to my research interests in theoretical astrophysics and plasma physics, particularly in its exploration of the magnetorotational instability (MRI) as it interfaces with dynamo processes, which aligns with my focus on "magnetic field amplification" driven by "dynamos." Additionally, the investigation of how the “interaction with the dynamo process” affects magnetic field dynamics could provide insights into the "emergent magnetic dynamics in turbulent plasmas" that I am seeking in my work.
# (139/382) http://arxiv.org/pdf/2504.16681v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On the origin of long-term modulation in the Suns magnetic activity cycle
**Chitradeep Saha,Suprabha Mukhopadhyay,Dibyendu Nandy**


#mhd
### Abstract:
One of the most striking manifestations of orderly behavior emerging out of complex interactions in any astrophysical system is the 11-year cycle of sunspots. However, direct sunspot observations and reconstructions of long-term solar activity clearly exhibit amplitude fluctuations beyond the decadal timescale -- which may be termed as supradecadal modulation. Whether this long-term modulation in the Suns magnetic activity results from nonlinear mechanisms or stochastic perturbations remains controversial and a matter of active debate. Utilizing multi-millennial scale kinematic dynamo simulations based on the Babcock-Leighton paradigm -- in the likely (near-critical) regime of operation of the solar dynamo -- we demonstrate that this supradecadal modulation in solar activity cannot be explained by nonlinear mechanisms alone; stochastic forcing is essential for the manifestation of observed long-term fluctuations in the near-critical dynamo regime. Our findings substantiate some independent observational and theoretical investigations, and provide additional insights into temporal dynamics associated with a plethora of natural phenomena in astronomy and planetary systems arising from weakly nonlinear, non-deterministic processes.


![[mdfiles/2504.16681.md|2504.16681]]
### AI Justification:
The paper is relevant to my research interests concerning "magnetic dynamics" and "mechanisms driving the amplification and evolution of magnetic fields," as it explores the "11-year cycle of sunspots" and its connections to "nonlinear mechanisms" and "stochastic perturbations." Additionally, its focus on "multi-millennial scale kinematic dynamo simulations" aligns well with my interest in theoretical models and simulations investigating magnetic behavior on various temporal scales.
# (140/382) http://arxiv.org/pdf/2504.16619v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### An efficient method for magnetic field extrapolation based on a family of analytical three-dimensional magnetohydrostatic equilibria
**Lilli Nadol,Thomas Neukirch**


#mhd
### Abstract:
With current observational methods it is not possible to directly measure the magnetic field in the solar corona with sufficient accuracy. Therefore, coronal magnetic field models have to rely on extrapolation methods using photospheric magnetograms as boundary conditions. In recent years, due to the increased resolution of observations and the need to resolve non-force-free lower regions of the solar atmosphere, there have been increased efforts to use magnetohydrostatic (MHS) field models instead of force-free extrapolation methods. Although numerical methods to calculateMHS solutions can deal with non-linear problems and hence provide more accurate models, analytical three-dimensional MHS equilibria can also be used as a numerically relatively `cheap` complementary method. In this paper, we present an extrapolation method based on a family of analytical MHS equilibria that allows for a transition from a non-force-free region to a force-free region. We demonstrate how asymptotic forms of the solutions can help to increase the numerical efficiency of the method. Through both artificial boundary condition testing and a first application to observational


![[mdfiles/2504.16619.md|2504.16619]]
### AI Justification:
This paper presents an analytical approach to magnetic field extrapolation that aligns with my interest in the "behavior, interaction, and amplification" of magnetic fields in astrophysical plasmas, particularly in non-force-free environments. The focus on "magnetohydrostatic equilibria" and exploring transitions between force-free and non-force-free regions provides valuable insights into the complexities of magnetic dynamics within plasma environments.
# (141/382) http://arxiv.org/pdf/2504.16019v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Cosmic Clues from Amaterasu... Blazar-Driven Ultrahigh-Energy Cosmic Rays?
**Saikat Das,Srijita Hazra,Nayantara Gupta**


#mhd
### Abstract:
The detection of the 244 EeV Amaterasu event by the Telescope Array, one of the most energetic ultrahigh-energy cosmic rays (UHECRs; $E\gtrsim0.1$ EeV) observed to date, invites scrutiny of its potential source. We investigate whether the nearby blazar PKS 1717+177, located within $2.5^\circ$ of the reconstructed arrival direction, could explain the event under a proton-primary hypothesis. Using a one-zone jet model, we fit the multi-wavelength spectral energy distribution of the source, incorporating both leptonic and hadronic cascade emission from photohadronic interactions. Our model supports a cosmic-ray origin of the very-high-energy ( $E\gtrsim 100$ GeV) $\gamma$ -ray flux and predicts a subdominant neutrino flux, an order of magnitude lower than from TXS 0506+056. Under Lorentz invariance violation, protons above a specific energy can propagate over hundreds of Mpc without significant energy loss for certain parameter choices. In such a scenario, our analysis indicates negligible deflection in the Galactic magnetic field, implying a strong extragalactic magnetic field, placing a lower bound on the field strength. Our findings provide a compelling multi-messenger framework linking UHECRs, $\gamma$ rays, and neutrinos and motivate targeted searches by current and future high-energy neutrino telescopes during increased $\gamma$ -ray or X-ray activity of this blazar.


![[mdfiles/2504.16019.md|2504.16019]]
### AI Justification:
The paper offers insights into the significance of magnetic fields in the propagation of ultrahigh-energy cosmic rays (UHECRs), specifically noting "negligible deflection in the Galactic magnetic field" which aligns with your interest in how "magnetic fields behave, interact, and amplify" across various scales. Additionally, the analysis of extragalactic magnetic fields providing a "lower bound on the field strength" could enhance your understanding of the "force interactions shaping magnetic dynamics" in plasma environments.
# (142/382) http://arxiv.org/pdf/2504.15890v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Tracing the imprints of large-scale magnetized structure on $γ$ rays from GRB 221009A
**Saikat Das,Soebur Razzaque,Nestor Mirabal,Nicola Omodei,Kohta Murase,Israel Martinez-Castellanos**


#mhd
### Abstract:
We search for possible GeV-TeV gamma-ray imprints of ultrahigh-energy (UHE; $\gtrsim 0.1$ EeV) cosmic ray (CR) acceleration in the large-scale structures surrounding the brightest gamma-ray burst (GRB) explosion, GRB 221009A. Using 1.25 years of post-event Fermi Large Area Telescope (LAT) data, we construct a 1 GeV - 1 TeV test-statistic (TS) map within 15 Mpc of the burst. We identify two peaks in the TS map with TS $\geq 9$ . The most significant peak, J1911.8+2044, exhibits gamma-ray emission in pre-burst LAT data. The other peak, J1913.2+1901, coincides with a 664.6 GeV photon recorded $\sim191.9$ days after the GRB trigger and located at about $0.75^{\circ}$ from the GRB localization. The per-photon 95% containment angle for the LAT is about $0.25^{\circ}$ in the 100 GeV - 1 TeV energy range. We explore two possible origins for the $\gamma$ -ray emission... (1) UHECRs from GRB 221009A propagating through a magnetized cosmological volume in its vicinity, and (2) UHE or very-high-energy (VHE; $\gtrsim 100$ GeV) $\gamma$ -ray emission from GRB 221009A, propagating in the same volume. In both cases, electromagnetic cascade emission is induced in the structured region embedding the burst. If any TS features are related to large-scale imprints induced by cosmic rays, it might be further evidence that GRB 221009A accelerated UHECRs. However, our results show that alternative scenarios without invoking UHECRs cannot be ruled out, and the observed high-energy photon could be unrelated to GRB 221009A.


![[mdfiles/2504.15890.md|2504.15890]]
### AI Justification:
This paper is relevant to your research interests as it explores the effects of large-scale magnetized structures on gamma-ray emissions in the context of cosmic ray acceleration, which aligns with your focus on "magnetic dynamics of plasmas in the interstellar medium." Additionally, the authors examine potential interactions between electromagnetic fields and cosmic rays, mirroring your interest in "force interactions shaping magnetic dynamics" and how these may influence the behavior of magnetic fields within plasma environments.
# (143/382) http://arxiv.org/pdf/2504.15684v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Hydrogen-poor Superluminous Supernovae with Bumpy Light Curves Powered by Precessing Magnetars
**Biao Zhang,Long Li,Zi-Gao Dai,Shu-Qing Zhong**


#mhd
### Abstract:
Recent observations and statistical studies have revealed that a significant fraction of hydrogen-poor superluminous supernovae (SLSNe-I) exhibit light curves that deviate from the smooth evolution predicted by the magnetar-powered model, instead showing one or more bumps after the primary peak. However, the formation mechanisms of these post-peak bumps remain a matter of debate. Furthermore, previous studies employing the magnetar-powered model have typically assumed a fixed magnetic inclination angle and neglected the effects of magnetar precession. However, recent research has shown that the precession of newborn magnetars forming during the collapse of massive stars causes the magnetic inclination angle to evolve over time, thereby influencing magnetic dipole radiation. In this paper, therefore, we incorporate the effects of magnetar precession into the magnetar-powered model to develop the precessing magnetar-powered model. Using this model, we successfully reproduce the multi-band light curves of 6 selected representative SLSNe-I with post-peak bumps. Moreover, the derived model parameters fall within the typical parameter range for SLSNe-I. By combining the precessing magnetars in SLSNe-I and long GRBs, we find that the ellipticity of magnetars is related to the dipole magnetic field strength, which may suggest a common origin for the two phenomena. Our work provides a potential explanation for the origin of post-peak bumps in SLSNe-I and offers evidence for the early precession of newborn magnetars formed in supernova explosions.


![[mdfiles/2504.15684.md|2504.15684]]
### AI Justification:
This paper explores the dynamics of magnetic fields through the lens of magnetar precession in superluminous supernovae, which touches upon the interaction of magnetic, gravitational, and thermal forces—elements relevant to your research on "how magnetic fields behave and interact across various scales." The focus on the "dipole magnetic field strength" and its relation to structural formation aligns well with your interest in "how magnetic fields organize and shape structures" in astrophysical plasmas.
# (144/382) http://arxiv.org/pdf/2504.14876v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Initiation Route of Coronal Mass Ejections... II. The Role of Filament Mass
**Chen Xing,Xin Cheng,Guillaume Aulanier,Mingde Ding**


#mhd
### Abstract:
The thorough understanding on the initiation of coronal mass ejections (CMEs), which is manifested as a slow rise of pre-eruptive structures before the impulsive ejection in kinematics, is the key for forecasting the solar eruptions. In our previous work, we showed that the slow rise of a hot flux rope with coronal mass density is caused by the moderate magnetic reconnection occurring in the hyperbolic flux tube (HFT) combined with the torus instability. However, it remains unclear how the initiation process varies when a filament is present in the pre-eruptive flux rope. In this work, we reveal the complete initiation route of a CME containing filament mass with a state-of-the-art full-magnetohydrodynamics simulation. The comprehensive analyses show that the filament mass has an important impact on the CME initiation through triggering and driving the slow rise of flux rope with its drainage, besides the contributions of HFT reconnection and torus instability. Finally, in combination with our previous work, we propose that the enhanced drainage of filament mass and various features related to the HFT reconnection, such as, the split of pre-eruptive structure and the pre-flare loops and X-ray emissions, can serve as the precursors of CME initiation in observations.


![[mdfiles/2504.14876.md|2504.14876]]
### AI Justification:
This paper is relevant to your research because it investigates the interplay between magnetic dynamics and coronal mass ejections (CMEs), focusing on how “the filament mass has an important impact on the CME initiation” through magnetic reconnection and torus instability. The emphasis on a full-magnetohydrodynamics simulation aligns with your interest in “theoretical models, simulations, and studies” that examine “the complex, multi-scale dynamics of magnetic fields in plasma environments,” specifically in the context of magnetic interactions and their implications in astrophysical settings.
# (145/382) http://arxiv.org/pdf/2504.12213v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetically driven outflows in 3D common-envelope evolution of massive stars
**Marco Vetter,Friedrich K. Roepke,Fabian R. N. Schneider,Rudiger Pakmor,Sebastian Ohlmann,Javier Moran-Fraile,...**


#mhd
### Abstract:
Recent three-dimensional magnetohydrodynamical simulations of the common-envelope interaction revealed the self-consistent formation of bipolar magnetically driven outflows launched from a toroidal structure resembling a circumbinary disk. So far, the dynamical impact of bipolar outflows on the common-envelope phase remains uncertain and we aim to quantify its importance. We illustrate the impact on common-envelope evolution by comparing two simulations -- one with magnetic fields and one without -- using the three-dimensional moving-mesh hydrodynamics code AREPO. We focus on the specific case of a $10 M_\odot$ red supergiant star with a $5 M_\odot$ black hole companion. By the end of the magnetohydrodynamic simulations (after $\sim 1220 $ orbits of the core binary system), about $ 6.4 \%$ of the envelope mass is ejected via the bipolar outflow, contributing to angular momentum extraction from the disk structure and core binary. The resulting enhanced torques reduce the final orbital separation by about $24 \%$ compared to the hydrodynamical scenario, while the overall envelope ejection remains dominated by recombination-driven equatorial winds. We analyze field amplification and outflow launching mechanisms, confirming consistency with earlier studies... magnetic fields are amplified by shear flows, and outflows are launched by a magneto-centrifugal process, supported by local shocks and magnetic pressure gradients. These outflows originate from $\sim 1.1$ times the orbital separation. We conclude that the magnetically driven outflows and their role in the dynamical interaction are a universal aspect, and we further propose an adaptation of the $\alpha_\mathrm{CE}$ -formalism by adjusting the final orbital energy with a factor of $1+ M_\mathrm{out}/\mu$ , where $M_\mathrm{out}$ is the mass ejected through the outflows and $\mu$ the reduced mass of the core binary. (abridged)


![[mdfiles/2504.12213.md|2504.12213]]
### AI Justification:
The paper is relevant to your research interests as it explores the "magnetic field amplification" in the context of magnetohydrodynamical simulations related to massive stars, which directly ties into your focus on how dynamical processes influence the evolution of magnetic fields in astrophysical plasmas. Additionally, the paper discusses "force interactions" and the impact of "bipolar magnetically driven outflows," which align with your investigation of how such forces shape magnetic dynamics within plasma environments.
# (146/382) http://arxiv.org/pdf/2504.11173v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Bright bursts with sub-millisecond structures of FRB 20230607A in a highly magnetized environment
**DeJiang Zhou,J. L. Han,Bing Zhang,WeiWei Zhu,Wei-yang Wang,Yuan-Pei Yang,...**


#mhd
### Abstract:
We report the observations of a repeating FRB 20230607A for 15.6 hours spanning 16 months using the Five-hundred-meter Aperture Spherical Radio Telescope (FAST) with the detection of 565 bursts. We present three bright bursts with detailed temporal/spectral structures. We also report that one burst carries a narrow component with a width of only 0.3 ms, which is surrounded by broader components. This suggests that repeaters can make both narrow and broad components in one burst. With the narrow spike, we precisely measure the dispersion measure (DM) of $362.85 \pm 0.15 \;{\rm pc\,cm^{-3}}$ and the Faraday rotation measures (RMs) of and $-12249.0\pm 1.5 \; {\rm rad\,m^{-2}}$ . We also analyze the statistical distribution of the burst parameters, including waiting times, temporal widths, central frequencies and frequency widths, fluences and energies, all showing typical distributions of known active repeaters. In particular, most bursts show narrow spectra with $\Delta\nu/\nu_0 = 0.125\pm 0.001$ . This fact, together with the narrow 0.3 ms spike, strongly suggests a magnetospheric origin of the FRB emission. Based on a predicted correlation between RM and the luminosity of a persistent radio source (PRS) by Yang et al., we predict that PRS should have a specific luminosity of the order of $10^{29} \ {\rm erg \ s^{-1} \ Hz^{-1}}$ and encourage a search for such a PRS.


![[mdfiles/2504.11173.md|2504.11173]]
### AI Justification:
This paper is relevant to your research on magnetic dynamics in the interstellar medium as it discusses the Faraday rotation measures (RMs) in the context of fast radio bursts (FRBs), implicating the "highly magnetized environment" in which these dynamics occur. The mention of a "magnetospheric origin of the FRB emission" aligns with your interest in how magnetic fields behave and interact within plasmas, suggesting potential insights into the amplification and structuring of these fields.
# (147/382) http://arxiv.org/pdf/2504.09501v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Energy-resolved polarisation study of the Crab Nebula with IXPE
**Wenhao Wei,Fei Xie,Fabio La Monaca,Wei Deng,Mingyu Ge,Kuan Liu,...**


#mhd
### Abstract:
This work presents a new detailed study on the energy-dependent variation in the X-ray polarisation of the Crab Pulsar Wind Nebula (PWN), obtained using data from the Imaging X-ray Polarimetry Explorer (IXPE). For the entire PWN, we observed a linear variation in polarisation degree (PD), and detected the rotation of the polarisation angle (PA) with the energy at higher than 99.9999\% of the confidence level. This energy-dependent polarisation variation is in line with the indication found in Vela PWN by IXPE, and it can be interpreted as the emitting region of the polarised photons shrinks with increasing energy, leading to higher PD because they are less influenced by the turbulence of the magnetic field. We compared the IXPE polarisation results with those of other hard X-ray/gamma observatories (PoGO+, Intregral, AstroSat) for the PWN, finding the same trend from soft-X to hard-X with the PD increasing with the energy and the PA approaching the pulsars spin axis. In fact, in this wide energy band, the fitting results show an energy trend for the PA compatible with the estimated pulsars spin axis within 3 $\sigma$ of confidence level.


![[mdfiles/2504.09501.md|2504.09501]]
### AI Justification:
The paper examines the energy-dependent variation in X-ray polarization within the Crab Pulsar Wind Nebula, which offers insights into how magnetic fields interact with turbulent environments. This directly relates to my research interest in "magnetic dynamics of plasmas" as it discusses the "variation in polarisation degree" and implications on magnetic structuring influenced by turbulence, aligning with my focus on "emergent magnetic dynamics in turbulent plasmas."
# (148/382) http://arxiv.org/pdf/2503.03344v3


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quantitative Magnetohydrodynamic Modelling of Flux Pumping in ASDEX Upgrade
**Haowei Zhang,Matthias Holzl,Isabel Krebs,Andreas Burckhart,Alexander Bock,Sibylle Gunter,...**


#mhd
### Abstract:
The sawtooth-free hybrid scenario has been achieved recently in ASDEX Upgrade (AUG) with applied non-inductive current sources and auxiliary heating [A. Burckhart et al 2023 Nucl. Fusion 63 126056]. Control experiments in AUG suggest that the self-regulating magnetic flux pumping mechanism, characterized by anomalous current redistribution, is responsible for clamping the central safety factor (q_0) close to unity, thereby preventing the sawtooth onset. This work presents a numerical and theoretical investigation of flux pumping in the AUG hybrid scenario based on the two-temperature, visco-resistive, full magnetohydrodynamic (MHD) model with the JOREK code. To quantitatively model the flux pumping, we choose realistic parameters, plasma configurations, and source terms based on AUG experiments. During the initial saturation stage of the unstable 1/1 quasi-interchange mode (on millisecond timescales), q_0 exhibits fast under-damped oscillation and reaches a value closer to unity, which is attributed to the self-regulation of core plasma and the fast dynamo effect on the order of V/m. On the longer resistive diffusion timescale of seconds, the slow negative dynamo effect on the order of mV/m induced by the 1/1 MHD instability plays an effective role in flux pumping, which provides quantitative agreement with experimental observations for the first time. The final saturated 1/1 MHD instability exhibits features of the quasi-interchange mode and tearing mode, and the associated convective plasma flow velocity is a few m/s. The toroidal negative electric field from the slow dynamo dominantly offsets the positive current drive and continuously redistributes the current density and pressure. As a result, q_0 is maintained close to unity due to the low-shear profiles of current density and pressure in the plasma core, and the system enters a sawtooth-free and quasi-stationary helical state.


![[mdfiles/2503.03344.md|2503.03344]]
### AI Justification:
The paper is relevant to your research interests as it explores "self-regulating magnetic flux pumping" within a magnetohydrodynamic context, which aligns with your focus on "magnetic field amplification" and "the interactions between magnetic, gravitational, and thermal forces." Additionally, the investigation of "flux pumping" and its dependence on "dynamo effects" presents valuable insights into the dynamics of magnetic fields in plasma environments, particularly as it relates to "the complex, multi-scale dynamics of magnetic fields."
# (149/382) http://arxiv.org/pdf/2504.07937v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Baryon asymmetry constraints on magnetic field from the Electroweak epoch
**T. Boyer,A. Neronov**


#mhd
### Abstract:
Decay of helical (hyper)magnetic fields that may have been present in the Universe during the Electroweak epoch can contribute to generation of the baryon asymmetry of the Universe. We revise constraints on the strength and correlation length of such fields from the requirement that their decay does not lead to over-production of the baryon asymmetry. We show that the helical fields with strength down to 1e-5 of the maximal possible strength during the Electroweak epoch should have had their correlation at least ~1e-6 of the Hubble radius during this epoch. For weaker fields this lower bound on the correlation length relaxes proportionally to the square of magnetic field strength. A field with parameters saturating the bound may actually be responsible for the baryon asymmetry observed today. We show that relic of such a field, surviving in the present day Universe in the form of intergalactic magnetic field detectable with Cherenkov Telescope Array Observatory, may have the strength up to 10-100 pG and can have parameters needed to affect the cosmological recombination and relax the Hubble tension. We also show that there is no constraint on the parameters of helical or non-helical magnetic fields stemming from the requirement that the baryon isocurvature perturbations produced by such fields during the Electroweak epoch are within the observational limits.


![[mdfiles/2504.07937.md|2504.07937]]
### AI Justification:
This paper is relevant to your interests as it explores "helical (hyper)magnetic fields" and their implications for the "baryon asymmetry of the Universe," which can intersect with your focus on "magnetic field amplification" and "force interactions." Additionally, the discussion of "magnetic fields" during the Electroweak epoch and potential observational implications aligns with your research on the behavior and evolution of magnetic fields in plasmas across various scales.
# (150/382) http://arxiv.org/pdf/2504.06170v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Investigating Embedded Structures and Gas Kinematics in the IRDC Hosting Bubble N59-North
**A. K. Maity,L. K. Dewangan,O. R. Jadhav,Saurabh Sharma,Ram Kesh Yadav,Y. Fukui,...**


#mhd
### Abstract:
We present a multi-wavelength study of an extended area hosting the bubble N59-North to explore the physical processes driving massive star formation (MSF). The Spitzer 8 $\mu$ m image reveals an elongated/filamentary infrared-dark cloud (length $\sim$ 28 pc) associated with N59-North, which contains several protostars and seven ATLASGAL dust clumps at the same distance. The existence of this filament is confirmed through $^{13}$ CO and NH $_3$ molecular line data in a velocity range of [95, 106] km s $^{-1}$ . All dust clumps satisfy Kauffmann & Pillais condition for MSF. Using Spitzer 8 $\mu$ m image, a new embedded hub-filament system candidate (C-HFS) is investigated toward the ATLASGAL clump, located near the filaments central region. MeerKAT 1.3 GHz continuum emission, detected for the first time toward C-HFS, reveals an ultracompact HII region driven by a B2-type star, suggesting an early stage of HFS with minimal feedback from the young massive star. The comparison of the position-velocity (PV) and position-position-velocity (PPV) diagrams with existing theoretical models suggests that rotation, central collapse, and end-dominated collapse are not responsible for the observed gas motion in the filament. The PPV diagram indicates the expansion of N59-North by revealing blue- and red-shifted gas velocities at the edge of the bubble. Based on comparisons with magnetohydrodynamic simulations, this study suggests that cloud-cloud collision (CCC) led to the formation of the filament, likely giving it a conical structure with gas converging toward its central region, where C-HFS is located. Overall, the study supports multi-scale filamentary mass accretion for MSF, likely triggered by CCC.


![[mdfiles/2504.06170.md|2504.06170]]
### AI Justification:
This paper presents a multi-wavelength study that investigates the dynamics of gas within a filamentary structure, showcasing the interactions involved in massive star formation. The mention of "magnetohydrodynamic simulations" and the exploration of cloud-cloud collision (CCC) in shaping filamentary structures indicates a direct relevance to your interests in "magnetic dynamics" and "scale-dependent magnetic structuring" in plasmas.
# (151/382) http://arxiv.org/pdf/2504.06086v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Investigating an Erupting Metric-decimetric Radio Depression and its Physical Origin
**B. T. Wang,X. Cheng,J. Y. Yan,C. Xing,W. T. Fu,L. Wu,...**


#mhd
### Abstract:
We present direct metric-decimetric radio imaging observations of a fascinating quiescent filament eruption on 2024 March 17 using data from the DAocheng Radio Telescope (DART), with a combination of the Solar Dynamics Observatory and the Chinese Ha Solar Explorer. At the radio band, even though the filament is difficult to identify in its early phase, it rapidly became distinct and formed a continuous loop-like dark structure during the eruption, i.e., so-called radio depression. Compared with the fragmentation of the erupting filament observed at the Ha and EUV bands, the radio depression appeared more coherently. Based on synthetic radio images from a three-dimensional magnetohydrodynamics (MHD) simulation of a flux-rope-filament eruption, it is suggested that the radio depression originates from the absorption of cold and dense materials within the erupting flux rope to the background emission. The absorption seems to be stronger than that at the Ha and EUV bands, thus leading to their apparent discrepancies. Moreover, the radio depression is also found to occupy the lower part but not the whole body of the flux rope.


![[mdfiles/2504.06086.md|2504.06086]]
### AI Justification:
This paper is relevant to your research interests as it explores "magnetic dynamics" through the context of a filament eruption and presents a "three-dimensional magnetohydrodynamics (MHD) simulation," which aligns well with your focus on theoretical models and simulations in plasma environments. The investigation of "radio depression" as it relates to the behavior of magnetic fields in plasma, particularly through interactions involving "absorption of cold and dense materials," may provide insights into the mechanisms that drive magnetic field amplification and their complex structuring in interstellar environments.
# (152/382) http://arxiv.org/pdf/2504.04926v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Coupling of Alfvén and magnetosonic waves in rotating Hall magnetoplasmas
**A. P. Misra,R. Dey,V. Krishan**


#mhd
### Abstract:
We study the linear theory of magnetohydrodynamic (MHD) waves, namely the Alfv{\e}n and the fast and slow magnetosonic modes in a rotating Hall-MHD plasma with the effects of the obliqueness of the external magnetic field and the Coriolis force and show that these waves can be coupled either by the influence of the Coriolis force or the Hall effects. To this end, we derive a general form of the linear dispersion relation for these coupled modes by the combined influence of the Coriolis force and the Hall effects and analyze numerically their characteristics in three different plasma- $\beta$ regimes... $\beta\sim1$ , $\beta>1$ , and $\beta<1$ , including some particular cases. We show that while the coupling between the Alfv{\e}n and the fast magnetosonic modes is strong in the low- $\beta$ $(\beta\lesssim1)$ regime and the wave dispersion appears in the form of a thumb curve, in the high- $\beta~(\beta>1)$ regime, the strong coupling can occur between the Alfv{\e}n and the slow magnetosonic modes and the dispersion appears in the form of a teardrop curve. Switching of the coupling in the regime of $\beta\sim1$ can occur, i.e., instead of a thumb curve, a teardrop curve appears when the obliqueness of propagation and rotational angle are close to $70^\circ$ or more (but less than $90^\circ$ ). Implications of our results to solar and fusion plasmas are briefly discussed.


![[mdfiles/2504.04926.md|2504.04926]]
### AI Justification:
This paper is relevant to your research interests as it examines the coupling of Alfvén and magnetosonic waves within the framework of magnetohydrodynamics (MHD), which directly relates to your focus on "magnetic dynamics of plasmas" and the interactions shaped by "magnetic, gravitational, and thermal forces." Furthermore, the investigation into how different plasma $\beta$ regimes affect wave behavior aligns with your emphasis on the "scale-dependent magnetic structuring" in interstellar plasma environments, particularly in the context of forces that shape magnetic fields.
# (153/382) http://arxiv.org/pdf/2504.03308v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Launching of asymmetric outflows from the star-disk magnetosphere
**Miljenko Cemeljic,Aleksandra Kotek,Wlodek Kluzniak**


#mhd
### Abstract:
In resistive and viscous magnetohydrodynamical simulations, we obtain axial outflows launched from the innermost magnetosphere of a star-disk system. The launched outflows are found to be asymmetric. We find the part of the parameter space corresponding to quasi-stationary axial outflows and compute the mass load and angular momentum flux in such outflows. We display the obtained geometry of the solutions and measure the speed of propagation and rotation of the obtained axial outflows.


![[mdfiles/2504.03308.md|2504.03308]]
### AI Justification:
This paper is relevant to your research interests as it delves into magnetohydrodynamical simulations that explore the behavior of outflows in a star-disk magnetosphere, which aligns with your focus on the "interactions between magnetic, gravitational, and thermal forces." The investigation into "asymmetric outflows" and their dynamics may provide insights into "emergent magnetic dynamics in turbulent plasmas" relevant to your study of the interstellar medium.
# (154/382) http://arxiv.org/pdf/2504.03335v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Evolution of interacting coronal mass ejections driving the great geomagnetic storm on 10 May 2024
**Soumyaranjan Khuntia,Wageesh Mishra,Anjali Agarwal**


#mhd
### Abstract:
The arrival of a series of coronal mass ejections (CMEs) at the Earth resulted in a great geomagnetic storm on 10 May 2024, the strongest storm in the last two decades. We investigate the kinematic and thermal evolution of the successive CMEs to understand their interaction en route to Earth. We attempt to find the dynamics, thermodynamics, and magnetic field signatures of CME-CME interactions. Our focus is to compare the thermal state of CMEs near the Sun and in their post-interaction phase at 1 AU. The 3D kinematics of six identified Earth-directed CMEs were determined using the GCS model. The flux rope internal state (FRIS) model is implemented to estimate the CMEs polytropic index and temperature evolution from their measured kinematics. The thermal states of the interacting CMEs are examined using in-situ at 1 AU. Our study determined the interaction heights of selected CMEs and confirmed their interaction that led to the formation of complex ejecta identified at 1 AU. The plasma, magnetic field, and thermal characteristics of magnetic ejecta (ME) within the complex ejecta and other substructures, such as interaction regions (IRs) within two ME and double flux rope-like structures within a single ME, show the possible signatures of CME-CME interaction in in-situ observations. The FRIS-model-derived thermal states for individual CMEs reveal their diverse thermal evolution near the Sun, with most CMEs transitioning to an isothermal state at 6-9 Rsun, except for CME4, which exhibits an adiabatic state due to a slower expansion rate. The complex ejecta at 1 AU shows a predominant heat-release state in electrons, while the ions show a bimodal distribution of thermal states. On comparing the characteristics of CMEs near the Sun and at 1 AU, we suggest that such one-to-one comparison is difficult due to CME-CME interactions significantly influencing their post-interaction characteristics.


![[mdfiles/2504.03335.md|2504.03335]]
### AI Justification:
This paper examines the dynamics, thermodynamics, and magnetic field signatures resulting from coronal mass ejection (CME) interactions, which is relevant to my research focus on "Magnetic Field Amplification" and "Force Interactions Shaping Magnetic Dynamics" in plasma environments. Although it centers on CMEs rather than interstellar mediums, the study of "CME-CME interactions" and the influence of "magnetic, thermal, and plasma characteristics" provides insights into multi-scale magnetic field behavior that could inform my work on emergent magnetic dynamics in turbulent plasmas.
# (155/382) http://arxiv.org/pdf/2504.02414v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Effective field theory of Plasmas in Podolsky corrected Photonic field
**Prabhat Singh,Punit Kumar**


#mhd
### Abstract:
A theory for abelian plasma permeated by photons has been developed considering QED (quantum electrodynamics) generalized in Podolsky electrodynamics framework for consideration of higher order terms in electromagnetic theory. The theory traces out photonic degrees of freedom in plasma and accounts for plasma dynamics mediated by photons by calculated effective Hamiltonian. New modes of propagation have been predicted along with suppression of fields and collective behaviour. Non-Markovian behaviour is also discovered for plasma states and interactions in finite plasma system. This finds applicability in solid-state plasma, plasma confinement of magnetic and inertial nature, and laser-plasma interaction when theory is reduced to local interactions.


![[mdfiles/2504.02414.md|2504.02414]]
### AI Justification:
This paper is relevant to your interests in theoretical astrophysics and plasma physics as it develops a new framework for plasma dynamics that incorporates magnetic interactions in a photonic context, aligning with your focus on "magnetic dynamics of plasmas in the interstellar medium." The exploration of "new modes of propagation" and "collective behaviour" provides insights into emergent magnetic dynamics, potentially influencing how magnetic fields behave in complex plasma environments.
# (156/382) http://arxiv.org/pdf/2504.02047v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A geometric Particle-In-Cell discretization of the drift-kinetic and fully kinetic Vlasov-Maxwell equations
**Guo Meng,Katharina Kormann,Emil Poulsen,Eric Sonnendrucker**


#mhd
### Abstract:
In this paper, we extend the geometric Particle in Cell framework on dual grids to a gauge-free drift-kinetic Vlasov--Maxwell model and its coupling with the fully kinetic model. We derive a discrete action principle on dual grids for our drift-kinetic model, such that the dynamical system involves only the electric and magnetic fields and not the potentials as most drift-kinetic and gyrokinetic models do. This yields a macroscopic Maxwell equation including polarization and magnetization terms that can be coupled straightforwardly with a fully kinetic model.


![[mdfiles/2504.02047.md|2504.02047]]
### AI Justification:
This paper is relevant to your research interests as it delves into the "drift-kinetic Vlasov-Maxwell model," which touches upon the behavior and interactions of "electric and magnetic fields," a fundamental aspect of the magnetic dynamics of plasmas. Furthermore, the paper's approach to incorporating both drift-kinetic and fully kinetic models may yield insights into "magnetic field amplification" and its implications in astrophysical contexts, aligning with your focus on the complex dynamics in the interstellar medium.
# (157/382) http://arxiv.org/pdf/2504.00093v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Origin of the Cluster of Local Interstellar Clouds
**Catherine Zucker,Seth Redfield,Sara Starecheski,Ralf Konietzka,Jeffrey L. Linsky**


#mhd
### Abstract:
The interstellar medium within $\rm\approx 15 \; pc$ of the Sun consists of a complex of fifteen diffuse, partially ionized clouds. Located within the Local Bubble, these clouds, known as the Cluster of Local Interstellar Clouds (CLIC), constitute the interstellar environment impinging upon our heliosphere. While each individual cloud can be modeled with a distinct velocity vector, the complex demonstrates a coherent bulk motion suggestive of a common origin. Here we examine two theories for the origin of the CLIC... that it formed due to an ionization front associated with nearby Str\`{o}mgren spheres and/or due to a nearby supernova explosion that occurred within the pre-evacuated cavity of the Local Bubble. Tracing back the trajectory of the clouds, we disfavor a purely Str\`{o}mgren sphere origin, given the CLICs position interior to the surface of the most significant nearby Stromgren sphere and its motion transverse to the spheres trajectory. Turning to a supernova origin, we model the formation of the CLIC assuming individual clouds have been swept up over time due to the expansion of a supernova remnant in its pressure-driven snowplow phase. We find that the 3D spatial-dynamical properties of the CLIC can be explained by the most recent supernova that exploded in the nearby Upper Centaurus Lupus cluster $\approx \rm 1.2 \; Myr$ ago and propagated into an ambient density of $n \approx 0.04 \;\rm cm^{-3}$ . Our model predicts that the formation of the individual CLIC clouds occurred progressively over the past $1 \; \rm Myr$ and offers a natural explanation for the observed distribution, column density, temperature, and magnetic field structure of the complex.


![[mdfiles/2504.00093.md|2504.00093]]
### AI Justification:
The paper is relevant to your research interests as it examines the complex dynamics of interstellar medium clouds, particularly addressing the "magnetic field structure" within the context of "pressure-driven" mechanisms. The connection to "supernova explosion" as a shaping force aligns with your interest in "force interactions" that influence magnetic dynamics within plasma environments.
# (158/382) http://arxiv.org/pdf/2503.21032v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic Reconnection in the Plasma Disk at 23 Jupiter Radii
**Jian-zhao Wang,Fran Bagenal,Stefan Eriksson,Robert E. Ergun,Peter A. Delamere,Robert J. Wilson,...**


#mhd
### Abstract:
A key open question in astrophysics is how plasma is transported within strongly magnetized, rapidly rotating systems. Magnetic reconnection and flux tube interchange are possible mechanisms, with Jupiter serving as the best local analog for distant systems. However, magnetic reconnection at Jupiter remains poorly understood. A key indicator of active magnetic reconnection is the ion diffusion region, but its detection at Jupiter has remained unconfirmed. Here, we report a unique magnetic reconnection event in Jupiters inner magnetosphere that presents the first detection of an ion diffusion region. We provide evidence that this event involves localized flux tube interchange motion driven by centrifugal forces, which occurs inside a thin current sheet formed by the collision and twisting of two distinct flux tubes. This study provides new insights into Io-genic plasma transport at Jupiter and the unique role of magnetic reconnection in rapidly rotating systems, two key unresolved questions.


![[mdfiles/2503.21032.md|2503.21032]]
### AI Justification:
This paper is relevant to your research interests as it examines "magnetic reconnection" within Jupiter's magnetosphere, connecting to your focus on "magnetic field amplification" and "force interactions shaping magnetic dynamics." Additionally, the discussion on how plasma transport is influenced by "centrifugal forces" and the dynamics within the "thin current sheet" aligns with your interest in the interactions between magnetic, gravitational, and thermal forces within plasma environments.
# (159/382) http://arxiv.org/pdf/2503.17208v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Hamiltonian Chaos... From Galactic Dynamics to Plasma Physics
**Henok Tenaw Moges**


#mhd
### Abstract:
The primary focus of this thesis is the numerical investigation of chaos in Hamiltonian models describing charged particle orbits in plasma, star motions in barred galaxies, and orbits diffusion in multidimensional maps. We systematically explore the interplay between magnetic and kinetic chaos in toroidal fusion plasmas, where non-axisymmetric perturbations disrupt smooth magnetic flux surfaces, generating complex particle trajectories. Using the Generalized Alignment Index (GALI) method, we efficiently quantify chaos, compare the behavior of magnetic field lines and particle orbits, visualize the radial distribution of chaotic regions, and offer GALI as a valuable tool for studying plasma physics dynamics. We also study the evolution of phase space structures in a 3D barred galactic potential, following successive 2D and 3D pitchfork and period-doubling bifurcations of periodic orbits. By employing the `color and rotation technique to visualize the systems 4D Poincar\e surface of sections, we reveal distinct structural patterns. We further investigate the long-term diffusion transport and chaos properties of single and coupled standard maps, focusing on parameters inducing anomalous diffusion through accelerator modes exhibiting ballistic transport. Using different ensembles of initial conditions in chaotic regions influenced by these modes, we examine asymptotic diffusion rates and time scales, identifying conditions suppressing anomalous transport and leading to long-term convergence to normal diffusion across coupled maps. Lastly, we perform the first comprehensive investigation into the GALI indices for various attractors in continuous and discrete-time dissipative systems, extending the methods application to non-Hamiltonian systems. A key aspect of our work involves analyzing and comparing GALIs with Lyapunov Exponents for systems exhibiting hyperchaotic motion.


![[mdfiles/2503.17208.md|2503.17208]]
### AI Justification:
The paper presents a numerical investigation of chaos in Hamiltonian models that also examines charged particle orbits within plasmas, which aligns with your interest in "how magnetic fields behave, interact, and amplify across various scales" and "the interactions between magnetic, gravitational, and thermal forces." Additionally, the exploration of complex particle trajectories due to magnetic disruptions in plasma environments contributes to your research focus on "emergent magnetic dynamics in turbulent plasmas."
# (160/382) http://arxiv.org/pdf/2503.15689v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Velocity and Density Fluctuations in the Quiet Sun Corona
**Michael Hahn,Xiangrong Fu,Stefan J. Hofmeister,Yifan Huang,Alexandros Koukras,Daniel Wolf Savin**


#mhd
### Abstract:
We investigate the properties and relationship between Doppler-velocity fluctuations and intensity fluctuations in the off-limb quiet Sun corona. These are expected to reflect the properties of Alfvenic and compressive waves, respectively. The data come from the Coronal Multichannel Polarimeter (COMP). These data were studied using spectral methods to estimate the power spectra, amplitudes, perpendicular correlation lengths, phases, trajectories, dispersion relations, and propagation speeds of both types of fluctuations. We find that most velocity fluctuations are due to Alfvenic waves, but that intensity fluctuations come from a variety of sources, likely including fast and slow mode waves, as well as aperiodic variations. The relation between the velocity and intensity fluctuations differs depending on the underlying coronal structure. On short closed loops, the velocity and intensity fluctuations have similar power spectra and speeds. In contrast, on longer nearly radial trajectories, the velocity and intensity fluctuations have different power spectra, with the velocity fluctuations propagating at much faster speeds than the intensity fluctuations. Considering the temperature sensitivity of COMP, these longer structures are more likely to be closed fields lines of the quiet Sun rather than cooler open field lines. That is, we find the character of the interactions of Alfvenic waves and density fluctuations depends on the length of the magnetic loop on which they are traveling.


![[mdfiles/2503.15689.md|2503.15689]]
### AI Justification:
The paper is relevant to my interests as it investigates the properties of Alfvenic waves within the solar corona, contributing to the understanding of "magnetic dynamics" and how "magnetic fields behave" in plasma environments. Additionally, it touches on "density fluctuations" and their relations to "velocity fluctuations," aligning with my focus on the interactions between forces that shape magnetic field behavior in astrophysical plasmas.
# (161/382) http://arxiv.org/pdf/2503.15430v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Turbulent power... a discriminator between sheaths and CMEs
**Deep Ghuge,Debesh Bhattacharjee,Prasad Subramanian**


#mhd
### Abstract:
Solar coronal mass ejections (CMEs) directed at the Earth often drive large geomagnetic storms. Here we use velocity, magnetic field and proton density data from 152 CMEs that were sampled in-situ at 1 AU by the WIND spacecraft. We Fourier analyze fluctuations of these quantities in the quiescent pre-CME solar wind, sheath and magnetic cloud. We quantify the extent by which the power in turbulent (magnetic field, velocity and density) fluctuations in the sheath exceeds that in the solar wind background and in the magnetic cloud. For instance, the mean value of the power per unit volume in magnetic field fluctuations in the sheath is 76.7 times that in the solar wind background, while the mean value of the power per unit mass in velocity fluctuations in the sheath is 9 times that in the magnetic cloud. Our detailed results show that the turbulent fluctuation power is a useful discriminator between the ambient solar wind background, sheaths and magnetic clouds and can serve as a useful input for space weather prediction.


![[mdfiles/2503.15430.md|2503.15430]]
### AI Justification:
The paper discusses the role of turbulent fluctuations in the magnetic field and plasma dynamics during coronal mass ejections (CMEs), which aligns with my interest in "Magnetic Field Amplification" and "Emergent Magnetic Dynamics in Turbulent Plasmas." Furthermore, the use of Fourier analysis to quantify fluctuations provides insight into how "magnetic fields behave, interact, and amplify," which is critical for understanding the dynamics within plasma environments.
# (162/382) http://arxiv.org/pdf/2503.15396v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On the linear structure of the interlaced Alfvén vortices in the tail of Uranus at solstice
**Filippo Pantellini**


#mhd
### Abstract:
Incompressible vortex flow are observed in a large variety of astrophysical plasmas such as the convection zone and the atmosphere of stars, in astrophysical jets in stellar winds and in planetary magnetospheres. More specifically, magnetohydrodynamic (MHD) simulations have shown that two large scale interlaced Alfv\enic vortices structure the magnetic tail of Uranus at solstice time. Assuming identical vortices, we compute the general linear structure of the flow near their centers within the frame of ideal MHD. We then use the analytic results to interpret and qualify the vortices observed in a 3D MHD simulation of a fast rotating Uranus-type planet.


![[mdfiles/2503.15396.md|2503.15396]]
### AI Justification:
This paper is relevant to my research interests in theoretical astrophysics and plasma physics, as it explores "magnetohydrodynamic (MHD) simulations" that provide insight into the "magnetic tail of Uranus," which relates to the dynamics and behavior of magnetic fields in plasma environments. Additionally, the focus on "interlaced Alfvén vortices" closely aligns with my interest in how magnetic fields interact and organize structures, potentially providing valuable information on "scale-dependent magnetic structuring" in astrophysical systems.
# (163/382) http://arxiv.org/pdf/2503.13827v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Anisotropic Turbulent Flows Observed in Above the Loop-top Regions During Solar Flares
**Xiaoyan Xie,Chengcai Shen,Katharine Reeves,Bin Chen,Xiaocan Li,Fan Guo,...**


#mhd
### Abstract:
Solar flare above-the-loop-top (ALT) regions are vital for understanding solar eruptions and fundamental processes in plasma physics. Recent advances in 3D MHD simulations have revealed unprecedented details on turbulent flows and MHD instabilities in flare ALT regions. Here, for the first time, we examine the observable anisotropic properties of turbulent flows in ALT by applying a flow-tracking algorithm on narrow-band Extreme Ultraviolet (EUV) images that are observed from the face-on viewing perspective. First, the results quantitatively confirm the previous observation that vertical motions dominate and that the anisotropic flows are widely distributed in the entire ALT region with the contribution from both upflows and downflows. Second, the anisotropy shows height-dependent features, with the most substantial anisotropy appearing at a certain middle height in ALT, which agrees well with the MHD modeling results where turbulent flows are caused by Rayleigh-Taylor-type instabilities in the ALT region. Finally, our finding suggests that supra-arcade downflows (SADs), the most prominently visible dynamical structures in ALT regions, are only one aspect of turbulent flows. Among these turbulent flows, we also report the anti-sunward-moving underdense flows that might develop due to MHD instabilities, as suggested by previous three-dimensional flare models. Our results indicate that the entire flare fan displays group behavior of turbulent flows where the observational bright spikes and relatively dark SADs exhibit similar anisotropic characteristics.


![[mdfiles/2503.13827.md|2503.13827]]
### AI Justification:
This paper is relevant to my interests as it explores "turbulent flows" and "MHD instabilities," which relate to my focus on the "emergent magnetic dynamics in turbulent plasmas." Additionally, the examination of "anisotropic flows" that arise from "Rayleigh-Taylor-type instabilities" aligns with my research on the interactions between magnetic and thermal forces within plasma environments.
# (164/382) http://arxiv.org/pdf/2503.08887v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On the million-degree signature of spicules
**Souvik Bose,Jayant Joshi,Paola Testa,Bart De Pontieu**


#mhd
### Abstract:
Spicules have often been proposed as substantial contributors toward the mass and energy balance of the solar corona. While their transition region (TR) counterpart has unequivocally been established over the past decade, the observations concerning the coronal contribution of spicules have often been contested. This is mainly attributed to the lack of adequate coordinated observations, their small spatial scales, highly dynamic nature, and complex multi-thermal evolution, which are often observed at the limit of our current observational facilities. Therefore, it remains unclear how much heating occurs in association with spicules to coronal temperatures. In this study, we use coordinated high-resolution observations of the solar chromosphere, TR, and corona of a quiet Sun region and a coronal hole with the Interface Region Imaging Spectrograph (IRIS) and the Atmospheric Imaging Assembly (AIA) to investigate the (lower) coronal ( $\sim$ 1MK) emission associated with spicules. We perform differential emission measure (DEM) analysis on the AIA passbands using basis pursuit and a newly developed technique based on Tikhonov regularization to probe the thermal structure of the spicular environment at coronal temperatures. We find that the EM maps at 1 MK reveal the presence of ubiquitous, small-scale jets with a clear spatio-temporal coherence with the spicules observed in the IRIS/TR passband. Detailed space-time analysis of the chromospheric, TR, and EM maps show unambiguous evidence of rapidly outward propagating spicules with strong emission (2--3 times higher than the background) at 1 MK. Our findings are consistent with previously reported MHD simulations that show heating to coronal temperatures associated with spicules.


![[mdfiles/2503.08887.md|2503.08887]]
### AI Justification:
This paper is relevant to your interests as it discusses the dynamics of spicules and their role in the thermal structure of the solar corona, which may relate to your interest in "magnetic dynamics of plasmas in the interstellar medium." The use of "MHD simulations" and the investigation of "rapidly outward propagating spicules" could offer insights into "magnetic field amplification" and the interactions between magnetic fields and thermal forces in similar plasma environments.
# (165/382) http://arxiv.org/pdf/2503.07787v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### L1448 IRS3B... Dust Polarization Aligned with Spiral Features, Tracing Gas Flows
**Leslie W. Looney,Zhe-Yu Daniel Lin,Zhi-Yun Li,John J. Tobin,Martin Radecki,Syzygy Butte,...**


#mhd
### Abstract:
Circumstellar disk dust polarization in the (sub)millimeter is, for the most part, not from dust grain alignment with magnetic fields but rather indicative of a combination of dust self-scattering with a yet unknown alignment mechanism that is consistent with mechanical alignment. While the observational evidence for scattering has been well established, that for mechanical alignment is less so. Circum-multiple dust structures in protostellar systems provide a unique environment to probe different polarization alignment mechanisms. We present ALMA Band 4 and Band 7 polarization observations toward the multiple young system L1448 IRS3B. The polarization in the two Bands is consistent with each other, presenting multiple polarization morphologies. On the size scale of the inner envelope surrounding the circum-multiple disk, the polarization is consistent with magnetic field dust grain alignment. On the very small scale of compact circumstellar regions, we see polarization that is consistent with scattering around source a and c, which are likely the most optically thick components. Finally, we see polarization that is consistent with mechanical alignment of dust grains along the spiral dust structures, which would suggest that the dust is tracing the relative gas flow along the spiral arms. If the gas-flow dust grain alignment mechanism is dominant in these cases, disk dust polarization may provide a direct probe of the small-scale kinematics of the gas flow relative to the dust grains.


![[mdfiles/2503.07787.md|2503.07787]]
### AI Justification:
This paper is relevant to your interests as it discusses the alignment of dust polarization with gas flows, which relates to the interaction of magnetic fields with plasma dynamics as seen in "mechanical alignment" and “scattering.” Additionally, the mention of "magnetic field dust grain alignment" addresses your focus on magnetic field amplification and evolution, thereby offering insights into the interactions and behaviors of magnetic fields in astrophysical plasmas.
# (166/382) http://arxiv.org/pdf/2503.07255v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Testing for Markovian character of transfer of fluctuations in solar wind turbulence on kinetic scales
**Dariusz Wojcik,Wieslaw M. Macek**


#mhd
### Abstract:
We apply statistical analysis to search for processes responsible for turbulence in physical systems. In our previous studies, we have shown that solar wind turbulence in the inertial range of large magnetohydrodynamic scales exhibits Markov properties. We have recently extended this approach on much smaller kinetic scales. Here we are testing for the Markovian character of stochastic processes in a kinetic regime based on magnetic field and velocity fluctuations in the solar wind, measured onboard the Magnetospheric Multiscale (MMS) mission... behind the bow shock, inside the magnetosheath, and near the magnetopause. We have verified that the Chapman-Kolmogorov necessary conditions for Markov processes is satisfied for local transfer of energy between the magnetic and velocity fields also on kinetic scales. We have confirmed that for magnetic fluctuations, the first Kramers-Moyal coefficient is linear, while the second term is quadratic, corresponding to drift and diffusion processes in the resulting Fokker-Planck equation. It means that magnetic self-similar turbulence is described by generalized Ornstein-Uhlenbeck processes. We show that for the magnetic case, the Fokker-Planck equation leads to the probability density functions of the kappa distributions, which exhibit global universal scale invariance with a linear scaling and lack of intermittency. On the contrary, for velocity fluctuations, higher order Kramers-Moyal coefficients should be taken into account and hence scale invariance is not observed. However, the nonextensity parameter in Tsallis entropy provides a robust measure of the departure of the system from equilibrium. The obtained results are important for a better understanding of the physical mechanism governing turbulent systems in space and laboratory.


![[mdfiles/2503.07255.md|2503.07255]]
### AI Justification:
This paper is relevant to your research interests as it investigates "turbulence in physical systems," particularly focusing on "magnetic fluctuations" within the context of solar wind dynamics, which aligns with your interest in the interactions between magnetic fields and turbulence. Moreover, the exploration of "kinetic scales" and the statistical analysis of magnetic and velocity fluctuations may offer insights into "scale-dependent magnetic structuring" relevant to astrophysical plasmas in the interstellar medium.
# (167/382) http://arxiv.org/pdf/2503.07205v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### X-ray and radio data obtained by XMM-Newton and VLA constrain the stellar wind of the magnetic quasi-Wolf-Rayet star in HD45166
**P. Leto,L. M. Oskinova,T. Shenar,G. A. Wade,S. Owocki,C. S. Buemi,...**


#mhd
### Abstract:
Recently, a powerful magnetic field was discovered in the hot helium star classified as a quasi-Wolf-Rayet star of ~2Msun, member of the HD45166 system. Upon its explosion as a core-collapse supernova, it is expected to produce a strongly magnetic neutron star, a magnetar. Among the key parameters governing the pre-supernova evolution is the amount of mass lost via stellar wind. However, the magnetic nature of this helium star is expected to affect its stellar wind making the estimation of the wind parameters uncertain. We report the first observations of HD45166 in X-rays with the XMM-Newton telescope and in radio with the VLA interferometer array. By placing the observation results in a theoretical framework, we aim to provide a reliable estimate of the wind strength of the magnetic qWR star. The X-ray properties are explained in the framework of the MCWS scenario, and the semi-analytic XADM model is applied to reproduce the X-ray emission. The thermal radio emission of the wind and its absorption effect on possible gyro-synchrotron emission from the underlying dipolar magnetosphere, sampled in 3D, are computed by integrating the radiative transfer equation. We did not detect radio emissions, this enabled us to set sensitive upper limits on the radio luminosity. The magnetic qWR star is a slow rotator, comparison with models reveals that the possible acceleration mechanisms occurring within its dynamical magnetosphere are not as efficient as in fast-rotating magnetic ApBp-type stars. In contrast, the system is detected in X-rays with log(L_X/L_bol)~ -5.6. Using suitable models, we constrain the mass lost from this magnetic quasi-Wolf-Rayet star as dot{M}~3e-10 Msun/yr. This novel empirical estimate of the mass-loss rate in a ~2Msun helium star confirms that it maintains super-Chandrasekhar mass till collapse and can produce a magnetar as its final evolutionary product.


![[mdfiles/2503.07205.md|2503.07205]]
### AI Justification:
The paper provides insights into the behavior of magnetic fields in the stellar wind of a magnetic quasi-Wolf-Rayet star, which aligns with my interest in "how magnetic fields behave, interact, and amplify" in various astrophysical contexts, particularly the role of magnetic dynamics in stellar evolution. Moreover, by examining how the "magnetic nature" of the helium star affects its stellar wind and estimating the "mass-loss rate," the paper addresses critical aspects of "force interactions shaping magnetic dynamics" and offers valuable theoretical frameworks relevant to my research in plasma environments.
# (168/382) http://arxiv.org/pdf/2503.01969v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### What Drives Cluster Cool-Core Transformations? A Population Level Analysis of TNG-Cluster
**Katrin Lehle,Dylan Nelson,Annalisa Pillepich**


#mhd
### Abstract:
In this study, we examine the frequency and physical drivers of transformations from cool-core (CC) to non-cool-core (NCC) clusters, and vice versa, in a sample of 352 massive galaxy clusters (M_vir = 10^14-15.3 M_sun) from the TNG-Cluster magnetohydrodynamical cosmological simulation of galaxies. By identifying transformations based on the evolution of central entropy and focusing on z<2.5, we find that clusters frequently undergo such events, depending on their assembly and supermassive black hole histories. On average, clusters experience 2 to 3 transformations. Transformations can occur in both directions and can be temporary, but those to higher entropy cores, i.e. in the direction from CC to NCC states, are the vast majority. CC phases are shorter than NCC phases, and thus overall the TNG-Cluster population forms with low-entropy cores and moves towards NCC states with time. We study the role that mergers play in driving transformations, and find that mergers within ~1Gyr prior to a transformation toward higher (but not lower) entropy cores occur statistically more often than in a random control sample. Most importantly, we find examples of mergers associated with CC disruption regardless of their mass ratio or angular momentum. However, past merger activity is not a good predictor for z=0 CC status, at least based on core entropy, even though clusters undergoing more mergers eventually have the highest core entropy values at z=0. We consider the interplay between AGN feedback and evolving cluster core thermodynamics. We find that core transformations are accompanied by an increase in AGN activity, whereby frequent and repeated (kinetic) energy injections from the central SMBHs can produce a collective, long-term impact on central entropy, ultimately heating cluster cores. Whether such fast-paced periods of AGN activity are triggered by mergers is plausible, but not necessary.


![[mdfiles/2503.01969.md|2503.01969]]
### AI Justification:
This paper is relevant to your research interests as it examines the "transformations from cool-core (CC) to non-cool-core (NCC) clusters," which aligns with your focus on how "magnetic fields behave, interact, and amplify" in plasma environments, particularly in massive galaxy clusters. Additionally, the mention of "mergers" and their impact on "central entropy" relates to your interest in "force interactions" and how these dynamics shape magnetic behaviors within astrophysical plasmas.
# (169/382) http://arxiv.org/pdf/2503.02105v1


### Rating: 7/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 70%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### NASA Innovative Advanced Concepts Phase I Final Report -- A Lunar Long-Baseline UV/Optical Imaging Interferometer... Artemis-enabled Stellar Imager (AeSI)
**Kenneth G. Carpenter,Tabetha Boyajian,Derek Buzasi,Jim Clark,Michelle Creech-Eakman,Bruce Dean,...**


#mhd
### Abstract:
This report presents the findings of a NIAC Phase I feasibility study for the Artemis-enabled Stellar Imager (AeSI), a proposed high-resolution, UV/Optical interferometer designed for deployment on the lunar surface. Its primary science goal is to image the surfaces and interiors of stars with unprecedented detail, revealing new details about their magnetic processes and dynamic evolution and enabling the creation of a truly predictive solar/stellar dynamo model. This capability will transform our understanding of stellar physics and has broad applicability across astrophysics, from resolving the cores of Active Galactic Nuclei (AGN) to studying supernovae, planetary nebulae, and the late stages of stellar evolution. By leveraging the stable vacuum environment of the Moon and the infrastructure being established for the Artemis Program, AeSI presents a compelling case for a lunar-based interferometer. In this study, the AeSI Team, working with the NASA Goddard Space Flight Centers Integrated Design Center (IDC), has firmly established the feasibility of building and operating a reconfigurable, dispersed aperture telescope (i.e., an interferometer) on the lunar surface. The collaboration produced a credible Baseline design featuring 15 primary mirrors arranged in an elliptical array with a 1 km major axis, with the potential to expand to 30 mirrors and larger array sizes through staged deployments. Additionally, this study identified numerous opportunities for optimization and the necessary trade studies to refine the design further. These will be pursued in follow-up investigations, such as a NIAC Phase II study, to advance the concept toward implementation.


![[mdfiles/2503.02105.md|2503.02105]]
### AI Justification:
This paper is relevant to your interests in theoretical astrophysics and the dynamics of magnetic fields within plasma environments, particularly due to its exploration of "magnetic processes and dynamic evolution" of stellar physics. Additionally, the mention of developing a predictive solar/stellar dynamo model aligns with your focus on "magnetic field amplification" and the complex interactions of forces shaping magnetic dynamics.
# (170/382) http://arxiv.org/pdf/2502.01251v3


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On field line slippage rates in the solar corona
**David MacTaggart**


#mhd
### Abstract:
Magnetic reconnection is one of the fundamental dynamical processes in the solar corona. The method of studying reconnection in active region-scale magnetic fields generally depends on non-local methods (i.e. requiring information across the magnetic field under study) of magnetic topology, such as separatrix skeletons and quasi-separatrix layers. The theory of General Magnetic Reconnection is also non-local, in that its measure of the reconnection rate depends on determining the maxima of integrals along field lines. In this work, we complement the above approaches by introducing a local description of magnetic reconnection, that is one in which information about reconnection at a particular location depends only on quantities at that location. This description connects the concept of the field line slippage rate, relative to ideal motion, to the underlying local geometry of the magnetic field characterized in terms of the Lorentz force and field-aligned current density. It is argued that the dominant non-ideal term for the solar corona, discussed in relation to this new description, is mathematically equivalent to the anomalous resistivity employed by many magnetohrdrodynamic simulations. However, the general application of this new approach is adaptable to the inclusion of other non-ideal terms, which may arise from turbulence modelling or the inclusion of a generalized Ohms law. The approach is illustrated with two examples of coronal magnetic fields related to flux ropes... an analytical model and a nonlinear force-free extrapolation. In terms of the latter, the slippage rate corresponds to the reconnection which would happen if the given (static) force-free equilibrium were the instantaneous form of the magnetic field governed by an Ohms law with non-ideal terms.


![[mdfiles/2502.01251.md|2502.01251]]
### AI Justification:
This paper addresses the dynamics of magnetic reconnection in the solar corona, which relates to your interests in "magnetic dynamics of plasmas" and the mechanisms that govern "magnetic field amplification." Although the focus is specific to the solar corona, its exploration of local geometries and non-ideal terms provides insight into "force interactions shaping magnetic dynamics," which could inform your understanding of similar processes within broader astrophysical settings.
# (171/382) http://arxiv.org/pdf/2503.08889v2


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetohydrodynamic Operating Regimes of Pulsed Plasma Accelerators for Efficient Propellant Utilization
**Ethan Horstman,Adrian Woodley,Thomas C. Underwood**


#mhd
### Abstract:
The presence of magnetohydrodynamic (MHD) acceleration modes in pulsed plasma thrusters has been verified using the magnetic extension of Rankine-Hugoniot theory. However, the impact of initial conditions within the accelerator volume on the formation and structure of these modes remains poorly understood. This work develops a regime map to clarify how key initial conditions - such as propellant gas dynamics, pulse energy, and the timing between propellant injection and discharge initiation - govern transitions between two distinct MHD operating modes, a magneto-detonation and magneto-deflagration, along with an unstable transition regime that connects them. To characterize these regimes, a combination of time-of-flight and thrust stand diagnostics was used to assess their properties, scalability, and structure while operating with air. Time-of-flight measurements reveal that reducing the initial downstream propellant mass ( $m_{dwn}$ ) of air from 120 $\mu$ g to 60 $\mu$ g shifts the thruster from the magneto-detonation to the magneto-deflagration regime, increasing exhaust velocity ( $v_{ex}$ ) from 20 km/s to 55 km/s. In this regime, the thruster exhibits improved propellant utilization as less mass is injected. At a constant 8 kA of peak current, specific impulse (Isp) increases from ~100-2000 s as $m_{dwn}$ decreases from 70 to 10 $\mu$ g, corresponding to an increase in utilization efficiency ( $\eta$ util) from 5% to 35%. Thrust-to-power ratios, measured using a thrust stand, also improve with peak current in the magneto-deflagration regime, increasing from 4.5 mN/kW to 8 mN/kW and 6.7 mN/kW for injected mass bits of 25 $\mu$ g and 50 $\mu$ g, respectively. This work provides critical insights into how the initial conditions in pulsed plasma thrusters dictate the formation of ionization waves, structure of plumes, and the performance of thrusters.


![[mdfiles/2503.08889.md|2503.08889]]
### AI Justification:
This paper discusses magnetohydrodynamic (MHD) operating regimes and their implications for plasma dynamics, which aligns with your interest in how "magnetic fields behave" and "interact" in plasma environments. Furthermore, the analysis of the "formation and structure" of different MHD modes, such as magneto-detonation and magneto-deflagration, contributes valuable insight into the "complex, multi-scale dynamics of magnetic fields" that you are seeking.
# (172/382) http://arxiv.org/pdf/2503.18651v2


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Impact of Accretion on FRB Radiation Mechanisms in Binary Systems... Constraints and Implications
**Gong-Yu Yao,Can-Min Deng**


#mhd
### Abstract:
Fast Radio Bursts (FRBs) are intense, millisecond-duration radio transients that have recently been proposed to arise from coherent radiation mechanisms within the magnetosphere of neutron stars. Observations of repeating FRBs, including periodic activity and large variations in Faraday rotation measures, suggest that these bursts may have binary system origins, with massive companion. In this work, we investigate how accretion from a massive companion influences the FRB radiation within the magnetosphere of the neutron star. Focusing on two widely accepted pulsar-like coherent radiation mechanisms, we establish the parameter space for neutron stars that allows FRB generation, even in the presence of accreted matter. Our analysis shows that coherent curvature radiation is only viable within a narrow range of parameters, while the magnetic reconnection mechanism operates across a broader range. In both cases, the neutron star must possess a strong magnetic field with strength $\gtrsim 10^{13}$ G. These findings at least indicate that the central engines responsible for producing observable FRBs in binary systems are indeed magnetars.


![[mdfiles/2503.18651.md|2503.18651]]
### AI Justification:
The paper investigates the role of magnetic fields in the context of Fast Radio Bursts (FRBs), specifically how "accretion from a massive companion influences the FRB radiation within the magnetosphere of the neutron star," which aligns with my research focus on "magnetic dynamics of plasmas in the interstellar medium." Moreover, it touches on magnetic reconnection mechanisms, highlighting how "the neutron star must possess a strong magnetic field," which connects to my interest in understanding the amplification and structure of magnetic fields in plasma environments.
# (173/382) http://arxiv.org/pdf/2504.14144v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### 3D PIC Study of Magnetic Field Effects on Hall Thruster Electron Drift Instability
**KunPeng Zhong,Demai Zeng,Yinjian Zhao,Daren Yu**


#mhd
### Abstract:
To fully characterize electron drift instability, a critical phenomenon governing electron transport in Hall thrusters, large-scale three-dimensional (3D) particle-in-cell (PIC) simulations are essential, as the instability inherently exhibits 3D features. While prior 3D PIC studies of this instability exist, their setups remain oversimplified to mitigate computational costs, often employing analytical approximations for ionization and magnetic fields. Notably, these models typically assume a purely radial magnetic field, significantly deviating from real thruster configurations. This work presents the first 3D PIC study incorporating realistic magnetic fields with both radial and axial components, coupled with a Monte Carlo collision model for ionization and a self-consistent fluid solver for neutral gas density. These advancements enable a systematic investigation of magnetic field effects on electron drift instability. Results demonstrate that both the spatial configuration and strength of the magnetic field profoundly influence instability dynamics.


![[mdfiles/2504.14144.md|2504.14144]]
### AI Justification:
The paper presents a 3D PIC study that explores the effects of realistic magnetic fields on electron drift instability in Hall thrusters, aligning with your interest in "magnetic dynamics of plasmas" and the "interaction between magnetic forces" within these environments. Although the focus is on a specific application rather than the broader astrophysical context, the results indicate how magnetic field configurations influence dynamics, showcasing a relevant aspect of how magnetic fields behave in plasma systems.
# (174/382) http://arxiv.org/pdf/2504.21857v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Transverse waves observed in a fibril with the MiHI prototype
**E. Petrova,T. Van Doorsselaere,M. van Noort,D. Berghmans,J. S. Castellanos Duran**


#mhd
### Abstract:
Context. Fine-scale structures of the solar chromosphere, particularly fibrils, are known to host various types of magnetohydrodynamic (MHD) waves that can transport energy to the corona. In particular, absorption features observed in the H{\alpha} channel have been widely detected that exhibit transverse oscillations. Aims. We aimed to detect a high-frequency transverse oscillation in fibrils. Methods. We conducted a case study on a high-frequency transverse oscillation in a chromospheric fibril. A chromospheric fibril was observed on 24 August 2018, in the H{\alpha} spectral line, with the prototype Microlensed Hyperspectral Imager (MiHI) at the Swedish 1- meter Solar Telescope. The MiHI instrument is an integral field spectrograph capable of achieving ultra-high resolution simultaneously in the spatial, temporal, and spectral domains. Results. The detected oscillation characteristics include a period of 15 s and a displacement amplitude of 42 km. Using the bisector method, we derived Doppler velocities and determined that the polarisation of the oscillation was elliptical. Conclusions. The energy contained in the oscillation ranges from 390 to 2300 W/m2, which is not sufficient to balance radiative losses of the chromosphere.


![[mdfiles/2504.21857.md|2504.21857]]
### AI Justification:
This paper is relevant to your research interests as it explores magnetohydrodynamic (MHD) waves within a plasma environment; specifically, it examines transverse oscillations in solar chromospheric fibrils, which relates to your focus on the dynamics of magnetic fields in astrophysical plasmas. The identification of oscillation characteristics and their implications on energy transport could provide insights into magnetic dynamics and force interactions in the interstellar medium, thereby offering valuable data for your interest in magnetic field amplification and scale-dependent structuring.
# (175/382) http://arxiv.org/pdf/2504.10965v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Investigating the light curve variation of magnetic white dwarfs induced by the axion-photon conversion
**Hao-Chen Tian,Zhao-Yang Wang,Yun-Feng Liang,Zhao-Wei Du**


#mhd
### Abstract:
Axion-photon oscillation refers to the process of mutual conversion between photons and axions when they propagate in a magnetic field. This process depends on the strength of the background magnetic field, and magnetic white dwarfs provide a natural laboratory for testing this process. In this work, we study the behavior of axion-photon oscillation near magnetic white dwarfs... as the magnetic white dwarf rotates, its magnetic field structure rotates accordingly, causing a periodic change of the magnetic field along the path of photons. These variations affect the axion-photon oscillation process experienced by the photons emitted from the white dwarf, thereby inducing a periodic modulation in the intensity and polarization of the white dwarfs thermal emission that we observe. Our study focuses on the impact of axion effects on the observed light curve variation and conducts a detailed investigation through numerical calculations. Using the light curve data of the white dwarf PG1015+014 obtained from the observations by the Jacobus Kapteyn Telescope, which has a photometric precision of $\sim1\%$ , we derive the constraints on axion parameters. In the axion mass range of $\lesssim10^{-8}\,{\rm eV}$ , the 95\% credible interval upper limit of the axion-photon coupling $g_{a\gamma\gamma}$ is constrained to $<8.1 \times 10^{-12} \mathrm{GeV^{-1}}$ .


![[mdfiles/2504.10965.md|2504.10965]]
### AI Justification:
The paper is somewhat relevant to your research focus as it investigates the behavior of magnetic fields in a specific astrophysical context—magnetic white dwarfs—and examines the impact of these fields on photon-axion oscillation. Although it does delve into magnetic dynamics, it primarily addresses axion impacts rather than the broader aspects of magnetic field amplification and interactions with plasma as defined in your interests.
# (176/382) http://arxiv.org/pdf/2504.09898v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Milky Way Project MOBStIRS... Parametrizing Infrared Stellar-Wind Bow Shock Morphologies with Citizen Science
**Angelica S. Whisnant,Matthew S. Povich,Nikhil Patten,Henry A. Kobulnicky**


#mhd
### Abstract:
Mass-loss influences stellar evolution, especially for massive stars with strong winds. Stellar wind bow shock nebulae driven by Galactic OB stars can be used to measure mass-loss rates ( $\dot{M}$ ). The standoff distance ( $R_{0}$ ) between the star and the bow shock is set by momentum flux balance between the stellar wind and the surrounding interstellar medium (ISM). We created the Milky Way Project... MOBStIRS (Mass-loss rates for OB Stars driving IR bow Shocks) using the online Zooniverse citizen science platform. We enlisted several hundred students to measure $R_0$ and two other projected shape parameters for 764 cataloged IR bow shocks. MOBStIRS incorporated 1528 JPEG cutout images produced from Spitzer GLIMPSE and MIPSGAL survey data. Measurements were aggregated to compute shape parameters for each bow shock image deemed high-quality by participants. The average statistical uncertainty on $R_0$ is $12.5\%$ but varies from ${<}5\%$ to ${\sim}40\%$ among individual bow shocks, contributing significantly to the total error budget of $\dot{M}$ . The derived nebular morphologies agree well with (magneto)hydrodynamic simulations of bow shocks driven by the winds of OB stars moving at $V_a = 10-40~km~s^{-1}$ with respect to the ambient interstellar medium (ISM). A systematic correction to $R_0$ to account for viewing angle appears unnecessary for computing $\dot{M}$ . Slightly more than half of MOBStIRS bow shocks are asymmetric, which could indicate anisotropic stellar winds, ISM clumping on sub-pc scales, time-dependent instabilities, and/or misalignments between the local ISM magnetic field and the star-bow shock axis.


![[mdfiles/2504.09898.md|2504.09898]]
### AI Justification:
The paper is somewhat relevant to your interests in theoretical astrophysics and plasma physics, particularly in its discussion of the interaction between stellar winds and the interstellar medium (ISM), which aligns with your focus on "force interactions shaping magnetic dynamics." Additionally, it touches on the "asymmetric" nature of bow shocks and their implications for understanding the local ISM magnetic field, suggesting connections to your research on how magnetic fields behave and interact within plasma environments.
# (177/382) http://arxiv.org/pdf/2504.10217v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Dissimilar magnetically driven accretion on the components of V4046 Sagittarii
**Kim Pouilly,Marc Audard**


#mhd
### Abstract:
Accretion of pre-main sequence stars (PMS) is a key process in stellar formation, governing mass assembly, influencing angular momentum conservation and stellar internal structure, and shaping disc evolution, which serves as the birthplace of exoplanets. Classical T Tauri stars (cTTSs), low-mass PMS stars actively accreting from a disc, hold a well-described magnetospheric accretion model. Their strong, inclined dipole magnetic fields truncate the disc at a few stellar radii, channelling material along magnetic field lines to fall onto the stellar surface near the dipole pole. However, this paradigm assumes the presence of a single star, and a complete description of the accretion process in multiple systems remains to be achieved. Building on our previous work on DQ Tau and AK Sco, we aim to describe the accretion processes in cTTS binaries, accounting for the influence of stellar magnetic fields. Specifically, we sought to explore how the magnetospheric accretion model of cTTSs can be applied to V4046 Sgr, a spectroscopic binary composed of equal-mass and coeval cTTSs in a circular orbit with synchronous rotation, surrounded by a circumbinary disc. We analysed a time series of ESPaDOnS spectra covering several orbital cycles. A variability analysis was performed on the radial velocities and on the Balmer, He I D3, and Ca II emission lines, which are associated with the accretion process. We identified the secondary as the systems main accretor, operating in an unstable regime. Additionally, we detected an accretion funnel flow connecting the dipole pole of the primary star with a nearby bulk of gas. We concluded that the two components exhibit dissimilar accretion patterns. The primary operates in an `ordered chaotic` regime, where accretion funnel flows and accretion tongues coexist. Conversely, the secondary appears to be in a chaotic regime, with accretion tongues dominating.


![[mdfiles/2504.10217.md|2504.10217]]
### AI Justification:
The paper's exploration of "magnetospheric accretion" and how "stellar magnetic fields" influence the accretion processes in binary systems directly relates to your interest in "magnetic field dynamics" and "force interactions shaping magnetic dynamics." Furthermore, the investigation of accretion patterns and their relation to stellar magnetic fields may offer insights into the "multi-scale dynamics of magnetic fields in plasma environments" you are focused on.
# (178/382) http://arxiv.org/pdf/2504.07353v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### MHD simulations of the slow-rise phase of solar eruptions initiated from a sheared magnetic arcade
**Qingjun Liu,Chaowei Jiang,Zhipeng Liu**


#mhd
### Abstract:
Before solar eruptions, a short-term slow-rise phase is often observed, during which the pre-eruption structure ascends at speeds much greater than the photospheric motions but much less than those of the eruption phase. Numerical magnetohydrodynamic (MHD) simulations of the coronal evolution driven by photospheric motions up to eruptions have been used to explain the slow-rise phase, but their bottom driving speeds are much larger than realistic photospheric values. Therefore, it remains an open question how the excessively fast bottom driving impacts the slow-rise phase. Here we modelled the slow-rise phase before eruption initiated from a continuously sheared magnetic arcade. In particular, we performed a series of experiments with the bottom driving speed unprecedentedly approaching the photospheric value of around $1$ km s $^{-1}$ . The simulations confirmed that the slow-rise phase is an ideal MHD process, i.e., a manifestation of the growing expansion of the sheared arcade in the process of approaching a fully open field state. The overlying field line above the core flux has a slow-rise speed modulated by the driving speeds magnitude but is always over an order of magnitude larger than the driving speed. The core field also expands with speed much higher than the driving speed but much lower than that of the overlying field. By incrementally reducing the bottom-driving speed to realistic photospheric values, we anticipate better matches between the simulated slow-rise speeds and some observed ones.


![[mdfiles/2504.07353.md|2504.07353]]
### AI Justification:
This paper is relevant to your research interests as it utilizes magnetohydrodynamic (MHD) simulations to examine the magnetic dynamics in a plasma environment, specifically focusing on the slow-rise phase of solar eruptions. It touches upon aspects of "magnetic field amplification" and the "interactions between magnetic, gravitational, and thermal forces," which are critical when considering how these dynamics manifest in astrophysical plasmas, aligning well with your emphasis on the behavior of magnetic fields across various scales.
# (179/382) http://arxiv.org/pdf/2504.07218v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Numerical analysis of three-dimensional magnetohydrodynamic effects in an inductively coupled plasma wind tunnel
**Sanjeev Kumar,Alessandro Munafo,Daniel J Bodony,Marco Panesi**


#mhd
### Abstract:
This paper introduces a three-dimensional model for the 350kW Plasmatron X inductively coupled plasma facility at the University of Illinois Urbana-Champaign, designed for testing high-temperature materials. Simulations of the facility have been performed using a three-dimensional, multiphysics computational framework, which reveals pronounced three-dimensional characteristics within the facility. The analysis of the plasma and electromagnetic field in the torch region reveals the influence of the helical coils, which cause a non-axisymmetric distribution of the plasma discharge. Additionally, simulations of the torch-chamber configuration at two operating pressures have been conducted to examine the impact of plasma asymmetry in the torch on jet characteristics in the chamber. The results indicate an unsteady, three-dimensional behavior of the plasma jet at high pressure. Spectral Proper Orthogonal Decomposition (SPOD) has been performed on the unsteady flow field to identify the dominant modes and their associated frequencies. At low pressure, a steady, supersonic, nearly axisymmetric plasma jet forms with consistent flow properties, such as temperature and velocity. However, strong non-equilibrium effects at low pressures lead to substantial deviations in species concentrations from axial symmetry despite having an almost axisymmetric distribution for quantities such as velocity and temperatures.


![[mdfiles/2504.07218.md|2504.07218]]
### AI Justification:
This paper presents a numerical study on the three-dimensional magnetohydrodynamic effects in an inductively coupled plasma, which is relevant to my interest in "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas." The focus on plasma behavior, particularly the "unsteady, three-dimensional behavior of the plasma jet" and its magnetic interactions, aligns with my research into how magnetic fields behave and interact within various plasma environments.
# (180/382) http://arxiv.org/pdf/2504.06576v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Theoretical analysis for non-linear effects of magnetic fields on unsteady boundary layer flows
**Jing-Yu Fu,Ming-Jiu Ni,Nian-Mei Zhang**


#mhd
### Abstract:
This study investigates unsteady boundary layer phenomena in electrically conducting fluids subjected to static magnetic fields. Using a semi-explicit similarity transformation method, the momentum equation associated with the Stokes stream function is solved. The nonlinear closed analytical solutions for both stagnation flow and converging flow are derived. The results demonstrate that the boundary layer structure incorporates similar shock and solitary wave components which are promoted by Lorentz force. Under extreme magnetic fields, the flow exhibits sine and cosine wave patterns, which are motivated by the strong Lorentz force. An in-depth asymptotic analysis establishes the square root scaling laws that quantify the growth of friction and flux with increasing magnetic field strength. The boundary layer thickness scales inversely with the Hartmann number, a consequence of dominant Lorentz force, which differs from the conclusion of duct flow (Hunt 1965). These findings elucidate the physical mechanisms governing the nonlinear coupling between magnetic fields and the dynamics of the boundary layer.


![[mdfiles/2504.06576.md|2504.06576]]
### AI Justification:
This paper is relevant to your interests in theoretical astrophysics and plasma physics as it presents a "theoretical analysis for non-linear effects of magnetic fields," which aligns with your focus on "magnetic field amplification" and "interactions" in plasma environments. Moreover, the study's exploration of how the "Lorentz force" influences "unsteady boundary layer flows" adds value to your understanding of the complex dynamics of magnetic fields within plasma structures.
# (181/382) http://arxiv.org/pdf/2504.05938v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Umbral oscillations in the photosphere. A comprehensive statistical study
**M. Berretti,M. Stangalini,G. Verth,V. Fedun,S. Jafarzadeh,D. B. Jess,...**


#mhd
### Abstract:
It is well-known that the global acoustic oscillations of the Suns atmosphere can excite resonance modes within large-scale magnetic concentrations. These structures are conduits of energy between the different layers of the solar atmosphere, and understanding their dynamics can explain the processes behind coronal heating and solar wind acceleration. In this work, we studied the Doppler velocity spectrum of more than a thousand large-scale magnetic structures (i.e., sunspots) in the solar photosphere that crossed near the disk centre of the Sun. We exploited the excellent stability and seeing-free conditions of the Helioseismic and Magnetic Imager (HMI) instrument onboard the Solar Dynamics Observatory (SDO) to cover nearly seven years of observations, providing the most comprehensive statistical analysis of its kind. Here, we show that the power spectra of the umbra of sunspots in the photosphere is remarkably different from the one of quiet-Sun regions, with both exhibiting a primary peak at 3.3 mHz, but the sunspot umbrae also displaying a closely packed series of secondary peaks in the $4-6$ ~mHz band. Understanding the origin of such peaks is a challenging task. Here, we explore several possible explanations for the observed oscillations, all pointing toward a potential resonant interaction within these structures and an unknown driver. Our observational result provides further insight into the magnetic connectivity between the different layers of the dynamic atmosphere of the Sun.


![[mdfiles/2504.05938.md|2504.05938]]
### AI Justification:
This paper is somewhat relevant to your research interests as it discusses the dynamics of large-scale magnetic structures (sunspots) and their interaction with oscillations in the solar atmosphere, which aligns with your focus on "magnetic dynamics of plasmas" and how these fields interact. However, while it delves into the magnetic connectivity and dynamics within the solar environment, it does not directly address "magnetic field amplification" or the broader scale-dependent structuring you are interested in, particularly in the context of the interstellar medium.
# (182/382) http://arxiv.org/pdf/2504.04439v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The enigmatic magnetic field of the planet hosting Herbig Ae/Be star HD169142
**S. Hubrig,S. P. Jarvinen,I. Ilyin,M. Scholler**


#mhd
### Abstract:
Recent observations of the accretion disk around the Herbig Ae/Be star HD169142 revealed its complex and asymmetric morphology indicating the presence of planets. The knowledge of the magnetic field structure in host stars is indispensable for our understanding of the magnetospheric interaction between the central stars, the circumstellar (CS) environment, and planetary companions. We intend to study the geometry of the magnetic field of HD169142. We measured the mean longitudinal magnetic field from high resolution ESPaDOnS and HARPSpol spectra of HD169142 using the Least Square Deconvolution technique. Additionally, the spectral variability of hydrogen lines is studied using dynamical spectra. Our analysis of the Stokes V spectra reveals the presence of definitely detected narrow Zeeman features observed using line masks with neutral iron lines. On two observing epochs, we also obtain marginally detected broad Zeeman features. To explain the simultaneous appearance of narrow and broad Zeeman features, we discuss different scenarios, including one scenario related to a non-photospheric origin of the narrow Zeeman features due to magnetospheric interaction with warm CS matter. In an environment such as a wind or an accretion disk, spectral lines may form over a relatively large volume, and the field topology may therefore be complex not only in latitude and azimuth, but in radius as well. Dynamical plots of the Hbeta line show an intriguing very complex structure with appearing and disappearing absorption features, which can be related to the complex morphology of the CS matter with asymmetric dust clump structures. The profiles of spectral lines belonging to different elements are variable, indicating the presence of chemical spots.


![[mdfiles/2504.04439.md|2504.04439]]
### AI Justification:
This paper addresses magnetic field dynamics in an accretion disk environment, making it relevant to your interest in "magnetic dynamics of plasmas" and how these fields interact with their surroundings. The discussion on "magnetospheric interaction" and "complex morphology" provides insights into scale-dependent structuring, which aligns well with your focus on multi-scale magnetic field dynamics in astrophysical contexts.
# (183/382) http://arxiv.org/pdf/2504.02138v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Anomalous cross-field motions of solar coronal loops
**Sudip Mandal,Hardi Peter,James A. Klimchuk,Lakshmi Pradeep Chitta**


#mhd
### Abstract:
Here, we present several examples of unusual evolutionary patterns in solar coronal loops that resemble cross-field drift motions. These loops were simultaneously observed from two vantage points by two different spacecraft... the High-Resolution Imager (HRI $_{EUV}$ ) of the Extreme Ultraviolet Imager aboard the Solar Orbiter and the Atmospheric Imaging Assembly (AIA) aboard the Solar Dynamics Observatory. Across all these events, a recurring pattern is observed... Initially, a thin, strand-like structure detaches and shifts several megameters (Mm) away from a main or parent loop. During this period, the parent loop remains intact in its original position. After a few minutes, the shifted strand reverses its direction and returns to the location of the parent loop. Key features of this `split-drift type evolution are... (i) the presence of kink oscillations in the loops before and after the split events, (ii) a sudden split motion at about 30~km.s $^{-1}$ , with additional slow drifts, either away from or back to the parent loops, at around 5~km.s $^{-1}$ . Co-temporal photospheric magnetic field data obtained from the Helioseismic and Magnetic Imager (HMI) reveal that during such split-drift evolution, one of the loop points in the photosphere moves back and forth between nearby magnetic polarities. While the exact cause of this `split-drift phenomenon is still unclear, the consistent patterns observed in its characteristics indicate that there may be a broader physical mechanism at play. This underscores the need for further investigation through both observational studies and numerical simulations.


![[mdfiles/2504.02138.md|2504.02138]]
### AI Justification:
This paper's examination of "cross-field drift motions" and "kink oscillations" in solar coronal loops aligns with your interest in the magnetic dynamics of plasmas, particularly in how magnetic interactions can shape the structure and behavior of these fields within plasma environments. The mention of the necessity for further investigation through "observational studies and numerical simulations" highlights a methodological approach that resonates with your focus on theoretical models and simulations in astrophysical settings.
# (184/382) http://arxiv.org/pdf/2504.00913v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Determining the 3D Dynamics of Solar Flare Magnetic Reconnection
**Joel T. Dahlin,Spiro K. Antiochos,C. Richard DeVore,Peter F. Wyper,Jiong Qiu**


#mhd
### Abstract:
Solar flares are major space weather events that result from the explosive conversion of stored magnetic energy into bulk motion, plasma heating, and particle acceleration. While the standard flare model has proven highly successful in explaining key morphological features of flare observations, many aspects of the energy release are not yet understood. In particular, the turbulent three-dimensional structure of the flare current sheet is thought to play an important role in fast reconnection, particle acceleration, and bursty dynamics. Although direct diagnosis of the magnetic field dynamics in the corona remains highly challenging, rich information may be gleaned from flare ribbons, which represent the chromospheric imprints of reconnection in the corona. Intriguingly, recent solar imaging observations have revealed a diversity of fine structure in flare ribbons that hints at corresponding complexity in the reconnection region. We present high-resolution three-dimensional MHD simulations of an eruptive flare and describe our efforts to interpret fine-scale ribbon features in terms of the current sheet dynamics. In our model, the current sheet is characterized by many coherent magnetic structures known as plasmoids. We derive a model analogue for ribbons by generating a time series of field-line length maps (L-maps) and identifying abrupt shortenings as flare reconnection events. We thereby demonstrate that plasmoids imprint transient spirals along the analogue of the ribbon front, with a morphology consistent with observed fine structure. We discuss the implications of these results for interpreting SolO, IRIS, and DKIST observations of explosive flare energy release.


![[mdfiles/2504.00913.md|2504.00913]]
### AI Justification:
This paper is relevant to your research interests as it explores "3D Dynamics of Solar Flare Magnetic Reconnection," which aligns with your focus on "magnetic dynamics of plasmas." The use of "MHD simulations" to interpret "coherent magnetic structures" and their role in energy release and interactions reflects your interest in "the interactions between magnetic, gravitational, and thermal forces" within plasma environments.
# (185/382) http://arxiv.org/pdf/2503.23607v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Accretion Properties and Jet Mechanisms for the Low-Excitation Radio Galaxies
**Xu-Hong Ye,Ranieri D. Baldi,Yong-Yun Chen,Denis Bastieri,Jun-Hui Fan**


#mhd
### Abstract:
Radio galaxies (RGs) are a subclass of active galactic nuclei, which are suggested to be the parent populations of blazars. According to the accretion-ejection paragram, RGs can be classified into low-excitation or high-excitation radio galaxies (LERGs or HERGs). In this paper, we compiled a distance-limited ( $z<0.15$ ) sample of 431 LERGs (Fanaroff-Riley, or FR, type 0, I, and II RGs) to discuss their jet formation mechanism with the ADAF (advection-dominated accretion flow) scenario, and compare their accretion properties with Fermi BL Lacertae objects. We explored different jet mechanisms (Blandford-Znajek [BZ] model and a mixture of the BZ and Blandford-Payne, hybrid, model) within the framework of ADAF-type disc around a Kerr black hole for both LERGs and Fermi BL Lacs. Based on standard assumptions on the accretion-ejection coupling in RGs, the maximum kinetic jet and accretion power for FR 0s, FR Is, FR IIs can be, explained by an ADAF with the pure BZ mechanism or hybrid jet mechanism. In addition, for one third of the FR IIs, to account for their higher kinetic jet power than what is simply expected by the hybrid jet mechanism, the magnetic field could play an important role as in the form of magnetization-driven outflows or stronger magnetic structures, as observed in some BL Lacs with high jet powers. Similarities between BL Lacs and LERGs (e.g., accretion-ejection and clustering properties) suggest that high synchrotron peaked BL Lacs could be the beamed counterparts of FR 0s, and a potential general unification between LERGs and BL Lacs populations is discussed. However, a complete sample of BL Lacs is needed to robustly compare the jet and accretion properties with those of LERGs in the future.


![[mdfiles/2503.23607.md|2503.23607]]
### AI Justification:
This paper provides insights into the magnetic dynamics in astrophysical contexts, particularly through its discussion on the role of magnetic fields in jet formation mechanisms such as the Blandford-Znajek model and hybrid jet mechanism. Its exploration of the relationship between accretion properties and magnetic structure in low-excitation radio galaxies aligns with my interest in "Magnetic Field Amplification" and "Emergent Magnetic Dynamics in Turbulent Plasmas," making it a potentially valuable addition to my research.
# (186/382) http://arxiv.org/pdf/2503.22509v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Comparison of plasma dynamics in Coronal Holes and Quiet Sun using flux emergence simulations
**Vishal Upendran,Durgesh Tripathi,Bhargav Vaidya,Mark Cheung,Takaaki Yokoyama**


#mhd
### Abstract:
This paper presents a comparison of plasma dynamics in Coronal Holes (CHs) and Quiet Sun (QS) through 2.5D MHD flux emergence simulations. The magnetic reconnection between the emerging and the pre-existing flux leads to the formation of cool, dense plasmoids with hot boundaries, and hot & cool jets with velocities $\approx50$ km s $^{-1}$ . We perform spectral synthesis in spectral lines probing transition region and coronal temperatures. CHs show reduced intensities, excess upflows (downflows), and widths during the jetting (downflow) period when compared to QS. During the jetting and downflow periods, velocity and line width of the hot spectral lines in CHs show a strong positive correlation with the vertical magnetic field at z = 0, while the intensity of the cooler lines shows a weak correlation, which is not seen in QS. During the jetting period in CH, we find upflows in Si IV to be correlated (anti-correlated) with upflows (downflows) in other lines, and downflows in CH in Si IV to be correlated (anti-correlated) with upflows (downflows) in other lines when compared to QS. During downflow, we find no strong correlation between Si IV and other line velocities. The correlation during the jetting period occurs due to coincident, co-spatial origins of the hot and cool jet, while the lack of correlation during the downflow phase suggests a decoupling of hot and cool plasma. These results demonstrate that flux emergence and reconnection with pre-existing flux in the atmosphere support a unified scenario for solar wind formation and coronal heating.


![[mdfiles/2503.22509.md|2503.22509]]
### AI Justification:
The paper's examination of plasma dynamics through magnetic reconnection and flux emergence simulations aligns with my interest in "Magnetic Field Amplification" and "Force Interactions Shaping Magnetic Dynamics." The results on how coronal holes show different behaviors in magnetic field interactions provide insight into the role of magnetic fields in plasma environments, which is a core aspect of my theoretical work in astrophysics.
# (187/382) http://arxiv.org/pdf/2503.21229v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Eruptivity of Flaring Active Regions Based on Electric Current Neutralization and Torus Instability Analysis
**Johan Muhamad,Kanya Kusano**


#mhd
### Abstract:
Solar flares are frequently accompanied by coronal mass ejections (CMEs) that release significant amount of energetic plasma into interplanetary space, potentially causing geomagnetic disturbances on Earth. However, many solar flares have no association with CMEs. The relationship between solar flare and CME occurrences remains unclear. Therefore, it is valuable to distinguish between active regions that potentially produce flares and CMEs and those that do not. It is believed that the eruptivity of a flare can be characterized by the properties of the active region from which it originates. In this study, we analyzed selected active regions that produced solar flares with and without CMEs during solar cycle 24. We carefully calculated the electric current neutralization of each active region by selecting relevant magnetic fluxes based on their connectivities using nonlinear force-free field models. Additionally, we analyzed their stabilities against the torus instability by estimating the proxies of critical heights of the active regions. We found that several non-eruptive active regions, which lacked clear signatures of neutral electric currents, exhibited a more apparent relationship with high critical heights of torus instability. Furthermore, we introduced a new non-dimensional parameter that incorporates current neutralization and critical height. We found that analysing ARs based on this new parameter can better discriminate eruptive and non-eruptive flare events compared to analysis that relied solely on current neutralization or torus instability. This indicates that torus instability analysis is necessary to complement electric current neutralization in characterizing the eruptivity of solar flares.


![[mdfiles/2503.21229.md|2503.21229]]
### AI Justification:
The paper's examination of "electric current neutralization" and "torus instability" as they relate to solar flares aligns with my focus on "magnetic dynamics of plasmas" and "force interactions shaping magnetic dynamics." The emphasis on analyzing magnetic fluxes and the interplay of instability in active regions touches on how these factors can influence magnetic field behaviors in plasma environments, providing insights into mechanisms of field amplification and dynamics that could be relevant to interstellar and astrophysical contexts.
# (188/382) http://arxiv.org/pdf/2503.20535v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Small-scale energetic phenomena in Hε... Ellerman bombs, UV bursts, and small flares
**K. Krikova,T. M. D. Pereira**


#mhd
### Abstract:
Aims. We investigated the potential of using Hepsilon to diagnose small-scale energetic phenomena such as Ellerman bombs, UV bursts, and small-scale flares. Our focus is to understand the formation of the line and how to use its properties to get insight into the dynamics of small-scale energetic phenomena. Methods. We carried out a forward modeling study, combining simulations and detailed radiative transfer calculations. The 3D radiative magnetohydrodynamic simulations were run with the Bifrost code and included energetic phenomena. We employed a Markovian framework to study the Hepsilon multilevel source function, used relative contribution functions to identify its formation regions, and correlated the properties of synthetic spectra with atmospheric parameters. Results. Ellerman bombs are predominantly optically thick in Hepsilon, appearing as well-defined structures. UV bursts and small flares are partially optically thin and give rise to diffuse structures. The Hepsilon line serves as a good velocity diagnostic for small-scale heating events in the lower chromosphere. However, its emission strength is a poor indicator of temperature, and its line width offers limited utility due to the interplay of various broadening mechanisms. Compared to Halpha, Hepsilon exhibits greater sensitivity to phenomena such as Ellerman bombs, as its line core experiences higher extinction than the Halpha wing. Conclusions. Hepsilon is a valuable tool for studying small-scale energetic phenomena in the lower chromosphere. It provides more reliable estimates of velocities than those extracted from wing emission in Halpha or Hbeta. Maps of Hepsilon emission show more abundant energetic events than the Halpha counterpart. Our findings highlight Hepsilons potential to advance our understanding of dynamic processes in the solar atmosphere.


![[mdfiles/2503.20535.md|2503.20535]]
### AI Justification:
This paper focuses on small-scale energetic phenomena, specifically Ellerman bombs and UV bursts, which may provide insights into the magnetic dynamics of plasmas in the solar atmosphere. While it primarily targets the chromosphere and the diagnostics of heating events, the use of magnetohydrodynamic simulations aligns with your interest in the "multi-scale dynamics of magnetic fields in plasma environments," making it somewhat relevant to your research on magnetic dynamics.
# (189/382) http://arxiv.org/pdf/2503.19749v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A depolarisation census of ASKAP fast radio bursts
**Pavan A. Uttarkar,Ryan M. Shannon,Kelly Gourdji,Adam T. Deller,Tyson Dial,Marcin Glowacki,...**


#mhd
### Abstract:
Fast radio bursts (FRBs) are luminous, dispersed pulses of extra-galactic origin. The physics of the emission mechanism, the progenitor environment, and their origin are unclear. Some repeating FRBs are observed to have frequency-dependent exponential suppression in linear polarisation fraction. This has been attributed to multipath propagation in a surrounding complex magneto-ionic environment. The magnitude of depolarisation can be quantified using the parameter $\rm \sigma^{\prime}_{RM}$ , which can be used to model the magneto-ionic complexity of the medium. In addition to depolarisation, some repeating sources (in particular those with active magneto-ionic environments) have been identified to have co-located persistent radio sources (PRS). Searches for depolarisation of non-repeating sources are challenging due to the limited bandwidth of most FRB detection systems used to detect one-off bursts. However, even with a limited bandwidth, such depolarisation can be identified if it lies within the $\rm \sigma^{\prime}_{RM}$ sensitivity window of the telescope. In this paper, we present a search for depolarisation in $12$ one-off FRBs detected by the Australian SKA Pathfinder. We report on the first strongly depolarised FRB detected by ASKAP (FRB $~$ 20230526A) and a marginal detection of depolarisation in a second. We also report constraints on the presence of a PRS coincident with FRB $~$ 20230526A using observations obtained with the Australia Telescope Compact Array. We use this to study the relationship between $\rm \sigma^{\prime}_{RM}$ and PRS luminosity. Our investigation supports a scenario in which repeaters and non-repeaters share a common origin and where non-repeaters represent an older population relative to repeating FRBs.


![[mdfiles/2503.19749.md|2503.19749]]
### AI Justification:
This paper examines the interaction of fast radio bursts (FRBs) with complex magneto-ionic environments, which aligns with my interest in "Force Interactions Shaping Magnetic Dynamics." The focus on spontaneous depolarization and its relation to the magneto-ionic complexity of the medium suggests insights into "Scale-Dependent Magnetic Structuring," highlighting how magnetic fields behave within astrophysical plasma contexts.
# (190/382) http://arxiv.org/pdf/2503.16300v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Localized Heating and Dynamics of the Solar Corona due to a Symbiosis of Waves and Reconnection
**A. K. Srivastava,Sripan Mondal,Eric R. Priest,Sudheer K. Mishra,David I. Pontin,R. Y. Kwon,...**


#mhd
### Abstract:
The Suns outer atmosphere, the corona, is maintained at mega-Kelvin temperatures and fills the heliosphere with a supersonic outflowing wind. The dissipation of magnetic waves and direct electric currents are likely to be the most significant processes for heating the corona, but a lively debate exists on their relative roles. Here, we suggest that the two are often intrinsically linked, since magnetic waves may trigger current dissipation, and impulsive reconnection can launch magnetic waves. We present a study of the first of these processes by using a 2D physics-based numerical simulation using the Adaptive Mesh Refined (AMR) Versatile Advection Code (VAC). Magnetic waves such as fast magnetoacoustic waves are often observed to propagate in the large-scale corona and interact with local magnetic structures. The present numerical simulations show how the propagation of magnetic disturbances towards a null point or separator can lead to the accumulation of the electric currents. Lorentz forces can laterally push and vertically stretch the magnetic fields, forming a current sheet with a strong magnetic-field gradient. The magnetic field lines then break and reconnect, and so contribute towards coronal heating. Numerical results are presented that support these ideas and support the concept of a symbiosis between waves and reconnection in heating the solar corona.


![[mdfiles/2503.16300.md|2503.16300]]
### AI Justification:
This paper is relevant to your research interests as it explores "magnetic waves" and their interactions in the solar corona, which parallels your focus on the "behavior and interaction of magnetic fields" in plasma environments. Furthermore, the study utilizes a "2D physics-based numerical simulation," which aligns with your interest in theoretical models and simulations that examine complex magnetic dynamics across various scales.
# (191/382) http://arxiv.org/pdf/2503.14624v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A 7-Day Multi-Wavelength Flare Campaign on AU Mic. II... Electron Densities and Kinetic Energies from High-Frequency Radio Flares
**Isaiah I. Tristan,Rachel A. Osten,Yuta Notsu,Adam F. Kowalski,Alexander Brown,Graeme L. White,...**


#mhd
### Abstract:
M dwarfs are the most common type of star in the solar neighborhood, and many exhibit frequent and highly energetic flares. To better understand these events across the electromagnetic spectrum, a campaign observed AU Mic (dM1e) over 7 days from the X-ray to radio regimes. Here, we present high-time-resolution light curves from the Karl G. Jansky Very Large Array (VLA) Ku band (12--18 GHz) and the Australia Telescope Compact Array (ATCA) K band (16--25 GHz), which observe gyrosynchrotron radiation and directly probe the action of accelerated electrons within flaring loops. Observations reveal 16 VLA and 3 ATCA flares of varying shapes and sizes, from a short (30 sec) spiky burst to a long-duration ( $\sim$ 5 hr) decaying exponential. The Ku-band spectral index is found to often evolve during flares. Both rising and falling spectra are observed in the Ku-band, indicating optically thick and thin flares, respectively. Estimations from optically thick radiation indicate higher loop-top magnetic field strengths ( $\sim$ 1 kG) and sustained electron densities ( $\sim$ 10 $^{6}$ cm $^{-3}$ ) than previous observations of large M-dwarf flares. We estimate the total kinetic energies of gyrating electrons in optically thin flares to be between 10 $^{32}$ and 10 $^{34}$ erg when the local magnetic field strength is between 500 and 700 G. These energies are able to explain the combined radiated energies from multi-wavelength observations. Overall, values are more aligned with modern radiative-hydrodynamic simulations of M-dwarf flares, and future modeling efforts will better constrain findings.


![[mdfiles/2503.14624.md|2503.14624]]
### AI Justification:
The paper presents key insights into "magnetic field strengths" and "kinetic energies" within flaring loops, which aligns well with my interest in understanding magnetic field dynamics across various scales in plasma environments. The emphasis on observations of M-dwarf flares and their relation to plasma dynamics suggests potential for exploring mechanisms of "magnetic field amplification" and interactions that shape "magnetic dynamics," particularly with relevance to high-energy astrophysical events.
# (192/382) http://arxiv.org/pdf/2503.13606v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Planetesimal formation via the streaming instability in simulations of infall dominated young disks
**L. -A. Huhn,C. P. Dullemond,U. Lebreuilly,R. S. Klessen,A. Maury,G. P. Rosotti,...**


#mhd
### Abstract:
Protoplanetary disks naturally emerge during protostellar core-collapse. In their early evolutionary stages, infalling material dominates their dynamical evolution. In the context of planet formation, this means that the conditions in young disks are different from the typically considered disks where infall has subsided. High inward velocities are caused by the advection of accreted material which is deficient in angular momentum, rather than being set by viscous spreading, and accretion gives rise to strong velocity fluctuations. Therefore, we aim to investigate when it is possible for the first planetesimals to form and subsequent planet formation to commence. We analyze the disks obtained in numerical 3D nonideal magnetohydrodynamical simulations, which serve as a basis for 1D models representing the conditions during the Class 0/I evolutionary stages. We integrate the 1D models with an adapted version of the TwoPopPy code to investigate the formation of the first planetesimals via the streaming instability. In disks with temperatures such that the snow line is located at ~10 AU and where it is assumed that velocity fluctuations felt by the dust are reduced by a factor of 10 compared to the gas, ${\sim}10^{-3}M_\odot$ of planetesimals may be formed already during the first 100 kyr after disk formation, implying the possible early formation of giant planet cores. The cold-finger effect at the snow line is the dominant driver of planetesimal formation, which occurs in episodes and utilizes solids supplied directly from the envelope, leaving the disk solid reservoir intact. However, if the cold-finger effect is suppressed, early planetesimal formation is limited to cold disks with efficient dust settling whose dust-to-gas ratio is initially enriched to $\epsilon_0\geq 0.03$ .


![[mdfiles/2503.13606.md|2503.13606]]
### AI Justification:
The paper explores the dynamics of protoplanetary disks, particularly during the early evolution stages, which has relevance to the magnetic dynamics of plasmas in the interstellar medium, a key focus of your research. Specifically, the use of numerical 3D nonideal magnetohydrodynamical simulations to analyze conditions affecting planetesimal formation could provide insights into magnetic field behavior and amplification, especially given your interest in how these fields evolve in turbulent plasma environments.
# (193/382) http://arxiv.org/pdf/2503.11448v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Cygnus X-3 as semi-hidden PeVatron
**M. Kachelriess,E. Lammert**


#mhd
### Abstract:
The high-mass X-ray binary Cygnus X-3 has been suggested for a long time to be a source of high-energy photons and neutrinos. In view of the increased sensitivity of current experiments, we examine the acceleration and interactions of high-energy cosmic rays (CRs) in this binary system, assuming that the compact object is a black hole. Using a test-particle approach in a Monte-Carlo framework, we employ as the basic CR acceleration mechanisms magnetic reconnection or 2.nd order Fermi acceleration and diffusive shock acceleration. We find that in all three scenarios CRs can be accelerated beyond PeV energies. High-energy photons and neutrinos are produced as secondaries in photo-hadronic interactions of CRs on X-ray photons and in the scattering on gas from the wind of the companion star. Normalising the predicted photon flux to the excess flux observed by LHAASO at energies above PeV in the direction of Cygnus X-3, a CR acceleration efficiency of $10^{-3}$ is sufficient to power the required CR luminosity. Our results suggest that the PeV photon flux from Cygnus X-3 could be in a bright phase significantly increased relative to the average flux of the last years.


![[mdfiles/2503.11448.md|2503.11448]]
### AI Justification:
This paper has relevance to your interests as it discusses the "acceleration and interactions of high-energy cosmic rays" in the context of a "high-mass X-ray binary," which may indirectly encompass the magnetic dynamics of plasmas through mechanisms like "magnetic reconnection" and "diffusive shock acceleration." The findings related to high-energy photons and the role of magnetic interactions provide insights into "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas," aligning with your focus on how magnetic fields influence plasma environments.
# (194/382) http://arxiv.org/pdf/2503.11459v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Moving Plasma Structures and Possible Driving Mechanisms of Solar Microflares Observed with High-Resolution Coronal Imaging
**Qingmei Wang,Yi Bi,Hongfei Liang,Jiayan Yang,Liufan Gong**


#mhd
### Abstract:
Solar microflares are ubiquitous in the solar corona, yet their driving mechanisms remain a subject of ongoing debate. Using high-resolution coronal observations from the Solar Orbiters Extreme Ultraviolet Imager (EUI), we identified about a dozen distinct moving plasma structures (hereafter, `` tiny ejections) originating from the centers of three homologous microflares out of four successive events. These tiny ejections propagate roughly perpendicular to the flaring loops. They often originate as dot-like structures with a length scale of approximately $10^{3}$ km. While these initial dot-like shapes are observable in EUI images, they remain undetectable in the images captured by the Atmospheric Imaging Assembly onboard the Solar Dynamics Observatory. As they propagate, these dot-like structures consistently evolve into loop-like formations, possibly due to the heating of the surrounding magnetic field. Rather than being generated by a series of flux rope eruptions, the tiny ejections appear to result from small-angle magnetic reconnections within a bipolar field. Thus, the microflares associated with these ejections may be driven by magnetic reconnection within braided fields, a process similar to the proposed nanoflare mechanism and distinct from the standard large-scale flare model.


![[mdfiles/2503.11459.md|2503.11459]]
### AI Justification:
This paper addresses the dynamics of magnetic reconnection in solar plasmas, specifically mentioning "magnetic reconnections within braided fields" and their role in driving solar microflares, which aligns with your interest in magnetic field interactions and amplification. While the focus is on the solar corona, the mechanisms discussed may provide insights into broader magnetic dynamics and may offer theoretical models relevant to your research on "how magnetic fields behave, interact, and amplify across various scales."
# (195/382) http://arxiv.org/pdf/2503.11451v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Oscillations of red giant stars with magnetic damping in the core. I. Dissipation of mode energy in dipole-like magnetic fields
**Jonas Muller,Quentin Coppee,Saskia Hekker**


#mhd
### Abstract:
Strong magnetic fields in the core of red-giant branch stars are expected to suppress the amplitudes of the multipole modes. This occurs when the strength of the internal magnetic field approaches the critical field strength, at which the magnetic forces become comparable to the buoyancy. We performed Hamiltonian ray tracing simulations of magneto-gravity waves to investigate the suppression of the multipole modes in the presence of an internal dipole-like magnetic field. We took into account different stellar masses, metallicities, and ages, as well as various oscillation frequencies and spherical degrees. In particular, we estimated the trapped fraction, a measure of multipole mode suppression, which quantifies the fraction of mode energy in the core that is dissipated by the interaction with the magnetic field. Our results indicate that the trapped fraction can be described by a simple expression, which smoothly connects the regime without multipole mode suppression with the regime with complete suppression of the multipole modes. Crucially, the trapped fraction depends only on the ratio between the strength of the internal magnetic field and the critical field strength. Therefore, our expression for the trapped fraction provides a flexible tool that can be used, for example, to estimate the amount of multipole mode suppression as a star ascends the red-giant branch or to investigate the onset of the suppression in observed power spectral densities.


![[mdfiles/2503.11451.md|2503.11451]]
### AI Justification:
This paper explores the behavior of magnetic fields in the context of oscillations in red giant stars, which aligns with your interest in the "interactions between magnetic, gravitational, and thermal forces" as it discusses how magnetic forces impact the mechanisms of wave suppression. Moreover, the results concerning the "trapped fraction" provide a framework that could be adapted to understand magnetic dynamics not just in stellar contexts but potentially in broader astrophysical plasma environments.
# (196/382) http://arxiv.org/pdf/2503.10747v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Lévy Flights and Leaky Boxes... Anomalous Diffusion of Cosmic Rays
**Naixin Liang,Siang Peng Oh**


#mhd
### Abstract:
In classical diffusion, particle step-sizes have a Gaussian distribution. However, in superdiffusion, they have power-law tails, with transport dominated by rare, long L\evy flights. Similarly, if the time interval between scattering events has power-law tails, subdiffusion occurs. Both forms of anomalous diffusion are seen in cosmic ray (CR) particle tracking simulations in turbulent magnetic fields. They also likely occur if CRs are scattered by discrete intermittent structures. Anomalous diffusion mimics a scale-dependent diffusion coefficient, with potentially wide-ranging consequences. However, the finite size of galaxies implies an upper bound on step-sizes before CRs escape. This truncation results in eventual convergence to Gaussian statistics by the central limit theorem. Using Monte-Carlo simulations, we show that this occurs in both standard finite-thickness halo models, or when CR diffusion transitions to advection or streaming-dominated regimes. While optically thick intermittent structures produce power-law trapping times and thus subdiffusion, gaussianization also eventually occurs on timescales longer than the maximum trapping time. Anomalous diffusion is a transient, and converges to standard diffusion on the (usually short) timescale of particle escape, either from confining structures (subdiffusion), or the system as a whole (superdiffusion). Thus, standard assumptions of classical diffusion are physically justified in most applications, despite growing simulation evidence for anomalous diffusion. However, if escape times are long, this is no longer true. For instance, anomalous diffusion in the CGM or ICM would change CR pressure profiles. Finally, we show the standard diagnostic for anomalous diffusion, $\langle d^2 \rangle \propto t^{\alpha} $ with $ \alpha \neq 1$ , is not justified for truncated L\evy flights, and propose an alternative robust measure.


![[mdfiles/2503.10747.md|2503.10747]]
### AI Justification:
The paper's exploration of "anomalous diffusion" in cosmic rays within "turbulent magnetic fields" directly aligns with your interest in "emergent magnetic dynamics" and "force interactions shaping magnetic dynamics" in astrophysical plasmas. Additionally, the discussion of how cosmic ray pressures could be influenced by magnetic field configurations in the circumgalactic medium (CGM) or intercluster medium (ICM) speaks to your focus on "magnetic field amplification" and its impact across various scales.
# (197/382) http://arxiv.org/pdf/2503.10456v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Ionization memory of plasma emiters in a solar prominence
**E. Wiehr,H. Balthasar,G. Stellmacher,M. Bianda**


#mhd
### Abstract:
Aims. In the low-collisional, partially ionized plasma (PIP) of solar prominences, uncharged emitters might show different signatures of magnetic line broadening than charged emitters. We investigate if the widths of weak metall emissions in prominences exceed the thermal line broadening by a different amount for charged and for uncharged emitters. Methods. We simultaneously observe five optically thin, weak metall lines in the brightness center of a quiescent prominence and compare their observed widths with the thermal broadening. Results. The inferred non-thermal broadening of the metall lines does not indicate systematic differences between the uncharged Mg b2 and Na D1 and the charged Fe II emitters, only Sr II is broader. Conclusions. The additional line broadening of charged emitters is reasonably attributed to magnetic forces. That of uncharged emitters can then come from their temporary state as ion before recombination. Magnetically induced velocities will retain some time after recombination. Modelling partially ionized plasmas then requires consideration of a memory of previous ionization states.


![[mdfiles/2503.10456.md|2503.10456]]
### AI Justification:
The paper focuses on the magnetic dynamics of plasmas in solar prominences, which is relevant to my interest in the "interstellar medium" and "magnetic dynamics." The study of "magnetic forces" affecting line broadening in the context of partially ionized plasma reflects my focus on how "magnetic fields behave and interact" in complex plasma environments.
# (198/382) http://arxiv.org/pdf/2503.09744v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Suns open-closed flux boundary and the origin of slow solar wind
**Chloe P. Wilkins,David I. Pontin,Anthony R. Yeates,Spiro K. Antiochos,Hannah Schunker,Bishnu Lamichhane**


#mhd
### Abstract:
The Suns open-closed flux boundary (OCB) separates closed and open magnetic field lines, and is the site for interchange magnetic reconnection processes thought to be linked to the origin of the slow solar wind (SSW). We analyse the global magnetic field structure and OCB from December 2010 to December 2019 using three coronal magnetic field models... a potential field source surface (PFSS) model, a static equilibrium magnetofrictional model, and a time-dependent magnetofrictional model. We analyse the model and cycle dependence of the OCB length on the photosphere, as well as the magnetic flux in the vicinity of the OCB. Near solar maximum, the coronal magnetic field for each model consists predominantly of long, narrow coronal holes, and nearly all the open flux lies within one supergranule-diameter (25 Mm) of the OCB. By comparing to interplanetary scintillation measurements of SSW speeds, we argue that the fraction of open flux within this 25 Mm band is a good predictor of the amount of SSW in the heliosphere. Importantly, despite its simplicity, we show that the PFSS model estimates this fraction as well as the time-dependent model. We discuss the implications of our results for understanding SSW origins and interchange reconnection at the OCB.


![[mdfiles/2503.09744.md|2503.09744]]
### AI Justification:
This paper is relevant to your research interests in the magnetic dynamics of plasmas due to its focus on "the site for interchange magnetic reconnection processes" and the implications for "the origin of the slow solar wind," which connects to the broader dynamics of magnetic fields in astrophysical environments. Additionally, its analysis of different models for the global magnetic field structure aligns with your interest in "the complex, multi-scale dynamics of magnetic fields in plasma environments," making it potentially valuable for understanding magnetic structuring across various scales.
# (199/382) http://arxiv.org/pdf/2503.06250v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Phase transitions in the inner crust of neutron stars within the superfluid band theory... Competition between $^1\text{S}_0$ pairing and spin polarization under finite temperature and magnetic field
**Kenta Yoshimura,Kazuyuki Sekizawa**


#mhd
### Abstract:
Phase transitions of matter under changes of external environment such as temperature and magnetic field have attracted great interests to various quantum many-body systems. Several phase transitions must have occurred in neutron stars as well such as transitions from normal to superfluid/superconducting phases and crust formation. In this work, we extend the superfluid band theory, which has been formulated in our previous work [K. Yoshimura and K. Sekizawa, Phys. Rev. C 109, 065804 (2024)] based on the Kohn-Sham density functional theory (DFT) for superfluid systems, into the finite temperature and finite magnetic field systems. As a result of the finite temperature calculations, we find that the superfluidity of neutrons dissapears at around $k_\text{B}T=0.6$ -- $0.9\,$ MeV, and ``melting of nuclear slabs, that is, a structural change into the uniform matter, takes place at around $k_\text{B}T=2.5$ -- $4.5\,$ MeV. We also reveal that these transition temperatures exhibit a systematical dependence on the baryon densities. By turning on the magnetic field, we find that protons spin gets polarized at around $B=10^{16}\,$ G, whereas neutrons spin is kept unpolarized on average up to around $B=10^{17}\,$ G. Intriguingly, our microscopic calculations reveal that neutrons spin is actually polarized locally inside and outside of the slab already at $B\sim10^{16}\,$ G, while keeping the system unpolarized in total. As a conclusion, we have demonstrated validity and usefulness of the fully self-consistent superfluid nuclear band theory for describing neutron star matter under arbitrary temperature and magnetic field. Critical temperatures and magnetic fields have been predicted for 1) superfluid to normal transition, 2) crust formation, and 3) spin polarization, under conditions relevant to realistic neutron star environments.


![[mdfiles/2503.06250.md|2503.06250]]
### AI Justification:
This paper is relevant to your interests as it addresses the behavior of magnetic fields in extreme astrophysical environments, specifically within neutron stars under varying temperature and magnetic field conditions. The focus on "spin polarization" and its interaction with strong magnetic fields aligns with your research on "magnetic dynamics of plasmas" and how such fields "behave, interact, and amplify" across various scales.
# (200/382) http://arxiv.org/pdf/2503.05293v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Bypassing the static input size of neural networks in flare forecasting by using spatial pyramid pooling
**Philippe Vong,Laurent Dolla,Alexandros Koukras,Jacques Gustin,Jorge Amaya,Ekaterina Dineva,...**


#mhd
### Abstract:
The spatial extension of active regions (ARs) of the Sun can vary from one case to the next. This is a problem when studying solar flares with Convolutional Neural Networks (CNNs) as they generally use input images of a fixed size. Different processes can be performed to retrieve a database with homogeneous-sized data, such as resizing. Unfortunately, key features can be lost or distorted during these processes. This can lead to a deterioration of the ability of CNNs to classify flares of different soft X-ray classes, especially those from ARs with complex structures. Our work aims to implement and test a CNN architecture that retains the full features of the original resolution of the input images. We compare the performance of two CNN architectures for solar flare prediction... the first is a traditional CNN with resized input whereas the other implements a spatial pyramid pooling (SPP) layer without any input resizing. Both are trained on the Spaceweather HMI Active Region Patch line-of-sight magnetogram database. We also study two cases of binary classification. In the first case, our model distinguishes ARs producing flares in less than 24h of class greater or equal to C1.0 from ARs producing flares in more than 24h or never; in the second case, it distinguishes ARs producing flares in less than 24h of class greater or equal to M1.0 from the other ARs. Our models implementing an SPP layer outperform the traditional CNN models when predicting flares greater or equal to C1.0 within 24h. However, their performances degrade sharply along the other models studied in this paper, when trained to classify images greater or equal to M1.0 flares. The degradation in SPP models when classifying only images greater or equal to M1.0 flares as positive may be attributed to its success in identifying features that appear in ARs a few hours before the flare, independently of their soft X-ray class.


![[mdfiles/2503.05293.md|2503.05293]]
### AI Justification:
This paper is somewhat relevant to your research interests, as it discusses the use of Convolutional Neural Networks (CNNs) to classify solar active regions (ARs) based on their magnetic properties and flare activity, touching on concepts such as "interactions between magnetic forces" and "complex structures" within plasma environments. However, while it focuses on a specific application in solar physics rather than the broader aspects of magnetic field amplification and dynamics in the interstellar medium, it may offer insights into computational methods for analyzing magnetic structures.
# (201/382) http://arxiv.org/pdf/2503.01960v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The abundance and origin of cool gas in galaxy clusters in the TNG-Cluster simulation
**Milan Staffehl,Dylan Nelson,Mohammadreza Ayromlou,Eric Rohr,Annalisa Pillepich**


#mhd
### Abstract:
In addition to the hot intracluster medium, massive galaxy clusters host complex, multi-phase gaseous halos. In this work, we quantify the abundance, spatial distribution, and origin of the cool T < 10^4.5 K gas within clusters. To do so, we combine the TNG-Cluster and TNG300 cosmological magnetohydrodynamical simulations, yielding a sample of 632 simulated galaxy clusters at z=0 with masses M_200c ~ 10^14-15.4 solar masses. We find that cool gas is present in every cluster at z=0, although it constitutes only a small fraction of the total gas mass within twice the virial radius, ranging from ~10^-4 to a few per cent. The majority of cool gas resides in the cluster outskirts in infalling satellites and other halos. More rarely, cool gas can also be present in the central regions of clusters. More massive halos contain larger amounts (but not fractions) of cool gas ~10^10-12 solar masses, and we identify correlations between cluster cool gas fraction and several global halo and galaxy properties at fixed halo mass. Using Monte-Carlo Lagrangian tracer particles, we then track the origin of cool gas in present-day clusters. We find that the primary source is recent accretion at z < 0.1, predominantly in the form of pre-cooled gas carried by infalling satellite galaxies and other halos. However, in-situ cooling of the hot intracluster medium gas accreted at earlier epochs also contributes, especially in present-day cool-core clusters.


![[mdfiles/2503.01960.md|2503.01960]]
### AI Justification:
This paper is somewhat relevant to my interests as it explores the spatial distribution and origin of cool gas in galaxy clusters, which ties into the broader context of magnetic dynamics in the intercluster medium. Although the focus on cool gas quantification does not directly address magnetic field amplification or the dynamics of plasmas, the use of "cosmological magnetohydrodynamical simulations" suggests that magnetism's role within these structures may be implicitly examined, providing a potential avenue for understanding force interactions shaping magnetic dynamics.
# (202/382) http://arxiv.org/pdf/2503.00593v1


### Rating: 6.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 65%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Electromagnetic Electron Kelvin-Helmholtz Instability
**H. Che,G. P. Zank**


#mhd
### Abstract:
On electron kinetic scales, ions and electrons decouple, and electron velocity shear on electron inertial length $\sim d_e$ can trigger electromagnetic (EM) electron Kelvin-Helmholtz instability (EKHI). In this paper, we present an analytic study of EM EKHI in an inviscid collisionless plasma with a step-function electron shear flow. We show that in incompressible collisionless plasma the ideal electron frozen-in condition $\mathbf{E} + \mathbf{v}_e \times \mathbf{B}/c = 0$ must be broken for the EM EKHI to occur. In a step-function electron shear flow, the ideal electron frozen-in condition is replaced by magnetic flux conservation, i.e., $\nabla \times (\mathbf{E} + \mathbf{v}_e\times \mathbf{B}/c) = 0$ , resulting in a dispersion relation similar to that of the standard ideal and incompressible magnetohydrodynamics KHI. The magnetic field parallel to the electron streaming suppresses the EM EKHI due to magnetic tension. The threshold for the EM mode of the EKHI is $(\mathbf{k}\cdot\Delta\mathbf{U}_e)^2>\frac{n_{e1}+n_{e2}}{n_{e1} n_{e2}}[n_{e1}(\mathbf{v}_{Ae1}\cdot\mathbf{k})^2+n_{e2}(\mathbf{v}_{Ae2}\cdot\mathbf{k})^2]$ , where $\mathbf{v}_{Ae} =\mathbf{B}/(4\pi m_e n_e)^{1/2}$ , $\Delta\mathbf{U}_e$ and $n_e$ are the electron streaming velocity shear and densities, respectively. The growth rate of the EM mode is $\gamma_{em} \sim \Omega_{ce}$ , the electron gyro-frequency.


![[mdfiles/2503.00593.md|2503.00593]]
### AI Justification:
This paper is relevant to your research interests as it explores the electromagnetic electron Kelvin-Helmholtz instability (EKHI), which involves "electron velocity shear" in plasma environments, closely aligning with your focus on "magnetic dynamics of plasmas." Furthermore, the implications about "magnetic tension" influencing the growth of instability provide insights into how magnetic fields can behave and interact on kinetic scales, resonating with your interest in "interactions between magnetic, gravitational, and thermal forces."
# (203/382) http://arxiv.org/pdf/2504.20636v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quasiperiodic Slow-Propagating EUV `Wave` Trains After the Filament Eruption
**Yining Zhang,Ting Li,Weilin Teng,Xinping Zhou,Yijun Hou,Zheng Sun,...**


#mhd
### Abstract:
The eruption of the filament/flux rope generates the coronal perturbations, which further form EUV waves. There are two types of EUV waves, including fast-mode magnetosonic waves and slow waves. In this paper, we first report an event showing the Quasiperiodic Slow-Propagating (QSP) EUV `wave` trains during an M6.4-class flare (SOL2023-02-25T18...40), using multiple observations from SDO/AIA, CHASE/HIS, ASO-S/FMG, SUTRI, and LASCO/C2. The QSP `wave` trains occurred as the filament showed a rapid rise. The QSP `wave` trains have the projected speeds of 50-130 km s $^{-1}$ on the plane of the sky, which is slower than the fast-mode magnetosonic speed in the solar corona. And the calculated period of the QSP wave trains is 117.9 s, which is in good agreement with the associated flare Quasi-Periodic Pulsation (140.3 s). The QSP wave trains could be observed during the entire impulsive phase of the flare and lasted about 30 minutes in the field of view (FOV) of SDO/AIA. About 30 minutes later, they appeared in the FOV of LASCO/C2 and propagated to the northwest. We suggest that the QSP wave trains are probably apparent waves that are caused by the successive stretching of the inclined field lines overlying the eruptive filament. The periodic pattern of the QSP wave trains may be related to the intermittent energy release during the flare.


![[mdfiles/2504.20636.md|2504.20636]]
### AI Justification:
This paper discusses the generation of coronal perturbations and the propagation of quasiperiodic slow-propagating EUV wave trains, which could relate to the dynamics of magnetic fields in astrophysical plasmas, particularly concerning "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas." The suggestion that the wave trains are caused by stretching of magnetic field lines "overlying the eruptive filament" indicates an interaction of magnetic forces, which aligns with my research focus on how magnetic fields behave and evolve in plasma environments.
# (204/382) http://arxiv.org/pdf/2504.16662v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### MHD Simulations Preliminarily Predict The Habitability and Radio Emission of TRAPPIST-1e
**BoRui Wang,ShengYi Ye,J. Varela,XinYi Luo**


#mhd
### Abstract:
As the closest Earth-like exoplanet within the habitable zone of the M-dwarf star TRAPPIST-1, TRAPPIST-1e exhibits a magnetic field topology that is dependent on space weather conditions. Variations in these conditions influence its habitability and contribute to its radio emissions. Our objective is to analyze the response of different terrestrial magnetosphere structures of TRAPPIST-1e to various space weather conditions, including events analogous to coronal mass ejections (CMEs). We assess its habitability by computing the magnetopause standoff distance and predict the resulting radio emissions using scaling laws. This study provides some priors for future radio observations. We perform three-dimensional magnetohydrodynamic (MHD) simulations of the TRAPPIST-1e system using the PLUTO code in spherical coordinates. Our analysis indicates that the predicted habitability and radio emission of TRAPPIST-1e strongly depend on the planets magnetic field intensity and magnetic axis inclination. Within sub-Alfvenic, super-Alfvenic, and transitional stellar wind regimes, the radio emission intensity positively correlates with both planetary magnetic field strength and axial tilt, while planetary habitability, quantified by the magnetopause standoff distance, shows a positive correlation with magnetic field strength and a negative correlation with magnetic axis tilt...


![[mdfiles/2504.16662.md|2504.16662]]
### AI Justification:
This paper is somewhat relevant to your interests as it explores magnetic field behavior in the context of TRAPPIST-1e, particularly focusing on "magnetic field intensity" and "structure" that can offer insights into "how magnetic fields behave" in astrophysical plasmas. However, while it addresses "magnetosphere structures" and consequences of "space weather conditions," the primary focus on habitability and radio emissions may not delve deeply into the "multi-scale dynamics of magnetic fields" you are particularly interested in.
# (205/382) http://arxiv.org/pdf/2504.08042v2


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Long-term evolution of the temperature structure in magnetized protoplanetary disks and its implication for the dichotomy of planetary composition
**Shoji Mori,Masanobu Kunitomo,Masahiro Ogihara**


#mhd
### Abstract:
The thermal structure and evolution of protoplanetary disks play a crucial role in planet formation. In addition to stellar irradiation, accretion heating is also thought to significantly affect the disk thermal structure and planet formation processes. We present the long-term evolution (from the beginning of Class II to disk dissipation) of thermal structures in laminar magnetized disks to investigate where and when accretion heating is a dominant heat source. In addition, we demonstrate that the difference in the disk structures affects the water content of forming planets. We considered the mass loss by magnetohydrodynamic (MHD) and photoevaporative disk winds to investigate the influence of wind mass loss on the accretion rate profile. Our model includes the recent understanding of accretion heating, that is, accretion heating in laminar disks is less efficient than that in turbulent disks because the surface is heated at optically thinner altitudes and energy is removed by disk winds. We find that accretion heating is weaker than irradiation heating at about 1--10 au even in the early Class II disk, but it can affect the temperature in the inner 1 au region. We also find that the magnetohydrodynamic wind mass loss in the inner region can significantly reduce the accretion rate compared with the rate in the outer region, which in turn reduces accretion heating. Furthermore, using evolving disk structures, we demonstrate that when accretion heating models are updated, the evolution of protoplanets is affected. In particular, we find that our model produces a dichotomy of the planetary water fraction of 1--10 $M_\oplus$ .


![[mdfiles/2504.08042.md|2504.08042]]
### AI Justification:
This paper is relevant to my research interests as it explores the "long-term evolution of thermal structures in laminar magnetized disks," which ties into my focus on magnetic dynamics and how they influence the behavior and evolution of plasmas. The investigation of "magnetohydrodynamic (MHD) wind mass loss" contributes to understanding the interactions between magnetic, gravitational, and thermal forces in shaping magnetic dynamics within astrophysical plasmas.
# (206/382) http://arxiv.org/pdf/2503.15792v3


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Turnstile area as a measure for chaotic transport in magnetic confinement fusion devices
**Christopher Berg Smiet,Ludovic Rais,Joaquim Loizu,Robert Davies**


#mhd
### Abstract:
We analyze stochasticity in the magnetic fields of magnetic confinement fusion reactors by calculating the lobe areas of turnstiles - a method developed for characterizing transport into and out of resonance zones in Hamiltonian dynamical systems. We develop an efficient algorithm based on an action principle to calculate this quantity directly from the magnetic field, including stellarator magnetic fields which are sourced by a complicated set of three-dimensional coils. In the analyzed devices, the turnstile area on the inboard (plasma-facing) manifolds is much smaller than the turnstile area on the outboard (wall-facing) manifolds. The application of the turnstile area calculation for the design of future reactors will be discussed.


![[mdfiles/2503.15792.md|2503.15792]]
### AI Justification:
The paper explores the stochastic behavior of magnetic fields in magnetic confinement fusion devices, which aligns with my interest in "Magnetic Field Amplification" and "Force Interactions Shaping Magnetic Dynamics." Specifically, the discussion of utilizing a turnstile area to analyze magnetic field dynamics reflects an innovative approach to understanding complex interactions in plasma environments, which could provide valuable insights for my research on magnetic fields in the interstellar medium.
# (207/382) http://arxiv.org/pdf/2504.08700v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Dont torque like that. Measuring compact object magnetic fields with analytic torque models
**J. J. R. Stierhof,E. Sokolova-Lapa,K. Berger,G. Vasilopoulos,P. Thalhammer,N. Zalot,...**


#mhd
### Abstract:
Context. Changes of the rotational period observed in various magnetized accreting sources are generally attributed to the interaction between the in-falling plasma and the large-scale magnetic field of the accretor. A number of models have been proposed to link these changes to the mass accretion rate, based on different assumptions on the relevant physical processes and system parameters. For X-ray binaries with neutron stars, with the help of precise measurements of the spin periods provided by current instrumentation, these models render a way to infer such parameters as the strength of the dipolar field and a distance to the system. Often, the obtained magnetic field strength values contradict those from other methods used to obtain magnetic field estimates. Aims. We want to compare the results of several of the proposed accretion models. To this end an example application of these models to data is performed. Methods. We reformulate the set of disk accretion torque models in a way that their parametrization are directly comparable. The application of the reformulated models is discussed and demonstrated using Fermi/GBM and Swift/BAT monitoring data covering several X-ray outbursts of the accreting pulsar 4U 0115+63. Results. We find that most of the models under consideration are able to describe the observations to a high degree of accuracy and with little indication for one model being preferred over the others. Yet, derived parameters from those models show a large spread. Specifically the magnetic field strength ranges over one order of magnitude for the different models. This indicates that the results are heavily influenced by systematic uncertainties.


![[mdfiles/2504.08700.md|2504.08700]]
### AI Justification:
This paper offers relevant insights into "magnetic field strength" and "interactions between the in-falling plasma and the large-scale magnetic field," which aligns with your interest in studying the dynamics of magnetic fields in plasma environments. Furthermore, the discussion of "models of accretion" and their "efficacy in describing observations" provides valuable context for understanding the complex interactions shaping magnetic dynamics in astrophysical plasmas.
# (208/382) http://arxiv.org/pdf/2504.05876v2


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Topological ignition of the stealth coronal mass ejections
**Yurii V. Dumin,Boris V. Somov**


#mhd
### Abstract:
One of hot topics in the solar physics are the so-called stealth coronal mass ejections (CME), which are not associated with any appreciable energy release events in the lower corona, such as the solar flares. It is often assumed recently that these phenomena might be produced by some specific physical mechanism, but no particular suggestions were put forward. It is the aim of the present paper to show that a promising explanation of the stealth CMEs can be based on the so-called topological ignition of the magnetic reconnection, when the magnetic null point is produced by a specific superposition of the remote sources (sunspots) rather than by the local current systems. As follows from our numerical simulations, the topological model explains very well all basic features of the stealth CMEs... (i) the plasma eruption develops without an appreciable heat release from the spot of reconnection, i.e., without the solar flare; (ii) the spot of reconnection (magnetic null point) can be formed far away from the location of the magnetic field sources; (iii) the trajectories of eruption are usually strongly curved, which can explain observability of CMEs generated behind the solar limb.


![[mdfiles/2504.05876.md|2504.05876]]
### AI Justification:
This paper explores the role of magnetic reconnection and topological effects in solar phenomena, which aligns with your interest in the "magnetic dynamics of plasmas" and the interactions between magnetic fields and plasma behavior. While it specifically focuses on the solar context, the insights into "topological ignition" and the dynamics of CMEs may offer valuable perspectives on "scale-dependent magnetic structuring" in broader astrophysical environments, particularly regarding force interactions in plasma.
# (209/382) http://arxiv.org/pdf/2504.06336v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The contribution of turbulent AGN coronae to the diffuse neutrino flux
**Damiano F. G. Fiorillo,Luca Comisso,Enrico Peretti,Maria Petropoulou,Lorenzo Sironi**


#mhd
### Abstract:
Active galactic nuclei (AGN) can accelerate protons to energies of $\sim$ 10-100 TeV, with secondary production of high-energy neutrinos. If the acceleration is driven by magnetized turbulence, the main properties of the resulting proton and neutrino spectra can be deduced based on insights from particle-in-cell simulations of magnetized turbulence. We have previously shown that these properties are consistent with the TeV~neutrino signal observed from the nearby active galaxy NGC 1068. In this work, we extend this result to a population study. We show that the produced neutrino flux depends mainly on the energetics of the corona -- the relative fraction of X-ray, magnetic, and non-thermal proton energy -- and on the spectral energy distribution of the AGN. We find that coronae with similar properties can explain neutrinos from the candidate AGN for which IceCube has reported an excess, albeit less significant than NGC 1068. Building on this framework, we show how the neutrino signal evolves with the AGN luminosity, and use this AGN sequence to predict the diffuse neutrino flux from the extragalactic population, showing that it can account for the diffuse neutrino signal observed by IceCube in the $\sim$ 1-100 TeV energy range.


![[mdfiles/2504.06336.md|2504.06336]]
### AI Justification:
This paper is somewhat relevant to your interests as it discusses the role of magnetized turbulence in the acceleration of protons and the production of high-energy neutrinos within active galactic nuclei (AGN), which aligns with your focus on "the interactions between magnetic... forces" in plasma environments. While it does not specifically address interstellar magnetic field dynamics, the use of simulations to understand "magnetized turbulence" may provide insights into "complex, emergent magnetic behaviors" relevant to your broader research in plasma physics.
# (210/382) http://arxiv.org/pdf/2504.05177v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A parametric study of solar wind properties and composition using fluid and kinetic solar wind models
**Paul Lomazzi,Alexis P. Rouillard,Michael A. Lavarra,Nicolas Poirier,Pierre-Louis Blelly,Jean-Baptiste Dakeyo,...**


#mhd
### Abstract:
The physical processes in the solar corona that shape the solar wind remain an active research topic. Modeling efforts have shown that energy and plasma exchanges near the transition region plays a crucial role in modulating solar wind properties. Although these regions cannot be measured in situ, plasma parameters can be inferred from coronal spectroscopy and ionization states of heavy ions, which remain unchanged as they escape the corona. We introduce a new solar wind model extending from the chromosphere to the inner heliosphere, capturing thermodynamic coupling across atmospheric layers. By including neutral and charged particle interactions, we model the transport and ionisation processes of the gas through the transition region, the corona and into the solar wind. Instead of explicitly modeling coronal heating, we link its spatial distribution to large-scale magnetic field properties. Our results confirm that energy deposition strongly affects wind properties through key mechanisms involving chromospheric evaporation, thermal expansion, and magnetic flux expansion. For sources near active regions, the model predicts significant solar wind acceleration, with plasma outflows comparable to those inferred from coronal spectroscopy. For winds from large coronal holes, the model reproduces the observed anticorrelation between charge state and wind speed. However, the predicted charge state ratios are overall lower than observed. Inclusion of a population of energetic electrons enhances both heavy ion charge states and solar wind acceleration, improving agreement with observations.


![[mdfiles/2504.05177.md|2504.05177]]
### AI Justification:
This paper is somewhat relevant to your interests as it investigates the interactions of magnetic fields with plasma dynamics in the solar wind, which aligns with your focus on "how magnetic fields behave, interact, and amplify across various scales." While the primary focus is on solar wind modeling and its thermodynamic aspects rather than directly studying magnetic field amplification or emergent dynamics in turbulent plasmas, it still provides insights into how "large-scale magnetic field properties" influence plasma behavior, which might have implications for understanding similar processes on interstellar scales.
# (211/382) http://arxiv.org/pdf/2504.02750v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Investigation of the influence of electrostatic excitation on instabilities and electron transport in ExB plasma configurations
**Maryam Reza,Farbod Faraji,Aaron Knoll,Benedict Rose**


#mhd
### Abstract:
Partially magnetized plasmas in ExB configurations - where the electric and magnetic fields are mutually perpendicular - exhibit a cross-field transport behavior, which is widely believed to be dominantly governed by complex instability-driven mechanisms. This phenomenon plays a crucial role in a variety of plasma technologies, including Hall thrusters, where azimuthal instabilities significantly influence electron confinement and, hence, device performance. While the impact of prominent plasma instabilities, such as the electron cyclotron drift instability (ECDI) and the modified two-stream instability (MTSI) on cross-field transport of electron species is well recognized and widely studied, strategies for actively manipulating these dynamics remain underexplored. In this study, we investigate the effect of targeted wave excitation on instability evolution and electron transport using one- and two-dimensional particle-in-cell simulations of representative plasma discharge configurations. A time-varying electric field is applied axially to modulate the spectral energy distribution of the instabilities across a range of forcing frequencies and amplitudes. Our results reveal that the so-called `unsteady forcing` can both suppress and amplify instability modes depending on excitation parameters. In particular, across both 1D and 2D simulation configurations, forcing near 40 MHz effectively reduces ECDI amplitude and decreases axial electron transport by about 30%, while high-frequency excitation near the electron cyclotron frequency induces spectral broadening, inverse energy cascades, and enhanced transport. These findings point to the role of nonlinear frequency locking and energy pathway disruption as mechanisms for modifying instability-driven transport. Our results offer insights into potential pathways to enhance plasma confinement and control in next-generation ExB devices.


![[mdfiles/2504.02750.md|2504.02750]]
### AI Justification:
This paper is somewhat relevant to my interests as it discusses "instability-driven mechanisms" and their impact on "electron transport" in the context of partially magnetized plasmas. However, it primarily focuses on electrostatic excitation in ExB configurations rather than directly addressing "magnetic field amplification" or how "magnetic fields behave and interact" in a broader astrophysical context, which is central to my research.
# (212/382) http://arxiv.org/pdf/2504.01061v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Encyclopedia Magneticum... Scaling Relations from Cosmic Dawn to Present Day
**Klaus Dolag,Rhea-Silvia Remus,Lucas M. Valenzuela,Lucas C. Kimmig,Benjamin Seidel,Silvio Fortune,...**


#mhd
### Abstract:
Galaxy and halo scaling relations, connecting a broad range of parameters, are well established from observations. The origin of many of these relations and their scatter is still a matter of debate. It remains a sizable challenge for models to simultaneously and self-consistently reproduce as many scaling relations as possible. We introduce the Magneticum Pathfinder hydrodynamical cosmological simulation suite, to date the suite that self-consistently covers the largest range in box volumes and resolutions. It is the only cosmological simulation suite that is tuned on the hot gas content of galaxy clusters instead of the stellar mass function. By assessing the successes and shortcomings of tuning to the hot gas component of galaxy clusters, we aim to further our understanding of the physical processes shaping the Universe. We analyze the importance of the hot and cold gas components for galaxy and structure evolution. We analyze 28 scaling relations, covering large-scale global parameters as well as internal properties for halos ranging from massive galaxy clusters down to galaxies, and show their predicted evolution from z=4 to z=0 in comparison with observations. These include the halo-to-stellar-mass and Kennicutt--Schmidt relations, the cosmic star formation rate density as well as the Fundamental Plane. Magneticum Pathfinder matches a remarkable number of the observed scaling relations from z=4 to z=0, including challenging relations like the number density of quiescent galaxies at cosmic dawn, the mass--size evolution, the mass--metallicity relation, the Magorrian relation, and the temperature--mass relation. We compile our data to allow for straightforward future comparisons. Galaxy properties and scaling relations arise naturally and the large scatter in observables at high redshift is crucial to distinguish the various galaxy formation models reproducing the z=0 relations.


![[mdfiles/2504.01061.md|2504.01061]]
### AI Justification:
This paper is somewhat relevant to your research interests as it discusses the "Magneticum Pathfinder" cosmological simulation suite, which could provide insights into the "magnetic dynamics of plasmas" and the "various scales" examined in your work. Additionally, while it primarily focuses on galaxy and halo scaling relations rather than specifically on magnetic field amplification and dynamics, it does analyze "physical processes shaping the Universe," which might offer some indirect insights into force interactions affecting magnetic fields in interstellar environments.
# (213/382) http://arxiv.org/pdf/2503.16857v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Observational Comparison Between Confined and Eruptive Flares... Magnetohydrodynamics Instability Parameters in a Similar Magnetic Configuration
**Kouhei Teraoka,Daiki Yamasaki,Yusuke Kawabata,Shinsuke Imada,Toshifumi Shimizu**


#mhd
### Abstract:
Unstable states of the solar coronal magnetic field structure result in various flare behaviors. In this study, we compared the confined and eruptive flares that occurred under similar magnetic circumstances in the active region 12673, on 2017 September 6, using the twist number, decay index, and height of magnetic field lines to identify observational behaviors of the flare eruption. We investigated the parameters from the magnetic field lines involved in an initial energy release, which were identified from the positions of the core of flare ribbons, i.e., flare kernels. The magnetic field lines were derived by nonlinear force-free field modeling calculated from the photospheric vector magnetic field obtained by the Solar Dynamics Observatory SDO/Helioseismic and Magnetic Imager, and flare kernels were identified from the 1600 angstrom data obtained by the SDO/Atmospheric Imaging Assembly. The twist number of all the magnetic field lines in the confined flare was below 0.6; however, the twist number in seven out of twenty-four magnetic field lines in the eruptive flare was greater than 0.6. These lines were tall. It is found that the decay index is not a clear discriminator of the confined and eruptive flares. Our study suggests that some magnetic field lines in the kink instability state may be important for eruptive flares, and that taller magnetic field lines may promote flare eruption.


![[mdfiles/2503.16857.md|2503.16857]]
### AI Justification:
This paper provides a detailed observational analysis of magnetic field dynamics related to solar flares, focusing on the "instability parameters" of magnetic field lines, which may resonate with your interest in "magnetic dynamics" and "force interactions." Although the context is specific to solar flares, the insights into how the "twist number" and structures of magnetic fields influence behavior could offer valuable analogies to your work on "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas."
# (214/382) http://arxiv.org/pdf/2503.18960v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Prototyping and Test of the `Canis` HTS Planar Coil Array for Stellarator Field Shaping
**D. Nash,D. A. Gates,W. S. Walsh,M. Slepchenkov,D. Guan,A. D. Cate,...**


#mhd
### Abstract:
Thea Energy, Inc. is currently developing the `Eos` planar coil stellarator, the Companys first integrated fusion system capable of forming optimized stellarator magnetic fields without complex and costly modular coils. To demonstrate the field shaping capability required to enable Eos, Thea Energy designed, constructed, and tested the `Canis` 3x3 array of high-temperature superconductor (HTS) planar shaping coils after successfully demonstrating a single shaping coil prototype. Through the Canis 3x3 magnet array program, Thea Energy manufactured nine HTS shaping coils and developed the cryogenic test and measurement infrastructure necessary to validate the arrays performance. Thea Energy operated the array at 20 K, generating several stellarator-relevant magnetic field shapes and demonstrating closed loop field control of the superconducting magnets to within 1% of predicted field, a margin of error acceptable for operation of an integrated stellarator. The Canis magnet array test campaign provides a proof of concept for HTS planar shaping coils as a viable approach to confining stellarator plasmas.


![[mdfiles/2503.18960.md|2503.18960]]
### AI Justification:
This paper is somewhat relevant to your interests in theoretical astrophysics and plasma physics, particularly in the context of magnetic field shaping within plasmas, as indicated by the phrase "optimizing stellarator magnetic fields." However, it primarily focuses on technical advancements related to the construction and testing of a specific magnetic field coil array rather than exploring the broader implications of magnetic field amplification and dynamics across scales, which is a key aspect of your research focus.
# (215/382) http://arxiv.org/pdf/2503.13292v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quantitative Image-Based Validation Framework for Assessing Global Coronal Magnetic Field Models
**Christopher E. Rura,Vadim M. Uritsky,Shaela I. Jones,Cooper Downs,Nathalia Alzate,Charles N. Arge**


#mhd
### Abstract:
Coronagraph observations provide key information about the orientation of the Suns magnetic field. Previous studies used quasi-radial features detected in coronagraph images to improve coronal magnetic field models by comparing the orientation of the features to the projected orientation of the model field. Various algorithms segment these coronal features to approximate the local plane-of-sky geometry of the coronal magnetic field, and their orientation can be used as input for optimizing and constraining coronal magnetic field models. We present a new framework that allows for further quantitative evaluations of image-based coronal segmentation methods against magnetic field models, and vice-versa. We compare quasi-radial features identified from QRaFT, a global coronal feature tracing algorithm, in white-light coronagraph images to outputs of MAS, an advanced magnetohydrodynamic model. We use the FORWARD toolset to produce synthetic polarized brightness images co-aligned to real coronagraph observations, segment features in these images, and quantify the difference between the inferred and model magnetic field. This approach allows us to geometrically compare features segmented in artificial images to those segmented in white-light coronagraph observations against the plane-of-sky projected MAS coronal magnetic field. We quantify QRaFTs performance in the artificial images and observational data, and perform statistical analyses that measure the similarity of these results to compute the accuracy and uncertainty of the model output to the observational data. The results demonstrate through a quantitative evaluation that a coronal segmentation method identifies the global large-scale orientation of the coronal magnetic field within $\sim\pm10^\circ$ of the plane-of-sky projected MAS magnetic field.


![[mdfiles/2503.13292.md|2503.13292]]
### AI Justification:
This paper is somewhat relevant to your research interests as it focuses on magnetic fields, specifically in the context of the Sun's corona, using quantitative evaluations to improve magnetic field models. While it primarily addresses the orientation of coronal magnetic fields rather than interstellar medium plasmas, the methods described for modeling and validating magnetic field orientations could provide insights into magnetic field amplification and dynamics that are relevant across astrophysical scales.
# (216/382) http://arxiv.org/pdf/2503.09553v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Observation of Fermi acceleration with cold atoms
**G. Barontini,V. Naniyil,J. P. Stinton,D. Reid,J. M. F. Gunn,H. M. Price,...**


#mhd
### Abstract:
Cosmic rays are deemed to be generated by a process known as ``Fermi acceleration`, in which charged particles scatter against magnetic fluctuations in astrophysical plasmas. The process itself is however universal, has both classical and quantum formulations, and is at the basis of dynamical systems with interesting mathematical properties, such as the celebrated Fermi-Ulam model. Despite its effectiveness in accelerating particles, Fermi acceleration has so far eluded unambiguous verifications in laboratory settings. Here, we realize the first fully controllable Fermi accelerator by colliding ultracold atoms against engineered movable potential barriers. We demonstrate that our Fermi accelerator, which is only 100 um in size, can produce ultracold atomic jets with velocities above half a meter per second. Adding dissipation, we also experimentally test Bells general argument for the ensuing energy spectra, which is at the basis of any model of cosmic ray acceleration. On the one hand, our work effectively opens the window to the study of high energy astrophysics with cold atoms, offering new capabilities for the understanding of phenomena such as diffusive acceleration at collisionless shocks. On the other, the performance of our Fermi accelerator is competitive with those of best-in-class accelerating methods used in quantum technology and quantum colliders, but with substantially simpler implementation and virtually no upper limit.


![[mdfiles/2503.09553.md|2503.09553]]
### AI Justification:
The paper's exploration of Fermi acceleration, a process linked to "charged particles scatter against magnetic fluctuations in astrophysical plasmas," aligns with your interest in "magnetic field amplification." Additionally, the mention of investigating phenomena such as "diffusive acceleration at collisionless shocks" offers insight into the dynamics between magnetic and gravitational forces that shape plasma behavior, making it relevant to your research on the interactions amongst these forces.
# (217/382) http://arxiv.org/pdf/2503.02433v3


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A Spectroastrometric Study of the Low-velocity Wind from DG Tau A
**Yu-Ru Chou,Michihiro Takami,Shin-Ping Lai,Emma Whelan,Noah B. Otten,Min Fang,...**


#mhd
### Abstract:
We obtained high spectral resolution spectra ( $\Delta v$ $\sim$ 2.5 km s $^{-1}$ ) for DG Tau A from 4800 \r{A} to 7500 \r{A} using Subaru High Dispersion Spectrograph (HDS) for the first time. The low-velocity components (LVCs, | $v$ | < 100 km s $^{-1}$ ) were observed in the [O I] 5577, 6300, 6364 \r{A}, [S II] 6716, 6731 \r{A} lines. The offset position spectra observed in the LVCs show a `negative velocity gradient`, supporting the presence of a wide-angled wind associated with the LVC emission. The offset position spectra observed in a component within the LVC velocity range between -16 km s $^{-1}$ to -41 km s $^{-1}$ , namely, LVC-M, show a `negative velocity gradient, supporting the presence of a wide-angled wind. With 12-70 au wind lengths measured using spectroastrometry, we estimate a lower limit to the wind mass-loss rate of $\sim$ 10 $^{-8}$ M $_\odot$ yr $^{-1}$ . In addition to the LVCs, we identify two high-velocity components (HVCs, | $v$ | > 100 km s $^{-1}$ ) associated with the collimated jet in 26 lines ([N I], [N II], [O I], [O II], [O III], [S II], [Ca II], [Fe II], H $\alpha$ , H $\beta$ , He I). The one with a clear spatial offset from the star ( $n_e$ $\sim$ 10 $^4$ cm $^{-3}$ , HVC1) is associated with an internal shock surface of the jet, while the other at the base ( $n_e$ $\sim$ 10 $^6$ cm $^{-3}$ , HVC2) may be a stationary shock component. We find that the observed line profiles and the spatial scales of the LVC emission do not agree with the existing predictions for photoevaporative or magnetohydrodynamical (MHD) disk winds. These could be explained by the X-wind model, but synthetic observations are required for detailed comparisons.


![[mdfiles/2503.02433.md|2503.02433]]
### AI Justification:
The paper is somewhat relevant to my research interests as it discusses the behavior of magnetic fields within the context of astrophysical plasmas, particularly through the lens of magnetohydrodynamical (MHD) disk winds and their interaction with low-velocity components. However, it primarily focuses on spectral observations of winds from DG Tau A without explicitly exploring the broader themes of magnetic field amplification or the multi-scale dynamics of magnetic fields which are central to my work.
# (218/382) http://arxiv.org/pdf/2503.05952v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### First detection of variable radio emission originating from the infant planetary system V1298 Tau
**M. Damasso,O. Morata,S. Kaur,D. Vigano,A. Melis,M. Murgia,...**


#mhd
### Abstract:
V1298 Tau is a very young and magnetically active star which hosts a benchmark multi-planetary system to study planet formation and evolutionary history at the earliest stages. We selected V1298 Tau for a first targeted follow-up at radio frequencies with the Karl G. Jansky Very Large Telescope (JVLA), the upgraded Giant Metrewave Radio Telescope (uGMRT), and the Sardinia Radio Telescope (SRT), to search for emission in the overall frequency range 0.55-7.2 GHz. Detecting radio emission from such a very active star is key to characterise its magnetosphere, allowing in principle to probe the strength of the coronal magnetic field and plasma density. Observations were carried out between Oct 2023 and Sept 2024... three epochs with uGMRT band-4 (0.55-0.75 GHz), 12 epochs with the JVLA using L (1-2 GHz) and C (4.5-6.5 GHz) bands, and three epochs with SRT using C-high band (6-7.2 GHz). We report the first detection of radio emission from V1298 Tau at different epochs using the JVLA. The emission has maximum peak flux densities of 91 $\pm$ 10 and 177 $\pm$ 6 $\mu$ Jy/beam in the L- and C-band, respectively. From a comparison with contemporary optical photometry, we found that the detected emission with the highest fluxes are located around a phase of minimum of the photospheric light curve. Although the uGMRT and SRT observations could not detect the source, we measured 3 $\sigma$ flux density upper limits in the range ~41-56 $\mu$ Jy/beam using uGMRT, while with SRT we reached upper limits down to 13 mJy. The lack of a significant fraction of circular polarisation indicates that the observed flux is not due to electron cyclotron maser emission from star-planet interaction, and it is likely produced by gyrosynchroton/cyclotron emission from the corona triggered by stellar magnetic activity, although we cannot exclude thermal emission due to a lack of constraints on the brightness temperature.


![[mdfiles/2503.05952.md|2503.05952]]
### AI Justification:
This paper is somewhat relevant to your interests in plasma physics and magnetic dynamics, particularly in its exploration of the "magnetically active star" V1298 Tau and the associated "magnetosphere." However, the focus on radio emissions and stellar magnetic activity does not directly address the broader complexities of magnetic field amplification or turbulent dynamics in interstellar plasma that you prioritize in your research.
# (219/382) http://arxiv.org/pdf/2503.04519v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Comparative study of small-scale magnetic fields on $ξ$ Boo A using optical and near-infrared spectroscopy
**A. Hahlin,O. Kochukhov,P. Chaturvedi,E. Guenther,A. Hatzes,U. Heiter,...**


#mhd
### Abstract:
Magnetic field investigations of Sun-like stars, using Zeeman splitting of non-polarised spectra, in the optical and H-band have found significantly different magnetic field strengths for the same stars, the cause of which is currently unknown. We aim to further investigate this issue by systematically analysing the magnetic field of $\xi$ Boo A, a magnetically active G7 dwarf, using spectral lines at different wavelengths. We used polarised radiative transfer accounting for the departures from local thermodynamic equilibrium to generate synthetic spectra. To find the magnetic field strengths in the optical, H-band, and K-band, we employed MCMC sampling analysis of high-resolution spectra observed with the spectrographs CRIRES $^+$ , ESPaDOnS, NARVAL, and UVES. We also determine the formation depth of different lines by calculating the contribution functions for each line employed in the analysis. We find that the magnetic field strength discrepancy between lines in the optical and H-band persists even when treating the different wavelength regions consistently. In addition, the magnetic measurements derived from the K-band appear to more closely align with the optical. The H-band appears to yield magnetic field strengths $\sim$ 0.4 kG with a statistically significant variation while the optical and K-band is stable at $\sim$ 0.6 kG for observations spanning about two decades. The contribution functions reveal that the optical lines form at a significantly higher altitude in the photosphere compared to those in the H- and K-band. While we find that the discrepancy remains, the variation of formation depths could indicate that the disagreement between magnetic field measurements obtained at different wavelengths is linked to the variation of the magnetic field along the line of sight and between different structures, such as star spots and faculae, in the stellar photosphere.


![[mdfiles/2503.04519.md|2503.04519]]
### AI Justification:
This paper investigates the magnetic fields of a Sun-like star, particularly focusing on "magnetic field strengths" using sophisticated spectroscopic methods, which aligns with my interest in "magnetic dynamics of plasmas." However, the study is mostly centered on a stellar context rather than the interstellar medium's dynamics or the multifaceted mechanisms driving magnetic field amplification across larger scales, making it only partially relevant.
# (220/382) http://arxiv.org/pdf/2503.03210v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The hot accretion flow evolution in the black hole X-ray binary MAXI J1348-630
**Hanji Wu,Wei Wang**


#mhd
### Abstract:
MAXI J1348-630 as a low-mass black hole binary system in the Galaxy showed an X-ray outburst in 2019. We analyzed the Insight-HXMT spectral data in the low hard state (LHS) and intermediate state (IS) during the outburst from MJD 58510 to 58519 at the energy band from 2 keV to 100 keV. During the entire process, a thin disk extending to the innermost stable circular orbit (ISCO) from a large truncated disk (truncated radius $> 5$ ISCO) suggests the corona geometry evolution. There exist time lags between radio and hard X-ray flux peaks... the 30 - 100 keV flux about 5 days ahead of radio flux, 11-30 keV flux about 4 days ahead, and reflection fraction about 2 days ahead, the accretion disk approaching the ISCO about 1 day before radio peak. This disk-corona-jet coupling and evolution suggest the corona containing two phases of cold dense material and hot gas, with high temperature region of corona cooling fast. The strong radio emission accompanying with a thin accretion disk of a relatively high accretion rate favors magnetic tower jet mechanism.


![[mdfiles/2503.03210.md|2503.03210]]
### AI Justification:
This paper is somewhat relevant to your research interests as it explores magnetic dynamics in the context of an accretion disk around a black hole, particularly mentioning the "magnetic tower jet mechanism," which aligns with your focus on "magnetic field amplification." However, the primary focus on observational data and specific black hole dynamics might limit its direct applicability to your theoretical modeling and plasma environments.
# (221/382) http://arxiv.org/pdf/2503.03387v1


### Rating: 6/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 60%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Novatron... Equilibrium and Stability
**Kristoffer Lindvall,Rickard Holmberg,Katarina Bendtz,Jan Scheffel,Johan Lundberg**


#mhd
### Abstract:
The Novatron is a fusion concept characterized by its axisymmetric mirror-cusp magnetic topology. The magnetic field exhibits good curvature and a high mirror ratio. Plasma equilibrium profiles for the Novatron are obtained by solving an axisymmetric guiding-center anisotropic boundary-value problem. These profiles are then analyzed with respect to several MHD stability criteria, including the mirror, firehose, and interchange conditions. A generalized Rosenbluth and Longmire MHD interchange criterion, where anisotropic pressure variations along flux tubes are allowed for, is subsequently employed for determining stable MHD equilibria. Additionally, a corresponding CGL double adiabatic interchange criterion is investigated for obtaining stable equilibria in the collisionless limit, both theoretically and numerically using the large scale Hybrid Particle-In-Cell code WarpX.


![[mdfiles/2503.03387.md|2503.03387]]
### AI Justification:
This paper is somewhat relevant to your interests, particularly through its examination of "plasma equilibrium profiles" and the various "MHD stability criteria." However, it does not directly address key themes such as "magnetic field amplification" or "emergent magnetic dynamics in turbulent plasmas," which are central to your research focus in theoretical astrophysics and magnetic dynamics.
# (222/382) http://arxiv.org/pdf/2502.03577v3


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Multidisciplinary Science in the Multimessenger Era
**Eric Burns,Christopher L. Fryer,Ivan Agullo,Jennifer Andrews,Elias Aydi,Matthew G. Baring,...**


#mhd
### Abstract:
Astrophysical observations of the cosmos allow us to probe extreme physics and answer foundational questions on our universe. Modern astronomy is increasingly operating under a holistic approach, probing the same question with multiple diagnostics including how sources vary over time, how they appear across the electromagnetic spectrum, and through their other signatures, including gravitational waves, neutrinos, cosmic rays, and dust on Earth. Astrophysical observations are now reaching the point where approximate physics models are insufficient. Key sources of interest are explosive transients, whose understanding requires multidisciplinary studies at the intersection of astrophysics, gravity, nuclear science, plasma physics, fluid dynamics and turbulence, computation, particle physics, atomic, molecular, and optical science, condensed matter and materials science, radiation transport, and high energy density physics. This white paper provides an overview of the major scientific advances that lay at the intersection of physics and astronomy and are best probed through time-domain and multimessenger astrophysics, an exploration of how multidisciplinary science can be fostered, and introductory descriptions of the relevant scientific disciplines and key astrophysical sources of interest.


![[mdfiles/2502.03577.md|2502.03577]]
### AI Justification:
This paper possesses some relevance due to its interdisciplinary approach and mention of plasma physics, fluid dynamics, and turbulence, which align with your interest in "Emergent Magnetic Dynamics in Turbulent Plasmas." However, it lacks a direct focus on magnetic field amplification or specific mechanisms driving magnetic dynamics in plasmas, which are crucial elements of your research interests.
# (223/382) http://arxiv.org/pdf/2505.00435v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Modeling Metric Gyrosynchrotron Radio Emission From the Quiet Solar Corona
**Kamen Kozarev,Mohamed Nedal**


#mhd
### Abstract:
The radio emission of the quiet Sun in the metric and decametric bands has not been well studied historically due to limitations of existing instruments. It is nominally dominated by thermal brehmsstrahlung of the solar corona, but may also include significant gyrosynchrotron emission, usually assumed to be weak under quiet conditions. In this work, we investigate the expected gyrosynchrotron contribution to solar radio emission in the lowest radio frequencies observable by ground instruments, for different regions of the low and middle corona. We approximate the coronal conditions by a synoptic magnetohydrodynamic (MHD) model. The thermal emission is estimated from a forward model based on the simulated corona. We calculate the expected gyrosynchrotron emission with the Fast Gyrosynchrotron Codes framework by Fleishman & Kuznetsov (2010). The model emissions of different coronal regions are compared with quiet-time observations between 20-90 MHz by the LOw Frequency ARray (LOFAR) radio telescope. The contribution of gyrosynchrotron radiation to low frequency solar radio emission may shed light on effects such as the hitherto unexplained brightness variation observed in decametric coronal hole emission, and help constrain measurements of the coronal magnetic fields. It can also improve our understanding of electron populations in the middle corona and their relation to the formation of the solar wind.


![[mdfiles/2505.00435.md|2505.00435]]
### AI Justification:
This paper may have partial relevance to your research interests, particularly in its investigation of magnetic fields in the solar corona and their effects on radio emissions, as it mentions "constrain measurements of the coronal magnetic fields," which aligns with your focus on "magnetic field amplification" and "force interactions shaping magnetic dynamics." However, its emphasis on solar emissions and observations does not directly cater to your primary interests in interstellar medium and multi-scale plasma dynamics.
# (224/382) http://arxiv.org/pdf/2504.18350v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Characterizing the Impact of Alfvén Wave Forcing in Interplanetary Space on the Distribution of near-Earth Solar Wind Speeds
**B. L. Alterman**


#mhd
### Abstract:
Broadly, solar wind source regions can be classified by their magnetic topology as intermittently and continuously open to the heliosphere. Early models of solar wind acceleration do not account for the fastest, non-transient solar wind speeds observed near-Earth and energy must be deposited into the solar wind after it leaves the Sun. Alfv\en wave energy deposition and thermal pressure gradients are likely candidates and the relative contribution of each acceleration mechanism likely depends on the source region. Although solar wind speed is a rough proxy for solar wind source region, it cannot unambiguously identify source region topology. Using near-Sun observations of the solar winds kinetic energy flux, we predict the expected kinetic energy flux near-Earth. This predicted kinetic energy flux corresponds to the range of solar wind speeds observed in the fast solar wind and infer that the solar winds near-Sun kinetic energy flux is sufficient to predict the distribution of fastest, non-transient speeds observed near Earth. Applying a recently developed model of solar wind evolution in the inner heliosphere, we suggest that the acceleration required to generate this distribution of fastest, non-transient speeds is likely due to the continuous deposition of energy by Alfv\en wave forcing during the solar winds propagation through interplanetary space. We infer that the solar winds Alfv\enicity can statistically map near-Earth observations to their source regions because the Alfv\en wave forcing that the solar wind experiences in transit is a consequence of the source region topology.


![[mdfiles/2504.18350.md|2504.18350]]
### AI Justification:
The paper explores the role of Alfvén wave forcing in understanding solar wind dynamics, which touches on the broader theme of magnetic field interactions in plasma environments, a key aspect of your research focus. Although it primarily deals with solar wind speeds rather than magnetic behavior on larger scales, the mention of energy deposition and source region topology indirectly relates to your interest in "Force Interactions Shaping Magnetic Dynamics" and may provide insights into magnetic field amplification mechanisms.
# (225/382) http://arxiv.org/pdf/2504.14984v2


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A New Formation Mechanism of Counterstreaming Mass Flows in Filaments and the Doppler Bullseye Pattern in Prominences
**Chengrui Zhou,Yuandeng Shen,Chun Xia,Dongxu Liu,Zehao Tang,Surui Yao**


#mhd
### Abstract:
The eruption of solar prominences can eject substantial mass and magnetic field into interplanetary space and cause geomagnetic storms. However, various questions about prominences and their eruption mechanism remain unclear. In particular, what causes the intriguing Doppler bullseye pattern in prominences has not yet been solved, despite some preliminary studies proposing that they are probably associated with counterstreaming mass flows. Previous studies are mainly based on single-angle and short timescale observations, making it difficult to determine the physical origin of Doppler bullseye patterns in prominences. Here, taking advantage of stereoscopic observations taken by the Solar Dynamics Observatory and the Solar Terrestrial Relations Observatory and a three-dimensional numerical simulation, we investigate the origin of prominence Doppler bullseye pattern by tracing a long-lived transequatorial filament/prominence from July 23 to August 4, 2012. We find that repeated coronal jets at one end of the prominence can launch the Doppler bullseye pattern. It is evidenced in our observations and simulation that during the forward traveling of jet plasma along the helical magnetic field structure of the prominence, part of the ejecting plasma can not pass through the apex of the prominence due to the insufficient kinetic energy and therefore forms a backward-moving mass flow along the same or neighboring magnetic field lines. This process finally forms counterstreaming mass flows in on-disk filaments. When the on-disk filament rotates to the solar limb to be a prominence, the counterstreaming mass flows are naturally observed as a Doppler bullseye pattern.


![[mdfiles/2504.14984.md|2504.14984]]
### AI Justification:
This paper discusses the dynamics of magnetic fields and mass flows in solar prominences, which relates to your interest in "how magnetic fields behave, interact, and amplify" within plasma environments. Although the focus is primarily on solar phenomena rather than the interstellar medium, the mechanisms of magnetic field interactions and the role of force dynamics in shaping these flows offer relevant insights into the broader context of magnetic field amplification and structure within plasmas.
# (226/382) http://arxiv.org/pdf/2502.20820v2


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Chinese pulsar timing array data release I. Polarimetry for 56 millisecond pulsars
**Jiangwei Xu,Jinchen Jiang,Heng Xu,Bojun Wang,Zihan Xue,Siyuan Chen,...**


#mhd
### Abstract:
We present polarization pulse profiles for 56 millisecond pulsars (MSPs) monitored by the Chinese Pulsar Timing Array (CPTA) collaboration using the Five-hundred-meter Aperture Spherical radio Telescope (FAST). The observations centered at 1.25 GHz with a raw bandwidth of 500 MHz. Due to the high sensitivity ( $\sim$ 16 K/Jy) of the FAST telescope and our long integration time, the high signal-to-noise ratio polarization profiles show features hardly detected before. Among 56 pulsars, the polarization profiles of PSRs J0406 $+$ 3039, J1327 $+$ 3423, and J2022 $+$ 2534 were not previously reported. 80\% of MSPs in the sample show weak components below 3\% of peak flux, 25\% of pulsars show interpulse-like structures, and most pulsars show linear polarization position angle jumps. Six pulsars seem to be emitting for full rotation phase, with another thirteen pulsars being good candidates for such a 360 $^\circ$ radiator. We find that the distribution of the polarization percentage in our sample is compatible with the normal pulsar distribution. Our detailed evaluation of the MSP polarization properties suggests that the wave propagation effects in the pulsar magnetosphere are important in shaping the MSP polarization pulse profiles.


![[mdfiles/2502.20820.md|2502.20820]]
### AI Justification:
The paper focuses on the polarization characteristics of millisecond pulsars and their associated magnetic fields, which could indirectly relate to aspects of magnetic dynamics and amplification in astrophysical plasmas, aligning with my interests in "magnetic dynamics of plasmas in the interstellar medium." However, it does not explicitly address the mechanisms driving magentic field amplification or the interactions shaping magnetic dynamics in wider plasma environments; thus, its relevance is limited.
# (227/382) http://arxiv.org/pdf/2504.14049v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### What determines the brightness of magnetically open solar corona?... Insights from three-dimensional radiative MHD simulations and observations
**Haruhisa Iijima**


#mhd
### Abstract:
We investigate the relationship between solar coronal holes and open-field regions using three-dimensional radiative magnetohydrodynamic (MHD) simulations combined with remote-sensing observations from the Solar Dynamics Observatory (SDO). Our numerical simulations reveal that magnetically open regions in the corona can exhibit brightness comparable to quiet regions, challenging the conventional view that open-field regions are inherently dark coronal holes. We find that the coronal brightness is primarily determined by the total energy input from photospheric magnetic activities, such as the small-scale dynamo, rather than differences in dissipative processes within the corona. Using synthesized EUV intensity maps, we show that brightness thresholds commonly used to identify coronal holes may overlook open-field regions, especially at lower spatial resolutions. Observational analysis utilizing SDO/HMI and AIA synoptic maps supports our simulation results, demonstrating that magnetic field extrapolation techniques, such as the Potential Field Source Surface (PFSS) model, are sensitive to the chosen parameters, including the source surface height. We suggest that discrepancies in estimates of open magnetic flux (the ``open flux problem) arise both from the modeling assumptions in coronal magnetic field extrapolation and systematic biases in solar surface magnetic field observations. Our findings indicate the need for reconsidering criteria used to identify coronal holes as indicators of open-field regions to better characterize the solar open magnetic flux.


![[mdfiles/2504.14049.md|2504.14049]]
### AI Justification:
While the paper primarily focuses on the solar corona, it utilizes three-dimensional radiative magnetohydrodynamic (MHD) simulations to explore magnetic field behaviors that could provide insights into broader magnetic dynamics within plasma environments. The findings related to the interaction of photospheric magnetic activities and their amplification, as well as the implications for identifying open magnetic flux, may resonate with your interest in "magnetic field amplification" and the role of dynamical processes in shaping magnetic fields across various scales.
# (228/382) http://arxiv.org/pdf/2504.13678v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Effect of micromagnetorotation on a micropolar magnetohydrodynamic blood flow in a 3D stenosed artery
**Kyriaki-Evangelia Aslani,Ioannis E. Sarris,Efstratios Tzirtzilakis**


#mhd
### Abstract:
This study presents a numerical investigation of a 3D micropolar magnetohydrodynamic (MHD) blood flow through stenosis, with and without the effects of micromagnetorotation (MMR). MMR refers to the magnetic torque caused by the misalignment of the magnetization of magnetic particles in the fluid with the magnetic field, which affects the internal rotation (microrotation) of these particles. Blood can be modeled as a micropolar fluid with magnetic particles due to the magnetization of erythrocytes. In this manner, this study analyzes important flow features, i.e., streamlines, vorticity, velocity, and microrotation, under varying stenosis (50%, 80%), hematocrit levels (25%, 45%), and magnetic fields (1T, 3T, 8T), using two newly developed transient OpenFOAM solvers epotMicropolarFoam and epotMMRFoam. Results indicate that micropolar effects become more pronounced at severe stenosis due to the significant reduction in artery size. Furthermore, when MMR is disregarded (i.e., when blood is modeled as a classical MHD micropolar fluid without magnetic particles), the magnetic field does not significantly alter blood flow, regardless of its intensity, due to the minimal impact of the Lorentz force on blood. Conversely, MMR substantially affects blood flow, particularly at higher hematocrit levels and severe stenoses, leading to reductions of up to 30% in velocity and vorticity and up to 99.9% in microrotation. Simultaneously, any vortices or disturbances are dampened. These findings underscore the critical role of MMR (which was ignored so far) in altering flow behavior in stenosed arteries, suggesting that it should be considered in future MHD micropolar blood flow studies.


![[mdfiles/2504.13678.md|2504.13678]]
### AI Justification:
This paper is somewhat relevant to your interests in theoretical astrophysics and plasma physics, specifically the study of magnetic dynamics. Although the focus is on micropolar magnetohydrodynamic blood flow, the investigation of "micromagnetorotation" and its effect on magnetic behaviors shares a conceptual link with your interests in "magnetic dynamics of plasmas" and how "magnetic fields behave" under varying conditions.
# (229/382) http://arxiv.org/pdf/2504.04165v2


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Charged particle motion in a strong magnetic field... Applications to plasma confinement
**Ugo Boscain,Wadim Gerner**


#mhd
### Abstract:
We derive the zero order approximation of a charged particle under the influence of a strong magnetic field in a mathematically rigorous manner and clarify in which sense this approximation is valid. We use this to further rigorously derive a displacement formula for the pressure of plasma equilibria and compare our findings to results in the physics literature. The main novelty of our results is a qualitative estimate of the confinement time for optimised plasma equilibria with respect to the gyro frequency. These results are of interest in the context of plasma fusion confinement.


![[mdfiles/2504.04165.md|2504.04165]]
### AI Justification:
The paper explores the motion of particles in a strong magnetic field, which is foundational to understanding magnetic dynamics in astrophysical plasmas—particularly under the context of "magnetic field amplification." While the focus is primarily on plasma confinement relevant to fusion, the mathematical rigor in deriving displacement formulas for plasma equilibria may provide insights into the "interactions between magnetic forces and plasma behaviors" that could align with my research interests.
# (230/382) http://arxiv.org/pdf/2504.12375v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Effects of Eccentricity on Accreting Binary Black Holes... MHD Simulations in Full GR Reveal Novel Periodicities in Jet Power and Synchrotron Spectra
**Vikram Manikantan,Vasileios Paschalidis,Gabriele Bozzola**


#mhd
### Abstract:
We perform simulations of magnetohydrodynamic accretion onto equal-mass, non-spinning binary black holes in 3+1 full general relativity addressing the effects of orbital eccentricity. We find that binary black holes with non-negligible eccentricity accrete matter with periodicity that matches the binary orbital period, whereas quasi-circular binaries exhibit accretion rate modulation at approximately $\sim 0.7\times$ their binary orbital period. Additionally, we find that the total jet luminosity is modulated at the orbital period for eccentric binaries, while quasi-circular binaries only exhibit long-term modulations. We perform a radiative transfer calculation of the dual jet synchrotron emission and demonstrate that the optically thin synchrotron emission varies on the binary orbital period for eccentric binaries. Moreover, eccentric binaries spend more time in a low state, where the synchrotron emission is minimum, than in a high state, where the synchrotron emission peaks. The quasi-circular binary also exhibits variability in its optically thin synchrotron emission but the exact frequency of variability does not appear robust against different parameters. Our suite of simulations is an essential step towards providing a comprehensive catalog of multi-messenger theoretical models that will enable studies of supermassive binary black holes detectable across the electromagnetic and gravitational wave spectra.


![[mdfiles/2504.12375.md|2504.12375]]
### AI Justification:
This paper discusses "magnetohydrodynamic accretion" and the "modulation of synchrotron emission," which can provide insights into magnetic field dynamics in accreting systems relevant to my interest in the magnetic behavior of plasmas. Although the focus is on binary black holes rather than the interstellar medium, the findings on "jet luminosity" and "accretion rate modulation" could inform the broader understanding of magnetic interactions and turbulence in astrophysical plasmas.
# (231/382) http://arxiv.org/pdf/2504.11263v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Discovery of a bimodal luminosity distribution in persistent Be/X-ray pulsar 2RXP J130159.6-635806
**Alexander Salganik,Sergey S. Tsygankov,Maria Chernyakova,Denys Malyshev,Juri Poutanen**


#mhd
### Abstract:
We present a comprehensive analysis of 2RXP J130159.6-635806, a persistent low-luminosity Be/X-ray pulsar, focusing on its transition to a spin equilibrium state and the discovery of a bimodal luminosity distribution revealing possibly a new accretion regime. Using data from NuSTAR, Swift, XMM-Newton, and Chandra observatories, we investigate changes in the pulsars timing and spectral properties. After more than 20 years of continuous spin-up, the pulsars spin period stabilized, marking the onset of spin equilibrium. This transition was accompanied by the emergence of a previously unobserved accretion regime at $L_{\rm bol} = (2.0_{-1.0}^{+2.3})\times 10^{34}$ erg s $^{-1}$ , an order of magnitude lower than its earlier quiescent state. After that, the source occasionally switched between these regimes, remaining in each state for extended periods, with the transition time from a luminosity of $10^{35}$ erg s $^{-1}$ to $10^{34}$ erg s $^{-1}$ taking less than 2.3 day. The analysis of the spectral data collected during this new low-luminosity state revealed a two-hump shape which is different from the cutoff power-law spectra observed at higher luminosities. The discovery of pulsations in this state, together with the hard spectral shape, demonstrates ongoing accretion. We estimate the magnetic field strength to be $\sim 10^{13}$ G based on indirect methods. Additionally, we report a hint of a previously undetected $\sim$ 90-day orbital period in the system.


![[mdfiles/2504.11263.md|2504.11263]]
### AI Justification:
This paper is somewhat relevant to your research interests as it discusses magnetic fields in relation to a Be/X-ray pulsar, mentioning an estimated magnetic field strength of ∼10^13 G which ties into your focus on "magnetic dynamics of plasmas." However, the paper primarily concentrates on pulsar luminosity distribution and timing properties rather than the intricate dynamics and force interactions of magnetic fields in astrophysical plasmas, which may cloud its applicability to your research focus.
# (232/382) http://arxiv.org/pdf/2504.11283v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Influence of the magnetic activity cycle on mean density and acoustic radius inversions
**Jerome Betrisey,Daniel R. Reese,Sylvain N. Breton,Anne-Marie Broomhall,Anish M. Amarsi,Rafael A. Garcia,...**


#mhd
### Abstract:
Asteroseismic modelling is crucial for upcoming missions like PLATO, CubeSpec, and Roman. Despite significant progress, discrepancies between observations and theoretical predictions introduce biases in stellar characterisation at the precision required by PLATO. Current models typically ignore magnetic activity, assuming its effects are hidden within surface effects. However, recent studies have shown significant impacts of magnetic activity on the Suns asteroseismic characterisation using forward modelling. Using GOLF and BiSON observations of two full solar activity cycles, we quantified the impact of magnetic activity on solar mean density and acoustic radius inversions. Observations were segmented into yearly overlapping snapshots, each offset by 91.25 days. Inversions were performed for each snapshot to determine mean density and acoustic radius, tracking their temporal evolution and estimating systematic uncertainty due to magnetic activity. We observed a clear imprint of the magnetic activity cycle on solar mean density and acoustic radius through helioseismic inversions, consistent across GOLF and BiSON datasets. This imprint is the largest source of systematic uncertainty in solar asteroseismic characterisation. Including low radial-order modes mitigates these effects more significantly than previously measured for other stellar variables. We recommend asteroseismic values for solar mean density (1.4104 \pm 0.0051 g/cm3) and acoustic radius (3722.0 \pm 4.1 s), averaged over two activity cycles. These values account for major systematic errors, achieving high precision (0.36% for mean density and 0.11% for acoustic radius). These results are promising for high-precision characterisation of Sun-like stars, a better-constrained mean density being able to enhance the precision of stellar radius estimate, which is crucial for exoplanetary system characterisation.


![[mdfiles/2504.11283.md|2504.11283]]
### AI Justification:
This paper discusses the significant effects of magnetic activity cycles on solar density and acoustic inversions, which indirectly relates to your research on magnetic field dynamics in plasma environments. However, it primarily focuses on asteroseismic modeling rather than the broader contexts of magnetic field amplification and emergent dynamics in interstellar plasmas, making it only partially relevant to your interests.
# (233/382) http://arxiv.org/pdf/2504.11215v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Observational Study of Recurrent Jets... Evolution of Magnetic Flux, Current, and Helicity
**Chang Zhou,Yang Guo,Guoyin Chen,Ye Qiu,M. D. Ding**


#mhd
### Abstract:
We observed three recurrent blowout jets in an active regio with Atmospheric Imaging Assembly (AIA) aboard the Solar Dynamics Observatory (SDO). Using Helioseismic Magnetic Imager (HMI) data. We found that the magnetic flux of an emerging negative pole increases steadily before declining just as the jets erupt. Certain physical quantities, like the total unsigned vertical current, align with the periodicity of the jets. The differential affine velocity of the vector magnetograms reveals strong shear around the negative pole. The Doppler velocity map, calculated from the H $\alpha$ spectra observed by the Chinese H $\alpha$ Solar Explorer (CHASE), shows upflows with large initial velocity before it can be observed by AIA. The magnetic field derived from the nonlinear force-free field (NLFFF) model suggests a topology akin to fan-spine structure, consistent with AIA images. We calculated the evolution of volumetric helicity ratio using the NLFFF model and found its phase aligns with the jet flux in AIA 171 \AA. These results suggest that recurrent jets may be triggered by the accumulation and release of energy and helicity, driven by emergence, shearing and cancellation of photospheric magnetic field.


![[mdfiles/2504.11215.md|2504.11215]]
### AI Justification:
The paper's relevance to your interests is moderate as it investigates the "evolution of magnetic flux" and "volumetric helicity ratio," which ties into your focus on "magnetic field amplification" and how those fields evolve in plasma environments. However, while the study addresses fundamental concepts of magnetic dynamics, the context of solar jets may not fully align with the broader interstellar medium focus you outlined.
# (234/382) http://arxiv.org/pdf/2504.09144v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic energies (and some other parameters) in solar active regions of different Hale and McIntosh classes... statistical analysis for 2010-2024
**I. V. Zimovets,I. N. Sharykin,W. -Q. Gan**


#mhd
### Abstract:
A statistical analysis of magnetic energies of the nonlinear force-free and potential fields, and their difference (a proxy for the free magnetic energy) in active regions (ARs) on the Sun of different Hale (Mount Wilson) and McIntosh classes for the period from May 1, 2010 to June 12, 2024 is presented. The magnetic fields in ARs are calculated using the GX Simulator based on the information about ARs contained in the daily Solar Region Summary (SRS) files provided by the NOAA SWPC and vector magnetograms by the Helioseismic and Magnetic Imager (HMI) onboard the Solar Dynamics Observatory (SDO). Total unsigned and signed magnetic fluxes and vertical electric currents on the photosphere are also calculated. For the parameters considered, distributions have been determined in total for all ARs and separately for each Hale and McIntosh class. Minimum, maximum, mean values of the parameters and standard deviations were calculated for each class. The information about the parameters is presented in the form of graphs and tables. The magnetic energies, unsigned magnetic flux, unsigned vertical current, as well as the integral number of sunspots, number of ARs, and area of sunspots, integrated over ARs visible per day on the solar disk, exhibit similar approximately 11.6-year cyclicity. On average, magnetic energies of ARs increase with increasing Hale and McIntosh class, while the average fraction of the free magnetic energy in ARs of different classes differs weakly. We also found that the Poisson Flare Probabilities (PFPs) correlate with the parameters, and the Pearson correlation coefficient is up to 0.89. The results reveal relationships between various parameters of ARs and may be used in developing prediction of space weather effects.


![[mdfiles/2504.09144.md|2504.09144]]
### AI Justification:
The paper provides valuable insights into the statistical relationships between magnetic energies and solar active regions, encompassing dynamics relevant to "magnetic field amplification" and the "interaction between magnetic, gravitational, and thermal forces" as seen in solar environments. While its primary focus is on solar phenomena, the findings on the amplification and cyclicity of magnetic energies in active regions could offer comparative insights into magnetic dynamics in broader astrophysical plasma contexts, aligning moderately with your interest in force interactions shaping magnetic dynamics in complex environments.
# (235/382) http://arxiv.org/pdf/2504.08990v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### X-ray spectro-polarimetry analysis of the weakly magnetized neutron star X-ray binary GX 9+1
**Antonella Tarana,Fiamma Capitanio,Andrea Gnarini,Sergio Fabiani,Francesco Ursini,Stefano Bianchi,...**


#mhd
### Abstract:
We present an X-ray spectro-polarimetric study of the weakly magnetized neutron star low-mass X-ray binary GX 9+1, utilizing data from the Imaging X-ray Polarimetry Explorer (IXPE), alongside simultaneous NuSTAR, NICER, and INTEGRAL observations. GX 9+1, located in the Galactic bulge, is a persistently bright Atoll source known for its spectral variability along the color-color diagram. Our spectral analysis during the soft state confirms emission dominated by a soft blackbody and thermal Comptonization components, with no evidence of a hard X-ray tail. These observations suggest a relatively low-inclination system (23 deg < i < 46 deg) with a weak reflection component, consistent with emission from the accretion disk and neutron star boundary layer. Spectro-polarimetric analysis reveals no significant polarization in the 2-8 keV range, with a 3-sigma upper limit for the polarization degree of 1.9%. However, marginal evidence of polarization was detected in the 2-3 keV band at the 95.5% confidence level (2-sigma), suggesting potential contributions from scattering effects in the individual spectral components (disk, reflection, and Comptonization) that could cancel each other out due to the different orientations of their polarization angles. This behavior aligns with other Atoll sources observed by IXPE, which typically exhibit lower and less variable polarization degrees compared to Z-class sources.


![[mdfiles/2504.08990.md|2504.08990]]
### AI Justification:
This paper provides insight into the magnetic dynamics of a weakly magnetized neutron star through X-ray spectro-polarimetry, which may offer indirect implications for magnetic field behavior in astrophysical plasmas. While it primarily focuses on the observational aspects of X-ray binary systems, the exploration of polarization and its potential scattering effects could relate to the broader theme of "magnetic dynamics" within your interest in the amplification and interaction of magnetic fields in plasma environments.
# (236/382) http://arxiv.org/pdf/2504.08926v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Constraints on QCD-based equation of state of quark stars from neutron star maximum mass, radius, and tidal deformability observations
**Joao V. Zastrow,Jonas P. Pereira,Rafael C. R. de Lima,Jorge E. Horvath**


#mhd
### Abstract:
(Abridged) Neutron stars (NSs), the densest known objects composed of matter, provide a unique laboratory to probe whether strange quark matter is the true ground state of matter. We investigate the parameter space of the equation of state of strange stars using a quantum chromodynamics (QCD)-informed model. The parameters - related to the energy density difference between quark matter and the QCD vacuum, the strength of strong interactions, and the gap parameter for color superconductivity - are sampled via quasi-random Latin hypercube sampling to ensure uniform coverage. To constrain them, we incorporate observational data on the maximum mass of NSs (from binary and merger systems), the radii of $1.4$ M $_{\odot}$ NSs (from gravitational wave and electromagnetic observations), and tidal deformabilities (from GW170817). Our results show that quark strong interactions play a key role, requiring at least a $20\%$ deviation from the free-quark limit. We also find that color superconductivity is relevant, with the gap parameter reaching up to $\sim 84$ MeV for a strange quark mass of $100$ MeV. The surface-to-vacuum energy density jump lies in the range $(1.1-1.3)$ $\rho_{\rm{sat}}$ , where $\rho_{\rm{sat}} \simeq 2.7 \times 10^{14} $ g cm $ ^{-3} $ . Observational constraints also imply that a $ 1.4$ M $_{\odot}$ quark star has a radius of $(11.5-12.3)$ km and tidal deformability between $670$ and $970$ . These are consistent with the low mass and radius inferred for the compact object XMMU J173203.3-344518. Our results provide useful inputs for future studies on quark and hybrid stars, including their tidal properties, thermal evolution, quasi-normal modes, and ellipticities.


![[mdfiles/2504.08926.md|2504.08926]]
### AI Justification:
This paper focuses on the equation of state of quark stars and how their properties relate to magnetic fields under extreme gravitational conditions, which indirectly connects to my interest in "the interactions between magnetic, gravitational, and thermal forces" within dense astrophysical plasmas. However, the specific emphasis on quark matter and neutron star constraints suggests limited direct relevance to my focus on magnetic dynamics in interstellar plasmas and turbulence.
# (237/382) http://arxiv.org/pdf/2504.08346v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Stochastic surfing turbulent vorticity
**Ziqi Wang,Xander M. de Wit,Roberto Benzi,Chunlai Wu,Rudie P. J. Kunnen,Herman J. H. Clercx,...**


#mhd
### Abstract:
The chaotic dynamics of small-scale vorticity plays a key role in understanding and controlling turbulence, with direct implications for energy transfer, mixing, and coherent structure evolution. However, measuring or controlling its dynamics remains a major conceptual and experimental challenge due to its transient and chaotic nature. Here we use a combination of experiments, theory and simulations to show that small magnetic particles of different densities, exploring flow regions of distinct vorticity statistics, can act as effective probes for measuring and forcing turbulence at its smallest scale. The interplay between the magnetic torque, from an externally controllable magnetic field, and hydrodynamic stresses, from small-scale turbulent vorticity, reveals an extremely rich phenomenology. Notably, we present the first observation of stochastic resonance for particles in turbulence... turbulent fluctuations, effectively acting as noise, counterintuitively enhance the particle rotational response to external forcing. We identify a pronounced resonant peak in particle rotational phase-lag when the applied magnetic field matches the characteristic intensity of small-scale vortices. Furthermore, we uncover a novel symmetry-breaking mechanism... an oscillating magnetic field with zero-mean angular velocity remarkably induces net particle rotation in turbulence with zero-mean vorticity, as turbulent fluctuations aid the particle in `surfing` the magnetic field. Our findings offer insights into flexible particle manipulation in complex flows and open up a novel magnetic resonance-based approach for measuring vorticity... magnetic particles as probes emit detectable magnetic fields, enabling turbulence quantification even under optically-inaccessible conditions.


![[mdfiles/2504.08346.md|2504.08346]]
### AI Justification:
This paper presents insights into the "chaotic dynamics of small-scale vorticity" and its influence on "turbulence," which aligns with your interest in how "magnetic fields interact with turbulence" and contribute to emergent magnetic behaviors within plasma structures. Additionally, the exploration of the interplay between "magnetic torque" and turbulent vorticity suggests a nuanced understanding of "force interactions shaping magnetic dynamics," which is central to your research focus on the magnetic behavior of plasmas in astrophysical contexts.
# (238/382) http://arxiv.org/pdf/2504.04144v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Simulations of coronal mass ejections on a young solar-type star and their detectability through coronal spectral observations
**Yu Xu,Hui Tian,Julian D. Alvarado-Gomez,Jeremy J. Drake,Gustavo Guerrero**


#mhd
### Abstract:
There is a growing interest in searching for coronal mass ejections (CMEs) in other stellar systems because they are thought to be one of the important factors shaping planetary atmospheres. We investigated the possible spectral signatures related to stellar CMEs using magnetohydrodynamic simulations and spectral synthesis techniques. Blue wing enhancements of the synthetic coronal line profiles caused by the line-of-sight motion of plasma were observed during the simulated CME events. We included instrumental conditions in the spectral synthesis and tested the detectability of the asymmetries under different instrumental broadening conditions. The results show that blue wing asymmetries are visible in some EUV lines with spectral resolutions higher than around 2000, and the line-of-sight velocities of CMEs obtained from asymmetry analysis techniques are comparable to the CME velocities derived from three-dimensional model outputs. However, when the spectral resolution drops below 2000, the asymmetries in the blue wings become barely visible, but blue shifts in the line centroids with velocities around -100 to -200 km/s are observed. We suggest a method of using MHD simulation to synthesize line profiles and analyze their asymmetries which may help to guide future instrument design in terms of detecting stellar CMEs through Doppler shifts or asymmetries of coronal spectral lines.


![[mdfiles/2504.04144.md|2504.04144]]
### AI Justification:
The paper explores magnetohydrodynamic simulations in the context of coronal mass ejections (CMEs) from young solar-type stars, which aligns with your interest in "the magnetic dynamics of plasmas." Although the primary focus is on stellar environments rather than the interstellar medium, the methodologies mentioned, such as spectral synthesis and MHD simulations, could provide insights into "magnetic field amplification" and "force interactions shaping magnetic dynamics," relevant to your focus on the behavior of magnetic fields in plasma environments.
# (239/382) http://arxiv.org/pdf/2504.03273v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The EMPI Code for Plasma-Induced Effects on Radio Waves I... Non-Magnetized Media and Applications to Fast Radio Bursts
**Nan Xu,He Gao,Yuan-Pei Yang,Bing Zhang,Wei-Yang Wang,Tian-Cong Wang,...**


#mhd
### Abstract:
Electromagnetic waves undergo modifications as they propagate through plasma. We present EMPI (ElectroMagnetic-wave Plasma Interaction), a three-dimensional numerical framework designed to simulate the interaction between radio signals and cold plasma. With input plasma density profiles, intrinsic radio signals, and the time and frequency resolutions of the telescope, the code synthesizes observed signals using first-principles calculations. EMPI is capable of modeling a wide range of plasma distributions, spanning analytically described smooth functions (e.g., Gaussian or exponential profiles), statistical models (e.g., turbulent screens), and discrete macroscopic structures like isolated plasma clumps, which are difficult to model both analytically and statistically. Validation tests demonstrate excellent agreement with established plasma propagation effects, such as dispersion, lensing, scintillation, and scattering. This code provides an efficient method for handling both analytical and statistical scenarios, bridging the gap between these descriptions. Thanks to its comprehensive capabilities, EMPI is particularly useful for studying radio sources with cosmological origin, especially pulse-like signals such as Fast Radio Bursts (FRBs). As these signals travel through diverse and complex plasma environments across the universe, their properties are inevitably altered, resulting in observable changes. In this context, EMPI serves as a valuable tool for studying the propagation effects of these sources, helping to advance the understanding of their essence and the intervening plasma environments.


![[mdfiles/2504.03273.md|2504.03273]]
### AI Justification:
The paper discusses the effects of plasma on electromagnetic waves, which relates to your interest in the dynamics of plasmas in the interstellar medium, specifically regarding how magnetic fields and other forces interact within these environments. Although the primary focus is on radio wave propagation and not directly on magnetic field amplification or dynamics, the EMPI code's capability to model complex plasma structures could provide insights into the broader context of magnetic structuring within turbulent plasma, which is relevant to your research on scale-dependent magnetic dynamics.
# (240/382) http://arxiv.org/pdf/2504.03224v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Effect of Spin Polarization on Lattice Vibrations and Electron Wave Interactions in Piezoelectric Semiconductor Quantum Plasma
**Abhishek Yadav,Punit Kumar**


#mhd
### Abstract:
The effect of spin polarization, induced by the difference in concentration of spin-up and spin-down electrons produced under the influence of a magnetic field, on lattice ion vibrationselectron wave interactions, and the resulting amplification of acoustic waves in spin polarised piezoelectric semiconductor quantum plasma has been studied. The dielectric permittivity of the high-density plasma medium has been evaluated through which the dispersion relation has been set up. The gain coefficient of acoustic waves has been obtained using the modified separate spin evolution quantum hydrodynamic (SSE-QHD) model for piezoelectric semiconductor plasma. The study reveals that quantum effects, including Fermi pressure and quantum Bohm potential, reduce wave frequency while spin polarization increases it. Acoustic gain rises significantly with frequency in the presence of quantum effects. Spin polarization also contributes to a slight increase in acoustic wave amplification.


![[mdfiles/2504.03224.md|2504.03224]]
### AI Justification:
This paper is somewhat relevant to your research interests as it touches on the influence of magnetic fields on a plasma medium, particularly through the lens of spin polarization and its effects on wave interactions, which aligns with your focus on magnetic field dynamics. However, it mainly discusses acoustic waves in semiconductor plasmas rather than the broader astrophysical context of magnetic field amplification, force interactions, or emergent dynamics in the interstellar medium.
# (241/382) http://arxiv.org/pdf/2504.03927v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Dimensionless learning based on information
**Yuan Yuan,Adrian Lozano-Duran**


#mhd
### Abstract:
Dimensional analysis is one of the most fundamental tools for understanding physical systems. However, the construction of dimensionless variables, as guided by the Buckingham- $\pi$ theorem, is not uniquely determined. Here, we introduce IT- $\pi$ , a model-free method that combines dimensionless learning with the principles of information theory. Grounded in the irreducible error theorem, IT- $\pi$ identifies dimensionless variables with the highest predictive power by measuring their shared information content. The approach is able to rank variables by predictability, identify distinct physical regimes, uncover self-similar variables, determine the characteristic scales of the problem, and extract its dimensionless parameters. IT- $\pi$ also provides a bound of the minimum predictive error achievable across all possible models, from simple linear regression to advanced deep learning techniques, naturally enabling a definition of model efficiency. We benchmark IT- $\pi$ across different cases and demonstrate that it offers superior performance and capabilities compared to existing tools. The method is also applied to conduct dimensionless learning for supersonic turbulence, aerodynamic drag on both smooth and irregular surfaces, magnetohydrodynamic power generation, and laser-metal interaction.


![[mdfiles/2504.03927.md|2504.03927]]
### AI Justification:
This paper explores "dimensionless learning" and its application to "magnetohydrodynamic power generation," which may provide insights into the dynamical behavior of magnetic fields relevant to my focus on "magnetic field amplification" and emergent dynamics in "turbulent plasmas." Although it leans towards methodology and predictive modeling rather than direct astrophysical magnetic dynamics, the principles of dimensionless analysis could still inform the understanding of force interactions shaping magnetic fields in various plasma environments.
# (242/382) http://arxiv.org/pdf/2504.02943v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Comparative Statistics of Solar Flares and Flare Stars
**J. I. Katz,M. Bharmal,M. Ju,N. Whitsett**


#mhd
### Abstract:
The distribution of interval times between recurrent discrete events, such as Solar and stellar flares, reflects their underlying dynamics. Log-normal functions provide good fits to the interval time distributions of many recurrent astronomical events. The width of the fit is a dimensionless parameter that characterizes its underlying dynamics, in analogy to the critical exponents of renormalization group theory. If the distribution of event strengths is a power law, as it often is over a wide range, then the width of the log-normal is independent of the detector sensitivity in that range, making it a robust metric. Analyzing two catalogues of Solar flares over periods ranging from 46 days to 37 years, we find that the widths of log-normal fits to the intervals between flares are wider than those of shot noise, indicating memory in the underlying dynamics even over a time much shorter than the Solar cycle. In contrast, the statistics of flare stars are consistent with shot noise (no memory). We suggest that this is a consequence of the production of Solar flares in localized transient active regions with varying mean flare rate, but that the very energetic flares of flare stars result from global magnetic rearrangement that reinitializes their magnetohydrodynamic turbulence.


![[mdfiles/2504.02943.md|2504.02943]]
### AI Justification:
This paper presents an analysis of the "underlying dynamics" of magnetic fields related to solar flares, which may provide insights into the "interactions between magnetic, gravitational, and thermal forces" as highlighted in your research focus. The concepts of "localized transient active regions" and "global magnetic rearrangement" could contribute to your understanding of "magnetic dynamics in plasmas," although the study centers on solar phenomena rather than interstellar mediums specifically.
# (243/382) http://arxiv.org/pdf/2504.00475v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Simulations of edge and SOL turbulence in diverted negative and positive triangularity plasmas
**P. Ulbl,A. Stegmeir,D. Told,G. Merlo,K. Zhang,F. Jenko**


#mhd
### Abstract:
Optimizing the performance of magnetic confinement fusion devices is critical to achieving an attractive fusion reactor design. Negative triangularity (NT) scenarios have been shown to achieve excellent levels of energy confinement, while avoiding edge localized modes (ELMs). Modeling turbulent transport in the edge and SOL is key in understanding the impact of NT on turbulence and extrapolating the results to future devices and regimes. Previous gyrokinetic turbulence studies have reported beneficial effects of NT across a broad range of parameters. However, most simulations have focused on the inner plasma region, neglecting the impact of NT on the outermost edge. In this work, we investigate the effect of NT in edge and scrape-off layer (SOL) simulations, including the magnetic X-point and separatrix. For the first time, we employ a multi-fidelity approach, combining global, non-linear gyrokinetic simulations with drift-reduced fluid simulations, to gain a deeper understanding of the underlying physics at play. First-principles simulations using the GENE-X code demonstrate that in comparable NT and PT geometries, similar profiles are achieved, while the turbulent heat flux is reduced by more than 50% in NT. Comparisons with results from the drift-reduced fluid turbulence code GRILLIX suggest that the turbulence is driven by trapped electron modes (TEMs). The parallel heat flux width on the divertor targets is reduced in NT, primarily due to a lower spreading factor $S$ .


![[mdfiles/2504.00475.md|2504.00475]]
### AI Justification:
The paper explores "turbulent transport" and the "impact of NT on turbulence," which aligns with my interest in "how magnetic fields interact with turbulence" and give rise to complex behaviors in plasma environments. Furthermore, it utilizes a "multi-fidelity approach" combining gyrokinetic and fluid simulations, which could offer insights relevant to "theoretical models" I seek related to the dynamics of magnetic fields in plasmas across different scales.
# (244/382) http://arxiv.org/pdf/2503.23319v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Class I/II Jets with JWST... Mass loss rates, Asymmetries, and Binary induced Wigglings
**Naman S. Bajaj,Ilaria Pascucci,Tracy L. Beck,Suzan Edwards,Sylvie Cabrit,Joan R. Najita,...**


#mhd
### Abstract:
We present JWST NIRSpec spectro-imaging observations of jets from four edge-on protoplanetary disks that exhibit clear signatures of MHD disk winds. Bipolar jets are detected and spatially resolved in over 30 shock-excited forbidden lines, multiple Paschen and Brackett series lines of atomic hydrogen, and the high-energy excitation line of atomic helium (1.083 um). This helium line is the brightest jet-tracer towards HH 30 and FS TauB, which also exhibit asymmetric intensity between their red- and blue-shifted lobes in all tracers, including the [Fe II] and [He I] lines. Extinction maps reveal no significant differences across the lobes, suggesting an asymmetric jet-launching mechanism rather than environmental effects. Diagnostic line ratios yield consistent shock speeds of 50-60 km/s, jet ionization fractions of 0.1-0.2, and pre-shock electron densities of 1000 /cm^3. Combined with pixel-by-pixel electron density maps and [Fe II] line luminosities, we estimate jet mass-loss rates using three independent methods, averaging around a few 10^(-9) solar masses/yr. We estimate the accretion rates for these sources as 10 times the jet mass loss rates and find them to match well with the independently derived accretion estimates of other Class II sources in the Taurus star-forming region. Owing to JWSTs high precision, we also investigate jet wiggling and find Tau 042021 to showcase the perfect case of mirror-symmetric wiggling, which can only be explained by the motion of the jet source around a stellar companion. Modeling this wiggling suggests Tau 042021 to host 0.33 and 0.07 solar masses binary at the center with binary separation of 1.35 au and an orbital period of 2.5 years.


![[mdfiles/2503.23319.md|2503.23319]]
### AI Justification:
While the paper focuses on the magnetic dynamics of jets from protoplanetary disks using JWST observations, it partially aligns with your interest in “Force Interactions Shaping Magnetic Dynamics,” particularly through the study of "MHD disk winds" and their associated magnetic field behaviors. However, the emphasis on binary-induced wiggling and jet characteristics may offer limited insight into the broader multi-scale dynamics of magnetic fields across the interstellar medium, which is a core aspect of your research focus.
# (245/382) http://arxiv.org/pdf/2503.22041v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Improved Tomographic Reconstruction of 3D Global Coronal Density from STEREO/COR1 Observations
**Tongjiang Wang,C. Nick Arge,Shaela I. Jones**


#mhd
### Abstract:
Tomography is a powerful technique for recovering the three-dimensional (3D) density structure of the global solar corona. In this work, we present an improved tomography method by introducing radial weighting in the regularization term. Radial weighting provides balanced smoothing of density values across different heights, helping to recover finer structures at lower heights while also stabilizing the solution and preventing oscillatory artifacts at higher altitudes. We apply this technique to reconstruct the 3D electron density of Carrington Rotation (CR) 2098 using two weeks of polarized brightness (pB) observations from the inner coronagraph (COR1) onboard spacecraft-B of the twin Solar Terrestrial Relations Observatory (STEREO), where the radial weighting function is taken as the inverse intensity background, calculated by averaging all the pB images used. Comparisons between density distributions at various heights from the tomography and magnetohydrodynamics (MHD) simulations show good agreement. We find that radial weighting not only effectively corrects the over-smoothing effect near the inner boundary in reconstructions using second-order smoothing but also significantly improves reconstruction quality when using zeroth-order smoothing. Additionally, comparing reconstructions for CR 2091 from single-satellite data with that from multi-viewpoint data suggests that coronal evolution and dynamics may have a significant impact on the reconstructed density structures. This improved tomography method has been used to create a database of 3D densities for CRs 2052 to 2154, based on STEREO/COR1-B data, covering the period from 08 January 2007 to 17 September 2014.


![[mdfiles/2503.22041.md|2503.22041]]
### AI Justification:
The paper presents an improved tomography method for reconstructing the 3D density structure of the solar corona, which aligns with my interests in the "emergent magnetic dynamics in turbulent plasmas" since density and magnetic field interactions are crucial in plasma environments. However, the focus on solar corona and the specific methodology of tomography do not directly address the "magnetic field amplification" or the "force interactions shaping magnetic dynamics" in broader astrophysical plasmas, limiting its overall relevance.
# (246/382) http://arxiv.org/pdf/2503.18884v2


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Further evidence of saturated, boosted, and disrupted magnetic braking from evolutionary tracks of cataclysmic variables
**Joaquin A. Barraza-Jorquera,Matthias R. Schreiber,Diogo Belloni**


#mhd
### Abstract:
Angular momentum loss through magnetic braking drives the spin-down of low-mass stars and the orbital evolution of various close binary systems. Current theories for magnetic braking, often calibrated for specific types of systems, predict angular momentum loss rates that differ by several orders of magnitude. A unified prescription would provide valuable constraints on the relationship between angular momentum loss, stellar dynamos, and magnetic activity. Recent studies have shown that a saturated, boosted, and disrupted (SBD) magnetic braking prescription can explain the observed increase in the fraction of close white dwarf plus M-dwarf binaries at the fully convective boundary, the period distribution of main-sequence binaries, and the mass distribution of close M-dwarf companions to hot subdwarfs. To analyze whether this prescription also applies to related binaries, we investigated the evolution of cataclysmic variables (CVs) using the SBD magnetic braking model. We implemented the SBD prescription into the stellar evolution code MESA and simulated CV evolution, testing different values for the boosting and disruption parameters over a range of stellar properties. Our model reproduces the observed mass transfer rates and donor mass-radius relation with good accuracy. The evolutionary tracks match the observed boundaries of the orbital period gap and the period minimum for values of boosting and disruption slightly smaller but still consistent with those derived from detached binaries. Angular momentum loss through SBD magnetic braking can explain not only detached binaries but also cataclysmic variables, making it the only current prescription suitable for multiple types of close binary stars. Further testing in other systems is needed, and the semi-empirical convective turnover times currently used for main-sequence stars should be replaced with self-consistent values.


![[mdfiles/2503.18884.md|2503.18884]]
### AI Justification:
The paper explores "angular momentum loss through magnetic braking," which aligns with my research interest in "magnetic field amplification" and how dynamo mechanisms influence magnetic dynamics within stellar environments. Additionally, its examination of different "stellar properties" and binary systems may offer insights into the "force interactions shaping magnetic dynamics" relevant to understanding the behavior and evolution of magnetic fields across scales.
# (247/382) http://arxiv.org/pdf/2503.19884v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetosphere Evolution and Precursor-Driven Electromagnetic Signals in Merging Binary Neutron Stars
**Dimitrios Skiathas,Constantinos Kalapotharakos,Zorawar Wadiasingh,Demosthenes Kazanas,Alice K. Harding,Paul T. Kolbeck**


#mhd
### Abstract:
We detail new force-free simulations to investigate magnetosphere evolution and precursor electromagnetic (EM) signals from binary neutron stars. Our simulations fully follow a representative inspiral motion, capturing the intricate magnetospheric dynamics and their impact on EM outflows. We explore a range of stellar magnetic moment orientations and relative strengths, finding that the magnetospheres and Poynting flux evolution are strongly configuration-dependent. The Poynting flux exhibits pulsations at twice the orbital frequency, $2\Omega$ , and is highly anisotropic, following a power-law dependence on orbital frequency. The index ranges from 1 to 6, shaped by the intricate dynamics of the magnetospheres. Furthermore, we present the first computation of... (1) The EM forces acting on the star surfaces, revealing the presence of torques that, for highly-magnetized stars, could influence the orbital dynamics or break the crust. (2) The high-energy emission signals from these systems by adopting the established isolated pulsar theory. Assuming curvature radiation in the radiation reaction limit, we find that photons could reach TeV--PeV energies in the last $\sim$ ~ms for magnetic field strengths $10^{10}-10^{15}$ ~G. However, our analysis of single photon magnetic pair production suggests that these photons are unlikely to escape, with the MeV band emerging as a promising observational window for precursor high-energy emission. In this framework, we construct high-energy emission skymaps and light curves, exploring observational implications. Finally, we propose potential precursor radio emission and delayed afterglow echoes from magnetized outflows, which may contribute to late-time re-brightening in short gamma-ray bursts or to orphan afterglows.


![[mdfiles/2503.19884.md|2503.19884]]
### AI Justification:
This paper has some relevance to your research interests as it discusses "magnetosphere evolution" and "magnetospheric dynamics," which relates to examining both "magnetic dynamics of plasmas" and "magnetic field amplification" in astrophysical environments. Additionally, the findings on "EM signals" and the interactions among stellar magnetic moments could contribute to the understanding of "force interactions shaping magnetic dynamics" in neutron star systems, although the primary focus is on a different astrophysical context than your primary interest in the interstellar medium.
# (248/382) http://arxiv.org/pdf/2503.17249v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On the origin of radio polarization in pulsar polar caps
**Jan Benacek,Axel Jessner,Martin Pohl,Tatiana Rievajova,Lucy S. Oswald**


#mhd
### Abstract:
A knowledge of polarization properties of coherent radio waves escaping pulsar polar caps is crucial for calculating radiative transfer through the magnetosphere and for obtaining specific predictions of observable radio properties. We describe the pair cascades in the pulsar polar cap, and for the first time, determine the Stokes parameters of the escaping radio waves from first-principle kinetic simulations for a pulsar with an inclination angle of the magnetic axis 60{\deg}. Our model provides a quantitative and qualitative explanation of the observed pulsar radio powers and spectra, the pulse profiles and polarization curves, their temporal variability, the strong Stokes L and weak Stokes V polarization components, as well as the fact that linear polarization decreases with frequency and the non-existence of a radius to frequency relationship. We find that the radio emission from the polar cap can produce a diverse range of observed pulsar properties, including single or double peaked profiles. Most of the Stokes V curves from our simulations appear to be antisymmetric, but symmetric curves are also present at some viewing angles. Although the PA swing of the radiation from the polar cap can be fitted by the rotating vector model (RVM) for most viewing angles, the angles obtained from the RVM do not correspond to the angular distance of the observer from the magnetic axis. Instead, the PA is directly related to the plasma flows in the polar cap and not to the dipole geometry of the magnetic field. The observed range of other polarization features, in addition to our results, can be explained by propagation effects which are not part of the simulation. Our simulations demonstrate that pair discharges determine the majority of its typically observed properties. The usage of RVM for estimations of the magnetic field geometry from observations needs to be reevaluated.


![[mdfiles/2503.17249.md|2503.17249]]
### AI Justification:
The paper's focus on "polarization properties of coherent radio waves" and its exploration of "pair cascades in the pulsar polar cap" relates to your interest in the "interaction of magnetic fields" within plasma environments, particularly in the context of astrophysical systems like pulsars. While it may not directly address magnetic field amplification mechanisms or scale-dependent structuring, it offers insight into magnetic dynamics and their observable effects, providing a complementary perspective to your theoretical models on magnetic behaviors.
# (249/382) http://arxiv.org/pdf/2504.03673v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Strong ionospheric activity at the MWA site associated with plasma bubble measured by GNSS
**Shintaro Yoshiura,Yuichi Otsuka,Cathryn M. Trott,Dev Null,Nozomu Nishitani,Keitaro Takahashi,...**


#mhd
### Abstract:
The Earths ionosphere refracts radio signals, shifting the apparent position of radio sources. Wide-field measurements with a radio interferometer can measure the ionospheric distortion. The Murchison Widefield Array (MWA) has the ability to capture ionospheric structures that are smaller than 100 km in extent. We report unusually strong ionospheric activity in MWA data during a magnetic storm on 2023 December 1. The duct-like structure (roughly 50 km $\times$ $>$ 100 km) passes through the MWA field-of-view (FOV) with a velocity of ~ 100 m/s. The offsets of the apparent position of the radio source are more than 1 degree in the MWA observation data at around 180 MHz. By comparing the Total Electron Content (TEC) data obtained from the GNSS receiver network, we have found that the TEC fluctuations represented by a high Rate of TEC change index (ROTI) coincided with the strong ionospheric activity observed by the MWA. This result suggests that unusual ionospheric signatures detected by the MWA could be caused by plasma bubbles extending across Western Australia during a magnetic storm.


![[mdfiles/2504.03673.md|2504.03673]]
### AI Justification:
This paper describes "strong ionospheric activity" and its relationship with "plasma bubbles," which aligns with my interest in the interactions between different plasma phenomena such as turbulence and magnetic fields. The results indicate the influence of magnetic storms on plasma behavior, which could provide insights into the "amplification and evolution of magnetic fields" in terrestrial plasma environments—this is relevant to my research focus on similar dynamics in astrophysical contexts.
# (250/382) http://arxiv.org/pdf/2503.14486v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Velocity Structure Correlations between the Nebular, Molecular, and Atmospheric Gases in the Cores of Four Cool Core Clusters
**Muzi Li,B. R. McNamara,Alison L. Coil,Marie-Joelle Gingras,Fabrizio Brighenti,H. R. Russell,...**


#mhd
### Abstract:
We investigate the velocity structure of nebular gas in the central galaxies of four clusters... Abell 1835, PKS 0745-191, Abell 262, and RXJ0820.9+0752, using data from the Keck Cosmic Web Imager (KCWI). Velocity structure functions (VSFs) of the [OII] emission line are compared to VSFs of molecular clouds observed with the Atacama Large Millimeter/submillimeter Array (ALMA). Apart from Abell 262 where the gas is located in a circumnuclear disk, the nebular gas in the remaining galaxies lies in off-nuclear filamentary structures with VSFs steeper than the Kolmogorov slope. This steepening may be plausibly attributed to gravity although other factors, such as magnetic stresses and bulk motion,} may be significant. The VSFs of CO and [OII] emission are similar in RXJ0820 and Abell 262, indicating close coupling of the nebular and molecular gases. In contrast, the nebular and molecular gases are differentiated on most scales in PKS 0745 and Abell 1835. This discrepancy is likely due to the radio-AGN churning the gas. We compare the scale-dependent velocity amplitudes of the hot atmospheres constrained by X-ray surface brightness fluctuation analysis using Chandra observations to the nebular VSFs. The large-scale consistency in Abell 1835 and RXJ0820 is consistent with condensation from the hot atmospheres. {We explore substantial systematic biases, including projection effects, windowing, and smoothing effects when comparing VSFs using different telescopes and instruments.


![[mdfiles/2503.14486.md|2503.14486]]
### AI Justification:
This paper has some relevance to your interests as it investigates the interactions between nebular and molecular gases in the context of galaxy clusters, which may imply underlying magnetic dynamics owing to the identification of "magnetic stresses" influencing the velocity structures. However, the focus on velocity structure functions and gravitational effects does not directly align with your primary interests in magnetic field amplification and emergent dynamics of magnetic fields in plasmas.
# (251/382) http://arxiv.org/pdf/2503.13118v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Gravitational Wave Effects on Radio Spectral Lines of Atomic Hydrogen... Hyperfine Splitting and Broadening Mechanisms
**Nontapat Wanwieng,Nithiwadee Thaicharoen,Narupon Chattrapiban,Apimook Watcharangkool**


#mhd
### Abstract:
We explore the effects of gravitational waves (GWs) on hydrogens radio spectral lines, focusing on the ground-state hyperfine transition and radiative transitions in highly excited Rydberg states. To analyze GW impacts on hyperfine structure, we derive Maxwells equations in a gravitational-wave background using linearized gravity and the $3+1$ formalism. Our findings reveal that GWs induce energy shifts in hyperfine magnetic substates, modifying the 21 cm line. However, these energy shifts fall well below the detection limits of current radio astronomical instruments. For transitions in highly excited states, which produce radio recombination lines (RRL), the influence of GW manifests itself as spectral broadening, with the fractional linewidth for $\mathrm{H}n\alpha$ scaling as $\Delta\nu/\nu_0 \sim n^7\omega^2_{\mathrm{gw}}h(t)$ . This suggests that RRLs could serve as probes for ultra-high-frequency GWs, particularly given that Rydberg atoms in the interstellar medium can reach quantum numbers above $n=100$ . As an example of possibly detectable high frequency GW source, We investigate GWs emitted during the inspiral of planetary-mass primordial black hole binaries, where GW-induced broadening in RRLs could exceed natural broadening effects. Additionally, we examine the influence of the recently detected stochastic gravitational-wave background on hydrogen spectral lines.


![[mdfiles/2503.13118.md|2503.13118]]
### AI Justification:
This paper is somewhat relevant to your interests in theoretical astrophysics and plasma physics as it explores the effects of gravitational waves on atomic hydrogen's radio spectral lines, which could intersect with the themes of magnetic dynamics in plasma environments. However, it primarily focuses on gravitational wave interactions and their implications on spectral lines, deviating from your primary interest in magnetic field amplification and interactions, making it of partial relevance rather than a direct match.
# (252/382) http://arxiv.org/pdf/2503.12498v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Diagnosing the solar atmosphere through the Mg I b $_2$ 5173 Å line. I. Nonlocal thermodynamic equilibrium inversions versus traditional inferences
**A. L. Siu-Tapia,L. R. Bellot Rubio,D. Orozco Suarez**


#mhd
### Abstract:
Aims. We examined the capabilities of methods based on the weak-field approximation and line bisectors to extract fast and reliable information about the height stratification of the magnetic field and line-of-sight velocities, respectively, from high spatial resolution observations of the Mg I b $_2$ line at 5173 \r{A}. Methods. The Mg I b $_2$ line was analyzed alongside the Fe I 6173 \r{A} line to help constrain the physical conditions of the photosphere. Additionally, we present the first high-resolution inversions of the Mg I b $_2$ line under nonlocal thermodynamic equilibrium (NLTE) conditions conducted over a large field of view using a full-Stokes multiline approach. To determine the optimal inversion strategy, we performed several tests on the Mg I b $_2$ line using the Fourier Transform Spectrometer atlas profile before applying it to our observations. Results. The good correlations between the traditional methods and the NLTE inversions indicate that the weak-field approximation is generally a reliable diagnostic tool at moderate field strengths for the rapid inference of the longitudinal magnetic field from the Mg I b $_2$ line. In contrast, line bisectors exhibit poorer correlations with the NLTE inferred plasma velocities, suggesting that they might not be suitable for deriving velocity gradients from the Mg I b $_2$ line. Furthermore, to accurately derive the thermodynamic properties of the solar atmosphere from this line, the more complex, and time-consuming, NLTE Stokes inversions are necessary. This work also provides observational evidence of the existence of low-lying canopies expanding above bright magnetic structures and pores near the low chromosphere.


![[mdfiles/2503.12498.md|2503.12498]]
### AI Justification:
This paper examines methods for diagnosing magnetic fields in the solar atmosphere, focusing on line profiles and their implications for the height stratification of magnetic fields, which connects to your interest in "Magnetic Dynamics" and "Scale-Dependent Magnetic Structuring." Although it primarily focuses on solar magnetism rather than interstellar mediums, the techniques and outcomes discussed may provide insights into the broader understanding of magnetic field behaviors across various plasma environments.
# (253/382) http://arxiv.org/pdf/2503.11799v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Effect of oblique horizontal magnetic field on convection rolls
**Snehashish Sarkar,Sutapa Mandal,Pinaki Pal**


#mhd
### Abstract:
We investigate the effect of external horizontal magnetic field applied on the convection rolls obliquely (at an angle $\phi$ with the $x$ -axis) in electrically conducting low Prandtl number fluids under the paradigm of the Rayleigh-B\{e}nard convection by performing three-dimensional direct numerical simulations. The control parameters, namely, the Chandrasekhar number ( $\mathrm{Q}$ ) and the reduced Rayleigh number $r$ (ratio of Rayleigh number to critical Rayleigh number), are varied in the ranges $0 \leq \mathrm{Q} \leq 1000 $ and $ 1 \leq r \leq 20 $ for the Prandtl numbers $ \mathrm{Pr} = 0.1$ and $0.2$ by considering three horizontal aspect ratios ( $\Gamma$ )... $\frac{1}{2}$ , $1$ and $2$ . In the absence of the magnetic field, the convection starts in the form of steady rolls including the one parallel to the $x$ -axis. As the oblique horizontal magnetic field is switched on at an angle $\phi \in (0^\circ, ~90^\circ] $ with the $ x$ -axis, it is observed that the Lorentz force generated by the component of the magnetic field transverse to the axis of the convection rolls inhibits convection in the form of steady rolls. Thus, with the application of the magnetic field, the convection is suppressed and restarts for a higher Rayleigh number in the form of steady convection rolls. The rolls can either be oriented along the $x$ -axis (steady parallel rolls, SPR) or oriented at an angle $45^\circ$ (steady oblique rolls, SOR $^+$ ) with the $x$ -axis depending on the choices of the parameters. A rich bifurcation structure with standing and traveling patterns emerges at higher $r$ . The oscillatory instability of steady rolls scales as \( \mathrm{Q}^\alpha \) with distinct exponents for weak and strong magnetic fields. Additionally, heat transfer decreases with increasing \( \phi \) for given \( \mathrm{Q} \) and \( \mathrm{Pr} \).


![[mdfiles/2503.11799.md|2503.11799]]
### AI Justification:
The paper offers insights into magnetic field interactions within convection processes, particularly with a magnetic field applied at an angle, which aligns with my interest in "Force Interactions Shaping Magnetic Dynamics" as it explores the effects of the Lorentz force on convection in plasmas. Furthermore, the investigation into how magnetic fields influence the behavior and structure of convection rolls ties into my focus on the "Scale-Dependent Magnetic Structuring," particularly in the context of astrophysical plasmas and their multi-scale dynamics.
# (254/382) http://arxiv.org/pdf/2503.10067v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Enhanced MVA of Polarized Proton Beams via PW Laser-Driven Plasma Bubble
**Zhikun Zou,Gan Guo,Meng Wen,Bin Liu,Xue Yan,Yangjie Liu,...**


#mhd
### Abstract:
The significance of laser-driven polarized beam acceleration has been increasingly recognized in recent years. We propose an efficient method for generating polarized proton beams from a pre-polarized hydrogen halide gas jet, utilizing magnetic vortex acceleration enhanced by a laser-driven plasma bubble. When a petawatt laser pulse passes through a pre-polarized gas jet, a bubble-like ultra-nonlinear plasma wave is formed. As part of the wave particles, background protons are swept by the acceleration field of the bubble and oscillate significantly along the laser propagation axis. Some of the pre-accelerated protons in the plasma wave are trapped by the acceleration field at the rear side of the target. This acceleration field is intensified by the transverse expansion of the laser-driven magnetic vortex, resulting in energetic polarized proton beams. The spin of energetic protons is determined by their precession within the electromagnetic field, as described by the Thomas-Bargmann-Michel-Telegdi equation in analytical models and particle-in-cell simulations. Multidimensional simulations reveal that monoenergetic proton beams with hundreds of MeV in energy, a beam charge of hundreds of pC, and a beam polarization of tens of percent can be produced at laser powers of several petawatts. Laser-driven polarized proton beams offer promising potential for application in polarized beam colliders, where they can be utilized to investigate particle interactions and to explore the properties of matter under unique conditions.


![[mdfiles/2503.10067.md|2503.10067]]
### AI Justification:
The paper's focus on "magnetic vortex acceleration" and its implications for "polarized proton beams" suggests an intersection with my interest in "magnetic dynamics of plasmas in the interstellar medium." Furthermore, the use of "multidimensional simulations" to explore the behavior of protons within a "laser-driven plasma bubble" aligns with my emphasis on theoretical models and simulations in studying the evolution and amplification of magnetic fields in plasma environments.
# (255/382) http://arxiv.org/pdf/2503.09667v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Unveiling the Dynamics and Genesis of Small-scale Fine Structure Loops in the Lower Solar Atmosphere
**Annu Bura,Tanmoy Samanta,Alphonse Sterling,Yajie Chen,Jayant Joshi,Vasyl Yurchyshyn,...**


#mhd
### Abstract:
Recent high-resolution solar observations have unveiled the presence of small-scale loop-like structures in the lower solar atmosphere, often referred to as unresolved fine structures, low-lying loops, and miniature hot loops. These structures undergo rapid changes within minutes, and their formation mechanism has remained elusive. In this study, we conducted a comprehensive analysis of two small loops utilizing data from the Interface Region Imaging Spectrograph (IRIS), the Goode Solar Telescope (GST) at Big Bear Solar Observatory, and the Atmospheric Imaging Assembly (AIA) and the Helioseismic Magnetic Imager (HMI) onboard the Solar Dynamics Observatory (SDO), aiming to elucidate the underlying process behind their formation. The GST observations revealed that these loops, with lengths of $\sim$ 3.5 Mm and heights of $\sim$ 1 Mm, manifest as bright emission structures in H $\alpha$ wing images, particularly prominent in the red wing. IRIS observations showcased these loops in 1330 angstrom slit-jaw images, with TR and chromospheric line spectra exhibiting significant enhancement and broadening above the loops, indicative of plasmoid-mediated reconnection during their formation. Additionally, we observed upward-erupting jets above these loops across various passbands. Furthermore, differential emission measurement analysis reveals an enhanced emission measure at the location of these loops, suggesting the presence of plasma exceeding 1 MK. Based on our observations, we propose that these loops and associated jets align with the minifilament eruption model. Our findings suggest a unified mechanism governing the formation of small-scale loops and jets akin to larger-scale X-ray jets.


![[mdfiles/2503.09667.md|2503.09667]]
### AI Justification:
This paper does connect to my research interests in theoretical astrophysics and plasma physics by examining the formation mechanisms of small-scale loop-like structures and their magnetic dynamics in the lower solar atmosphere, which could provide insights into "the role of magnetic fields in organizing and shaping structures." The mention of “plasmoid-mediated reconnection” and the analysis of rapid changes in these structures aligns with my focus on how "magnetic fields behave, interact, and amplify" within plasma environments, although it primarily pertains to solar plasmas rather than the interstellar medium.
# (256/382) http://arxiv.org/pdf/2503.08983v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Large-scale multifractality and lack of self-similar decay for Burgers and 3D Navier-Stokes turbulence
**Takeshi Matsumoto,Dipankar Roy,Konstantin Khanin,Rahul Pandit,Uriel Frisch**


#mhd
### Abstract:
We study decaying turbulence in the 1D Burgers equation (Burgulence) and 3D Navier-Stokes (NS) turbulence. We first investigate the decay in time $t$ of the energy $E(t)$ in Burgulence, for a fractional Brownian initial potential, with Hurst exponent $H$ , and demonstrate rigorously a self-similar time-decay of $E(t)$ , previously determined heuristically. This is a consequence of the nontrivial boundedness of the energy for any positive time. We define a spatially forgetful \textit{oblivious fractional Brownian motion} (OFBM), with Hurst exponent $H$ , and prove that Burgulence, with an OFBM as initial potential $\varphi_0(x)$ , is not only intermittent, but it also displays, a hitherto unanticipated, large-scale bifractality or multifractality; the latter occurs if we combine OFBMs, with different values of $H$ . This is the first rigorous proof of genuine multifractality for turbulence in a nonlinear hydrodynamical partial differential equation. We then present direct numerical simulations (DNSs) of freely decaying turbulence, capturing some aspects of this multifractality. For Burgulence, we investigate such decay for two cases... (A) $\varphi_0(x)$ a multifractal random walk that crosses over to a fractional Brownian motion beyond a crossover scale $\mathcal{L}$ , tuned to go from small- to large-scale multifractality; (B) initial energy spectra $E_0(k)$ , with wavenumber $k$ , having one or more power-law regions, which lead, respectively, to self-similar and non-self-similar energy decay. Our analogous DNSs of the 3D NS equations also uncover self-similar and non-self-similar energy decay. Challenges confronting the detection of genuine large-scale multifractality, in numerical and experimental studies of NS and MHD turbulence, are highlighted.


![[mdfiles/2503.08983.md|2503.08983]]
### AI Justification:
The paper delves into "turbulence" and "multifractality" which are directly relevant to your interest in "emergent magnetic dynamics in turbulent plasmas," as it discusses how complex behaviors in fluid dynamics can provide insights into similar behaviors in astrophysical plasmas. Additionally, the mention of "nonlinear hydrodynamical partial differential equations" suggests a rigorous theoretical approach that aligns with your focus on simulations and models within plasma environments, particularly regarding how energy dynamics may reflect broader magnetic interactions.
# (257/382) http://arxiv.org/pdf/2503.07947v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Oscillations of the black hole photon ring as a probe of ultralight dilaton fields
**Chunlong Li,Chao Chen,Xiao Yan Chew**


#mhd
### Abstract:
Recent advancements of very long baseline interferometry (VLBI) have facilitated unprecedented probing of superradiant phenomena in the vicinities of supermassive black holes (SMBHs), establishing an ideal laboratory to detect ultralight bosons beyond the Standard Model. In this study, we delve into how ultralight dilaton clouds, formed via SMBH superradiance, impact the black hole photon rings. Our focus is on the dilaton-electromagnetic coupling term of the form $f(\phi)F_{\mu\nu}F^{\mu\nu}$ . By integrating geometric optics with plasma refractive effects in accretion environments, we demonstrate that the dilaton cloud dynamically alters the plasma frequency. Through systematic ray-tracing simulations covering a range of plasma densities and dilaton coupling strengths, we reveal a periodic distortion in the photon ring morphology, with the periodicity aligning with that of the dilaton-driven plasma frequency oscillations. We then assess the magnitude of this effect under the current angular resolution constraints of VLBI observations. Our analysis indicates that a comprehensive search for superradiant dilaton clouds based on the dilaton-electromagnetic coupling would necessitate radio interferometric baselines significantly exceeding the Earths diameter to resolve the corresponding signatures.


![[mdfiles/2503.07947.md|2503.07947]]
### AI Justification:
This paper discusses the interaction of ultralight dilaton fields with electromagnetic fields in the vicinity of supermassive black holes, touching upon the interplay of magnetic dynamics in a plasma environment, which aligns with my interest in "Force Interactions Shaping Magnetic Dynamics." Although it primarily focuses on dilaton fields, the integration of plasma refractive effects and the implications for magnetic behavior near black holes provides relevant insight into the more complex multi-scale dynamics of magnetic fields in astrophysical plasmas.
# (258/382) http://arxiv.org/pdf/2503.08878v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Atomic and Molecular Nitrogen Ions at the Dayside Magnetopause During the 2024 Mothers Day Storm
**R. G. Gomez,S. A. Fuselier,S. K. Vines,J. Goldstein,J. L. Burch,R. J. Strangeway**


#mhd
### Abstract:
Ion measurements made with the Hot Plasma Composition Analyzers of the Magnetospheric Multiscale Mission (MMS-HPCAs) during the Mothers Day Storm (Gannon Storm) of 10-13 May 2024 yield the first observations of atomic and molecular nitrogen ions in the Earths dayside outer magnetosphere. A population of ions identified as doubly charged nitrogen and oxygen was also measured. These observations were made within a highly compressed magnetosphere at a geocentric distance of ~6 Earth Radii during the early recovery phase of the storm. From the ion composition measurements and accompanying magnetic field data, we determine the reconnection rate at the magnetopause; we compare this result to a model reconnection rate that assumes the presence of only atomic oxygen and hydrogen. The heavy ion-laden-mass density in the magnetosphere was greater than the shocked solar wind mass density in the magnetosheath. Despite these conditions, magnetic reconnection still occurred at the magnetopause.


![[mdfiles/2503.08878.md|2503.08878]]
### AI Justification:
The paper examines **magnetic reconnection** events within the magnetosphere, highlighting ion compositions and magnetic field interactions, which are relevant to my research focus on **force interactions shaping magnetic dynamics**. However, it primarily deals with the Earth’s magnetosphere during a specific storm rather than the **broader interstellar plasma dynamics** I am interested in, leading to a partial alignment with my interests.
# (259/382) http://arxiv.org/pdf/2503.08940v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Coherent Structures and Lattice-Boltzmann Hydrodynamics in Turbulent Pipe Flows
**B. Magacho**


#mhd
### Abstract:
Coherent structures (CS) are known to be part of the foundations of turbulent flow dynamics. For a long time, their appearance was believed to be chaotic and unorganized. However, it has been demonstrated through numerical simulations and experiments that a high degree of organization of CS could be attributed to the constitution of a turbulent state. Understanding these organizational dynamics promises to bring valuable theoretical and applied predictions, such as the average lifetime of turbulent structures and understanding the role of CS in particulate transport. The identification of CS was achieved by selecting the most energetic mode in the flow direction within a specified reference shell. Furthermore, the transition dynamics between the identified CS was investigated as a stochastic process, revealing a non-Markovian effect through an algebraic decay of the temporal self-correlation of the identified CS. Finally, the non-Markovian behavior observed between the transitions of CS was reproduced by a low-level Markovian model, which takes into account the degeneracy effects in the definition of the identified CS. In order to obtain an algorithm capable of simulating the quasi-static regime in magnetohydrodynamic (MHD) flows a multiple-relaxation-time (MRT) model and a distance-dependent boundary condition were introduced for the lattice Boltzmann method (LBM) associated with the induction equation for MHD flows. Finally, a turbulent pipe flow simulation was performed by the LBM with a MRT model for hydrodynamic distributions. The identification of CS revealed a non-trivial memory effect with respect to the force that triggered the turbulent state. The transition dynamics of CS revealed a Markovian behavior for finely resolved time data, indicating that experimental behavior could be recovered for larger time separations and, consequently, a larger dataset.


![[mdfiles/2503.08940.md|2503.08940]]
### AI Justification:
The paper examines "coherent structures" within turbulent flows and offers insights into the organizational dynamics of turbulence, which can relate to my interests in "emergent magnetic dynamics in turbulent plasmas" and how these effects might interplay with magnetic fields in astrophysical contexts. Additionally, the use of a magnetohydrodynamic (MHD) framework in the simulations hints at methodologies that could help illuminate "magnetic dynamics" in plasma environments, albeit with a focus that might diverge from my specific astrophysical applications.
# (260/382) http://arxiv.org/pdf/2503.01745v2


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Gone with the wind... the outward migration of eccentric giant planets in windy disks
**Gaylor Wafflard-Fernandez,Geoffroy Lesur**


#mhd
### Abstract:
Recent studies indicate that circumstellar disks exhibit weak turbulence, with their dynamics and evolution being primarily influenced by magnetic winds. However, most numerical studies have focused on planet-disk interactions in turbulent disk models. We aim to explore how wind-driven accretion affects the orbital and eccentricity evolution of a Jovian planet within a magnetized disk. Conversely, we seek to determine in what extent such a planet can modify the accretion behavior and the wind dynamics. We perform high-resolution 3D global non-ideal magneto-hydrodynamic (MHD) simulations of a massive gap-carving planet interacting with a wind-launching disk, using the accelerated code IDEFIX. We consider the influence of the gap shape on planet migration by restarting a `fixed-planet` simulation at three different times, from which the planet evolves freely in the disk. For a strong initial magnetization and a sufficiently deep planet gap, we find that the planet becomes moderately eccentric, and its migration is slow, unsteady and mostly outward. This migration pattern is due to the gaps radial asymmetry which enhances the inner Lindblad torque while reducing the outer Lindblad torque. We show that eccentricity can grow up to 6-8% and is likely driven by a finite-amplitude instability triggered by first-order external Lindblad resonances. These moderate eccentricity values periodically modulate the gap accretion rate and wind mass loss rate, possibly leading to the formation of discrete structures in CO outflows. Slow outward migration and eccentricity growth appear to be common outcomes of planet-disk-wind interactions, which may contribute significantly to both the long orbital periods and the moderate eccentricities of warm jupiters. Additionally, eccentric massive protoplanets embedded in circumstellar disks could play a role in generating structured outflows.


![[mdfiles/2503.01745.md|2503.01745]]
### AI Justification:
The paper explores magnetic dynamics within circumstellar disks, emphasizing "magnetic winds" and their impact on planet migration, which indirectly relates to "magnetic field amplification" and "force interactions" outlined in your research focus. Although primarily centered on planet-disk interactions, the study's use of "non-ideal magneto-hydrodynamic (MHD)" simulations touches upon multi-scale dynamics and potentially relevant emergent behaviors, making it a thought-provoking read within the context of magnetic behavior in plasma environments.
# (261/382) http://arxiv.org/pdf/2503.03959v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Improving the Temporal Resolution of SOHO/MDI Magnetograms of Solar Active Regions Using a Deep Generative Model
**Jialiang Li,Vasyl Yurchyshyn,Jason T. L. Wang,Haimin Wang,Yasser Abduallah,Khalid A. Alobaid,...**


#mhd
### Abstract:
We present a novel deep generative model, named GenMDI, to improve the temporal resolution of line-of-sight (LOS) magnetograms of solar active regions (ARs) collected by the Michelson Doppler Imager (MDI) on board the Solar and Heliospheric Observatory (SOHO). Unlike previous studies that focus primarily on spatial super-resolution of MDI magnetograms, our approach can perform temporal super-resolution, which generates and inserts synthetic data between observed MDI magnetograms, thus providing finer temporal structure and enhanced details in the LOS data. The GenMDI model employs a conditional diffusion process, which synthesizes images by considering both preceding and subsequent magnetograms, ensuring that the generated images are not only of high-quality, but also temporally coherent with the surrounding data. Experimental results show that the GenMDI model performs better than the traditional linear interpolation method, especially in ARs with dynamic evolution in magnetic fields.


![[mdfiles/2503.03959.md|2503.03959]]
### AI Justification:
This paper presents a deep generative model designed to improve the temporal resolution of solar magnetograms, which indirectly relates to your interest in "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas." While the focus is on solar active regions, the techniques and findings regarding magnetic field dynamics could offer insights applicable to your research on the behavior and interaction of magnetic fields across varying astrophysical environments.
# (262/382) http://arxiv.org/pdf/2503.02601v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Episodic outbursts during brown dwarf formation
**Adam Parkosidis,Dimitris Stamatellos,Basmah Riaz**


#mhd
### Abstract:
There is evidence that stars and browns dwarfs grow through episodic rather than continuous gas accretion. However, the role of episodic accretion in the formation of brown dwarfs remains mostly unexplored. We investigate the role of episodic accretion, triggered by the magnetorotational instability in the inner disk regions, resulting in episodic outbursts during the formation of brown dwarfs, and its implications for their early formation stages. We use hydrodynamical simulations coupled with a sub-grid accretion model to investigate the formation of young proto-brown dwarfs and protostars, taking into account the effects of episodic accretion resulting in episodic radiative feedback, i.e. in luminosity outbursts. The formation timescale for proto brown dwarfs is at least one order of magnitude shorter than that of protostars. Episodic accretion leads to a shorter main accretion phase compared to continuous accretion in brown dwarfs, whereas the opposite is true for low-mass stars. Episodic accretion can accelerate early mass accretion in proto-brown dwarfs and protostars, but it results in less massive objects by the end of the main phase compared to continuous accretion. We find an approximately linear correlation between an objects mass at the end of the main accretion phase and the timing of the last episodic outburst... later events result in more massive brown dwarfs but less massive low-mass stars. Episodic outbursts have a stronger effect on brown dwarf-forming cloud cores, with the last outburst essentially splitting the brown dwarf evolution into a short high-accretion and a much longer low-accretion phase.


![[mdfiles/2503.02601.md|2503.02601]]
### AI Justification:
This paper discusses the role of magnetic dynamics in the formation of brown dwarfs, specifically through the magnetorotational instability, which aligns with my interest in “magnetic dynamics of plasmas” as it emphasizes the interaction between magnetic fields and accretion processes. Additionally, the use of “hydrodynamical simulations” suggests relevant methodologies might be shared in exploring the complexities of magnetic field behaviors in plasma environments, which is central to my research focus.
# (263/382) http://arxiv.org/pdf/2503.01983v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The temperature and metallicity distributions of the ICM... insights with TNG-Cluster for XRISM-like observations
**Dimitris Chatzigiannakis,Annalisa Pillepich,Aurora Simionescu,Nhut Truong,Dylan Nelson**


#mhd
### Abstract:
The new era of high-resolution X-ray spectroscopy will significantly improve our understanding of the intra-cluster medium (ICM) by providing precise constraints on its underlying physical properties. However, spectral fitting requires reasonable assumptions on the thermal and chemical distributions of the gas. We use the output of TNG-Cluster, the newest addition to the IllustrisTNG suite of cosmological magnetohydrodynamical simulations, to provide theoretical expectations for the multi-phase nature of the ICM across hundreds of z=0 clusters (M $_{500c}$ = 10 $^{14.0-15.3}$ M $_\odot$ ) based upon a realistic model for galaxy formation and evolution. We create and analyse, in an observer-like manner, end-to-end XRISM/Resolve mock observations towards cluster centres. We then systematically compare the intrinsic properties of the simulated gas with the inferred ones from spectral fitting via a variety of commonly used spectral-emission models. Our analysis suggests that models with a distribution of temperatures, such as bvlognorm and bvgadem, better describe the complex thermal structure of the ICM, as predicted by TNG-Cluster, but incur biases of 0.5-2 keV (16th-84th percentiles). The 1T bvapec is too simplistic for the predicted broad temperature distributions, while a 2T double bvapec model systematically fails to capture the input temperature structure. However, all spectral emission models systematically underestimate the Fe abundance of the central ICM by ~0.1 Solar (~ 20 per cent) primarily due to projection effects. Selecting only strong cool core clusters leads to minor improvements on inference quality, removing the majority of outliers but maintaining similar overall biases and cluster-to-cluster scatter.


![[mdfiles/2503.01983.md|2503.01983]]
### AI Justification:
This paper has some relevance to your work as it employs "magnetohydrodynamical simulations" which align with your interests in studying "the complex, multi-scale dynamics of magnetic fields in plasma environments." While it primarily focuses on the thermal and chemical distributions in the intra-cluster medium, the underlying magnetic dynamics could inform your research on "how magnetic fields behave and interact" across different scales within astrophysical plasmas.
# (264/382) http://arxiv.org/pdf/2502.09545v2


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Cascaded Gamma-ray Emission Associated with the KM3NeT Ultra-High-Energy Event KM3-230213A
**Ke Fang,Francis Halzen,Dan Hooper**


#mhd
### Abstract:
A neutrino-like event with an energy of $\sim 220 \,{\rm PeV}$ was recently detected by the KM3NeT/ARCA telescope. If this neutrino comes from an astrophysical source, or from the interaction of an ultra-high-energy cosmic ray in the intergalactic medium, the ultra-high-energy gamma rays that are co-produced with the neutrinos will scatter with the extragalactic background light, producing an electromagnetic cascade and resulting in emission at GeV-to-TeV energies. In this paper, we compute the gamma-ray flux from this neutrino source considering various source distances and strengths of the intergalactic magnetic field (IGMF). We find that the associated gamma-ray emission could be observed by existing imaging air cherenkov telescopes and air shower gamma-ray observatories, unless the strength of the IGMF is $B\gtrsim 3\times 10^{-13}$ G, or the ultra-high-energy gamma-rays are attenuated inside of the source itself. In the latter case, this source is expected to be radio-loud.


![[mdfiles/2502.09545.md|2502.09545]]
### AI Justification:
The paper examines the role of intergalactic magnetic fields (IGMF) in relation to ultra-high-energy gamma-ray and neutrino emission, which aligns somewhat with my interest in "magnetic field amplification" and "force interactions shaping magnetic dynamics." While it does not directly address the broader aspects of "emergent magnetic dynamics in turbulent plasmas," the consideration of how IGMF affects gamma-ray flux could provide insights on magnetic field behavior in large-scale plasma environments.
# (265/382) http://arxiv.org/pdf/2503.00683v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Linking Critical Heights in Solar Active Regions with 3D CME Speeds... Insights from Automated and Manual PIL Detection Methods
**Harshita Gandhi,Alexander James,Huw Morgan,Lucie Green**


#mhd
### Abstract:
In a space weather context, the most geoeffective coronal mass ejections (CMEs) are fast CMEs from Earth-facing solar active regions. These CMEs are difficult to characterize in coronagraph data due to their high speed (fewer observations), faintness, Earthward orientation (halo CMEs), and disruptions from associated high-energy particle storms. Any diagnostic aiding in early CME speed identification is valuable. This study investigates whether the 3D speeds of 37 CMEs are correlated with the critical heights of their source regions, to test the hypothesis that if the critical height is located at a higher altitude in the corona, the weaker magnetic field environment will enable a faster CME to be produced. Critical heights near CME onset are calculated by identifying polarity inversion lines (PIL) in magnetogram data using automated and manual methods. 3D speeds are determined by fitting a Graduated Cylindrical Shell (GCS) model to multi-viewpoint coronagraph images. For the automated method, we find a high correlation of 71% +- 8% between CME speed and critical height, dropping to 48% +- 12% when using CME plane-of-sky speeds, on which most previous similar studies are based. An attempt to improve the critical height diagnostic through manual PIL selection yields a lower correlation of 58% +/- 13%. The higher correlation from the automated method suggests that encompassing the full PIL structure is a better measure of the magnetic conditions that influence CME dynamics. Our results highlight the potential for critical height as a continuously computable diagnostic for forecasting the 3D speeds of Earth-directed CMEs.


![[mdfiles/2503.00683.md|2503.00683]]
### AI Justification:
This paper presents insights into the behavior of magnetic fields in solar active regions and how they influence the speeds of coronal mass ejections (CMEs), pertinent to your interest in "magnetic dynamics of plasmas" and "force interactions shaping magnetic dynamics." While it primarily focuses on CMEs rather than the interstellar medium directly, the relationship between magnetic fields and plasma dynamics discussed in the context of solar phenomena could yield valuable insights applicable to your research on magnetic field amplification and organizational structures in various plasma environments.
# (266/382) http://arxiv.org/pdf/2503.00373v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Their currents turn awry, and lose the name of action. I... Fundamental limits to orbit reconstruction due to non-conservation of stellar actions
**Arunima Arunima,Mark Krumholz,Michael Ireland,Chuhan Zhang,Zipeng Hu**


#mhd
### Abstract:
The conservation of stellar actions is a fundamental assumption in orbit reconstruction studies in the Milky Way. However, the disc is highly dynamic, with time-dependent, non-axisymmetric features like transient spiral arms and giant molecular clouds (GMCs) driving local fluctuations in the gravitational potential on top of the near-axisymmetric background. Using high-resolution magnetohydrodynamic simulations that incorporate gas dynamics and star formation, we quantify the rate at which these effects drive non-conservation of the actions of young stars from Myr to Gyr timescales. We find that action evolution is well described as a logarithmic random walk, with vertical action evolving more rapidly than radial action; the diffusion rate associated with this random walk is weakly dependent on the stellar birth environment and scales approximately linearly with the galactic orbital frequency at a stars position. The diffusion rates we measure imply a fundamental limit of $\sim 100$ Myr as the timescale over which stellar orbits can be reliably reconstructed using methods that assume action conservation. By comparing diffusion rates for younger stars to those measured for an older and more vertically-extended control population, we conclude that radial action evolution is driven primarily by transient spiral arms, while vertical action evolution is driven by gravitational scattering off gaseous structures. Our results have significant implications for galactic archaeology and disc dynamics studies, necessitating a closer look at the timescales over which actions are assumed to be conserved in the disc.


![[mdfiles/2503.00373.md|2503.00373]]
### AI Justification:
The paper’s focus on "high-resolution magnetohydrodynamic simulations" aligns with your interest in theoretical models and simulations of magnetic dynamics in plasma environments. While the primary emphasis is on stellar actions and their evolution due to dynamic features like "transient spiral arms" and "gaseous structures," the findings regarding the interactions of magnetic and gravitational forces could provide valuable insights into the broader implications for magnetic field behavior in the interstellar medium.
# (267/382) http://arxiv.org/pdf/2503.00543v1


### Rating: 5.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 55.00000000000001%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Disk draining in LIGO progenitor black hole binaries and its significance to electromagnetic counterparts
**Xiaoshan Huang,Sierra Dodd,Sophie Lund Schroder,Shane W. Davis,Enrico Ramirez-Ruiz**


#mhd
### Abstract:
The effect of tidal forces on transport within a relic accretion disk in binary black holes is studied here with a suite of two-dimensional hydrodynamic simulations. As the binary contracts due to the emission of gravitational waves, the accretion disk is truncated, and a two-armed spiral wave is excited, which remains stationary in the rotating reference frame of the coalescing binary. Such spiral waves lead to increased transport of mass and angular momentum. Our findings suggest that even in the case of weakly ionized accretion disks, spiral density waves will drain the disk long before the orbit of the two black holes decays enough for them to merge, thus dimming prospects for a detectable electromagnetic counterpart.


![[mdfiles/2503.00543.md|2503.00543]]
### AI Justification:
This paper is somewhat relevant to your interests, particularly due to its examination of "two-dimensional hydrodynamic simulations" related to the behavior of accretion disks in black hole binaries, which could offer insights into dynamical processes in plasmas. However, it lacks a direct focus on "magnetic field amplification" and "magnetic dynamics," which are central to your research on the interactions and complexities of magnetic fields in astrophysical environments.
# (268/382) http://arxiv.org/pdf/2502.02811v3


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Cherenkov emission by a fast-moving uncharged Schwarzschild black hole
**Sergei Khlebnikov,Maxim Lyutikov**


#mhd
### Abstract:
We demonstrate that in the presence of an external magnetic field, an uncharged classical Schwarzschild black hole moving superluminally in a dielectric with permittivity $\epsilon > 1$ produces Cherenkov emission. This is a new physical effect... classical (non-quantum) emission of electromagnetic waves by a completely charge-neutral ``particle. The governing equations (involving General Relativity, electromagnetism, and the physics of continuous media) have no external electromagnetic source - it is the distortion of the initial electromagnetic fields by the gravity of the black hole that plays the role of a superluminally moving source. The effect relies on nonzero values of both the magnetic field and the gravitational radius, as well as on the usual Cherenkov condition on the velocity, $v/c > 1/\sqrt{\epsilon}$ . Unlike Cherenkov emission by a point charge, the effective source in this case is spatially distributed, with emission generated along the single Cherenkov emission cone. The emitted spectrum is red-dominated, with power $\propto dk_z /|k_z| $ for wave numbers $ |k_z| \leq 1/R_G $ , where $ R_G$ is the Schwarzschild radius. We comment on possible observability of this process during black hole -- neutron star mergers.


![[mdfiles/2502.02811.md|2502.02811]]
### AI Justification:
The paper discusses the interaction of magnetic fields with the dynamics of a superluminal black hole, which touches on themes of magnetic field behavior and gravitation in astrophysical contexts, albeit indirectly. While it doesn't directly address magnetic field amplification or turbulence within plasma, the exploration of Cherenkov emission under the influence of magnetic fields might provide insights into emergent magnetic dynamics within complex systems, aligning somewhat with my interest in the behavior of magnetic fields in the interstellar medium.
# (269/382) http://arxiv.org/pdf/2504.21408v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The maximum mass and rotational kinetic energy of rapidly rotating neutron stars
**Shao-Peng Tang,Yong-Jia Huang,Yi-Zhong Fan**


#mhd
### Abstract:
Rapid uniformly-rotating neutron stars are expected to be formed for instance in the collapse of some massive stars, the accretion of some compact object binaries, and some double neutron star mergers. The huge amount of the rotational energy has been widely believed to be the source of some cosmic gamma-ray bursts and superluminous supernovae. Benefited from the tight constraints on the equation of state of the neutron star matter set by the latest multi-messenger data, the chiral effective field theory ( $\chi$ EFT) and perturbative quantum chromodynamics (pQCD), here we present the maximum gravitational mass as well as the kinetic rotational energy for a neutron star at a given spin period. Our nonparametric EOS analysis reveals that the critical Keplerian configurations ( $\Omega_{\rm kep}^{\rm crit}=1.00\pm0.07\times 10^{4}~ {\rm rad/s}$ ) can sustain maximum gravitational masses of $M_{\rm kep}^{\rm crit}=2.76^{+0.11}_{-0.09} M_\odot$ with corresponding rotational energy reaching $E_{\rm rot,kep}^{\rm crit}=2.38^{+0.25}_{-0.24}\times 10^{53}$ . However, the maximum rotational energy that can be feasibly extracted from a neutron star is limited to $1.40^{+0.15}_{-0.13}\times 10^{53}$ erg, which holds for a baryon mass of $2.68^{+0.10}_{-0.09}M_\odot$ . All these parameters, obtained via the nonparametric reconstruction of the equation of state, are at the $68.3\%$ confidence level and the adoption of a quarkonic model yields rather similar results. These findings are found to have already set some intriguing constraints on the millisecond magnetar interpretation of some exciting data.


![[mdfiles/2504.21408.md|2504.21408]]
### AI Justification:
This paper discusses the rotational dynamics of neutron stars and their implications for cosmic phenomena, which somewhat intersects with my interest in the magnetic dynamics of plasmas, particularly in the context of neutron stars potentially acting as magnetic field amplifiers through their energetic processes. However, the focus is primarily on gravitational mass and rotational energy rather than the mechanisms of magnetic field behavior, making it less relevant for my specific research interests in the multi-scale dynamics and amplification processes of magnetic fields in the interstellar medium.
# (270/382) http://arxiv.org/pdf/2504.19534v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quantifying Uncertainties in Solar Wind Forecasting Due to Incomplete Solar Magnetic Field Information
**Stephan G. Heinemann,Jens Pomoell,Ronald M. Caplan,Mathew J. Owens,Shaela Jones,Lisa Upton,...**


#mhd
### Abstract:
Solar wind forecasting plays a crucial role in space weather prediction, yet significant uncertainties persist due to incomplete magnetic field observations of the Sun. Isolating the solar wind forecasting errors due to these effects is difficult. This study investigates the uncertainties in solar wind models arising from these limitations. We simulate magnetic field maps with known uncertainties, including far-side and polar field variations, as well as resolution and sensitivity limitations. These maps serve as input for three solar wind models... the Wang-Sheeley-Arge (WSA), the Heliospheric Upwind eXtrapolation (HUXt), and the European Heliospheric FORecasting Information Asset (EUHFORIA). We analyze the discrepancies in solar wind forecasts, particularly the solar wind speed at Earths location, by comparing the results of these models to a created `ground truth` magnetic field map, which is derived from a synthetic solar rotation evolution using the Advective Flux Transport (AFT) model. The results reveal significant variations within each model with a RMSE ranging from 59-121 km/s. Further comparison with the thermodynamic Magnetohydrodynamic Algorithm outside a Sphere (MAS) model indicates that uncertainties in the magnetic field data can lead to even larger variations in solar wind forecasts compared to those within a single model. However, predicting a range of solar wind velocities based on a cloud of points around Earth can help mitigate uncertainties by up to 20-77%.


![[mdfiles/2504.19534.md|2504.19534]]
### AI Justification:
This paper examines the uncertainties in solar wind forecasting due to incomplete magnetic field information, which relates directly to my interest in "magnetic field amplification" and "force interactions" within astrophysical plasmas. While the focus is on solar magnetic fields, the study's insights into how variations in magnetic field data influence plasma behavior may provide valuable context for understanding similar phenomena in the interstellar medium.
# (271/382) http://arxiv.org/pdf/2504.20015v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Interaction of Laguerre-Gaussian laser pulses with borane targets of different hydrogen-boron ratio
**Lars Reichwein,Alexander Pukhov,Markus Buscher**


#mhd
### Abstract:
We study the interaction of high-intensity Laguerre Gaussian laser pulses with hydrogen-boron compounds targets using 3D particle-in-cell simulations. The ratio of hydrogen to boron is varied throughout different simulation runs as a proxy model for various borane molecules that can be synthesized. We show that the strength of the axial magnetic fields generated via the Inverse Faraday effect depends on the specific ratio of target components, making boranes and the option to tune their composition of interest for proton-boron fusion.


![[mdfiles/2504.20015.md|2504.20015]]
### AI Justification:
This paper carries relevance to my research interests primarily through its exploration of "axial magnetic fields generated" in a plasma environment, which aligns with my focus on "magnetic field amplification" and the behavior of magnetic fields. Furthermore, the use of "3D particle-in-cell simulations" offers a methodological framework that could potentially inform my work on how magnetic fields interact with other forces in various plasma scales.
# (272/382) http://arxiv.org/pdf/2503.07880v3


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Structure and Dynamics of the Suns Interior Revealed by Helioseismic and Magnetic Imager
**Alexander Kosovichev,Sarbani Basu,Yuto Bekki,Juan Camilo Buitrago-Casas,Theodosios Chatzistergos,Ruizhu Chen,...**


#mhd
### Abstract:
High-resolution helioseismology observations with the Helioseismic and Magnetic Imager (HMI) onboard Solar Dynamics Observatory (SDO) provide a unique three-dimensional view of the solar interior structure and dynamics, revealing a tremendous complexity of the physical processes inside the Sun. We present an overview of the results of the HMI helioseismology program and discuss their implications for modern theoretical models and simulations of the solar interior.


![[mdfiles/2503.07880.md|2503.07880]]
### AI Justification:
While the paper focuses on the solar interior and helioseismology, it may partially align with your interest in magnetic fields due to discussions on "implications for modern theoretical models and simulations." However, the primary focus on the Sun's interior structure is less directly related to your specific interests in "magnetic dynamics of plasmas in the interstellar medium" and interactions within plasma environments.
# (273/382) http://arxiv.org/pdf/2504.18014v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Kinematic Signature of the Warp and Waves in the Milky Way Disk
**Weixiang Sun,Han Shen,Biwei Jiang,Xiaowei Liu**


#mhd
### Abstract:
Using over 170,000 red clump stars selected from LAMOST and APOGEE, we conduct a detailed analysis of the stellar $V_{Z}$ as a function of $L_{Z}$ (or $R_{g}$ ) across different $\phi$ bins for various disk populations. The $V_{Z}$ of the whole RC sample stars exhibits a wave-like pattern superimposed on an exponentially increasing trend, indicating the contribution from disk warp, disk flare and disk waves. Our results across various populations suggest that the thin disk is similar to the whole RC sample behavior, while the thick disk displays a wave-like pattern superimposed on a linearly increasing trend, meaning that the features of disk warp and waves are present in both thin and thick disks, and the disk flare feature is only present in the thin disk. These results indicate that the disk warp is potentially driven by secular processes like disk perturbations from intergalactic magnetic fields and a misaligned dark halo. The line-of-node (LON) of the disk warp of various populations displays a slight difference, with $\phi_{0}$ = 5.68 $\pm$ 2.91 degree for the whole RC sample stars, $\phi_{0}$ = 5.78 $\pm$ 2.89 degree for the thin disk stars, and $\phi_{0}$ = 4.10 $\pm$ 3.43 degree for the thick disk stars.


![[mdfiles/2504.18014.md|2504.18014]]
### AI Justification:
This paper is somewhat relevant to my research interests as it explores the influence of "intergalactic magnetic fields" in the context of disk dynamics, which touches upon magnetic interactions that may parallel my focus on "magnetic dynamics of plasmas in the interstellar medium." However, while the findings relate to structural behaviors in stellar populations, they do not explicitly delve into the "amplification" or "complex dynamics" of magnetic fields within plasma environments, limiting its direct applicability to my specific research focus.
# (274/382) http://arxiv.org/pdf/2504.17482v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A New Age-Activity Relation For Solar Analogs that Accounts for Metallicity
**Gabriela Carvalho-Silva,Jorge Melendez,Anne Rathsam,J. Shejeelammal,Giulia Martos,Diego Lorenzo-Oliveira,...**


#mhd
### Abstract:
Determining stellar ages is challenging, particularly for cooler main-sequence stars. Magnetic evolution offers an observational alternative for age estimation via the age-chromospheric activity (AC) relation. We evaluate the impact of metallicity on this relation using near one-solar-mass stars across a wide metallicity range. We analyze a sample of 358 solar-type stars with precise spectroscopic parameters determined through a line-by-line differential technique and with ages derived using Yonsei-Yale isochrones. We measured chromospheric activity (S-index) using high-quality HARPS spectra, calibrated to the Mount Wilson system, and converted to the $R^{\prime}_{\mathrm HK}(T_{\mathrm{eff}})$ index with a temperature-based photospheric correction. Our findings show that the AC relation for $R^{\prime}_{\mathrm HK}(T_{\mathrm{eff}})$ is strongly influenced by metallicity. We propose a new age-activity-metallicity relation for solar-type main-sequence (MS) stars ( $\log{g} \gtrsim 4.2 $ ) with temperatures 5370 $\lesssim$ $T_{\mathrm{eff}}$ $\lesssim$ 6530 K and metallicities from -0.7 to +0.3 dex. We show that taking metallicity into account significantly enhances chromospheric ages reliability, reducing the residuals root mean square (RMS) relative to isochronal ages from 2.6 Gyr to 0.92 Gyr. This reflects a considerable improvement in the errors of chromospheric ages, from 53\% to 15\%. The precision level achieved in this work is also consistent with previous age-activity calibration from our group using solar twins.


![[mdfiles/2504.17482.md|2504.17482]]
### AI Justification:
This paper presents a new age-activity relation for solar analogs that factors in metallicity, which is somewhat aligned with your interest in “the role of magnetic fields” as it relates to magnetic dynamics in stellar environments. However, the focus on stellar activities and chromospheric analysis does not directly encompass the complex, multi-scale dynamics of magnetic fields in plasma environments within the interstellar medium, making it less relevant to your primary research focus.
# (275/382) http://arxiv.org/pdf/2504.14543v2


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On the development of OpenFOAM solvers for simulating MHD micropolar fluid flows with or without the effect of micromagnetorotation
**Kyriaki-Evangelia Aslani,Ioannis E. Sarris,Efstratios Tzirtzilakis**


#mhd
### Abstract:
The paper introduces two new OpenFOAM solvers, epotMicropolarFoam and epotMMRFoam, developed for simulating magnetohydrodynamic (MHD) micropolar flows with magnetic particles, such as blood, without or with the effect of micromagnetorotation (MMR). MMR refers to the magnetic torque resulting from the misalignment between the magnetization of magnetic particles within the fluid and the magnetic field, influencing the internal rotation (microrotation) of these particles. Blood can be represented as a micropolar fluid containing magnetic particles, owing to the magnetization of erythrocytes. EpotMicropolarFoam utilizes a transient approach and the PISO algorithm for pressure-velocity coupling, adopting the low-magnetic-Reynolds-number approximation for the MHD phenomena. It also accounts for micropolar effects, incorporating the force term arising from the microrotation-vorticity difference in the momentum equation, and solves the internal angular momentum equation. EpotMMRFoam is a modification of epotMicropolarFoam to include the MMR term in the internal angular momentum equation, while a constitutive magnetization equation is also solved. Validation was conducted against analytical solutions of MHD micropolar Poiseuille blood flow, demonstrating excellent accuracy (error < 2%) for both solvers. When the MMR term is included, velocity and microrotation were significantly reduced (up to 40% and 99.9%, respectively), particularly under strong magnetic fields and high hematocrit values. In the absence of MMR, magnetic effects were minimal due to the bloods relatively low conductivity and small vessel size. MHD 3D artery blood flow simulations confirmed similar trends. The solvers exhibit strong potential for biomedical applications such as magnetic hyperthermia and targeted drug delivery.


![[mdfiles/2504.14543.md|2504.14543]]
### AI Justification:
The paper presents novel OpenFOAM solvers for simulating magnetohydrodynamic (MHD) micropolar flows, which aligns with my interest in exploring magnetic field dynamics within plasma environments, specifically through its focus on "magnetic torque" and the interaction of magnetic fields with fluids. However, the application to biomedical contexts, such as blood flow simulations, suggests that while the methods may provide useful insights, they may not fully address the complexities of "magnetic field amplification" and interactions in astrophysical plasmas I am exploring.
# (276/382) http://arxiv.org/pdf/2503.19507v2


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Velocity modulations in view of the elliptical approach at Wendelstein 7-X
**A. Kramer-Flecken,X. Han,G. Weir,T. Windisch,H. M. Xiang,T. Andreeva,...**


#mhd
### Abstract:
The estimation of the poloidal velocity of the turbulence and the poloidal mean flow velocity are important quantities for the study of sheared flows on turbulence and transport. The estimation depends on the underlying model of the turbulence. Beside the propagation time of the turbulence, its decay with the fading time must be considered. For the description of the propagation, the elliptical approach is applied, which takes into account the propagation and fading time of the turbulence. The model has been applied successfully in experimental fluid dynamics and is confirmed by direct numerical simulations, also. In this paper, the elliptical approach is applied in the analysis of density fluctuations, measured by poloidal correlation reflectometry at two different fusion devices, TEXTOR and W7-X. For the latter, it is demonstrated that the elliptical approach is necessary for a correct description of the turbulence propagation. In addition, the velocity modulations are investigated, which in principle can be either generated by an oscillation of the propagation time of density fluctuations and/or an oscillation of the fading of the turbulence. An example for low frequency velocity oscillations in W7-X will be given in the paper, showing a relation between turbulence properties and small oscillations on the measured diamagnetic plasma energy.


![[mdfiles/2503.19507.md|2503.19507]]
### AI Justification:
This paper discusses the estimation of poloidal velocity in turbulence, which relates indirectly to the interactions between magnetic and fluid dynamics; however, it does not specifically address the amplification or evolution of magnetic fields in astrophysical plasmas as outlined in your research focus. While the topic of turbulence is relevant, the primary focus on fusion devices and the elliptical approach limits its alignment with your interests in magnetic field dynamics across astrophysical scales.
# (277/382) http://arxiv.org/pdf/2504.15601v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### [PK2008] HalphaJ115927 and IGR J14091-6108... Two new intermediate polars above the period gap
**Arti Joshi**


#mhd
### Abstract:
This study presents a detailed timing analyses of two cataclysmic variables (CVs), [PK2008] HalphaJ115927 and IGR J14091-610, utilizing the optical data from the Transiting Exoplanet Survey Satellite (TESS). Periods of 7.20 $\pm$ 0.02 h, 1161.49 $\pm$ 0.14 s, and 1215.99 $\pm$ 0.15 s are presented for [PK2008] HalphaJ115927, and are interpreted as the probable orbital, spin, and beat periods of the system, respectively. The presence of multiple periodic variations suggests that it likely belongs to the intermediate polar (IP) category of magnetic CVs. Interestingly, [PK2008] HalphaJ115927 exhibits a unique and strong periodic modulation at 5.66 $\pm$ 0.29 d, which may result from the precession of an accretion disc, similar to the IP TV Col. The detection of a spin signal of 576.63 $\pm$ 0.03 s and inferred orbital signal of $\sim$ 15.84 h supports the classification of IGR J14091-610 as an IP. The identification of such a long orbital period adds a new example to the limited population of long-period IPs. The observed dominant signal at the second harmonic of the orbital frequency also suggests ellipsoidal modulation of the secondary in this system. The observed double-peaked spin pulse profile in [PK2008] HalphaJ115927 likely results from two-pole accretion, where both poles contribute to the spin modulation, and their geometry allows equal visibility of both accreting poles. In contrast, IGR J14091-610 exhibits a single-peaked sinusoidal like spin pulse, attributed to the changing visibility of the accretion curtains due to a relatively low dipole inclination. The present observations indicate that accretion in both systems occurs predominantly through a disc.


![[mdfiles/2504.15601.md|2504.15601]]
### AI Justification:
This paper presents a detailed analysis of magnetic dynamics in intermediate polar cataclysmic variables, which aligns with your interest in "magnetic dynamics of plasmas" and "how magnetic fields behave and interact." However, the focus on specific binaries and their timing analysis may limit its applicability to your broader research interests in the interstellar medium and multi-scale dynamics.
# (278/382) http://arxiv.org/pdf/2504.16190v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Simulating X-point radiator turbulence
**K. Eder,W. Zholobenko,A. Stegmeir,M. Bernert,D. Coster,F. Jenko**


#mhd
### Abstract:
Coupling a high-performance burning plasma core to a detached boundary solution is critical for realizing magnetic confinement fusion power. Predictive simulations of the edge and scrape-off layer are therefore essential and must self-consistently account for turbulence and the interplay between the plasma, neutral gas, and impurities. We present results on controlled full detachment in ASDEX Upgrade with an X-point radiator (XPR), obtained with the edge turbulence code GRILLIX. Two simulations with dense nitrogen radiation fronts, located 5 and 12 cm above the X-point (accounting for 80% of the input heating power), are discussed. In validations against density, temperature, and bolometry measurements, the simulations show good agreement and reproduce the detached divertor conditions observed in the experiment. Neutral gas is critical for achieving detachment and modulating the height of the XPR front, in agreement with previous SOLPS-ITER transport modeling and analytical power balance studies. In addition, the front structure is highly dynamic due to turbulence, consisting of ionizing and radiative mantles surrounding intermittent cold spots of recombining plasma. Near the detachment front, density and temperature fluctuation amplitudes exceed the background by more than 400%, compared to 40% in an attached reference case. In detached conditions, we observe an inward shift of the radial electric field well at the OMP, along with the breaking of poloidal symmetry in the electrostatic potential. The latter induces strong radial flows around the XPR, which may explain the ELM suppression observed in the H-mode XPR regime.


![[mdfiles/2504.16190.md|2504.16190]]
### AI Justification:
This paper focuses on turbulence and the interplay between plasma and neutral gas in magnetic confinement, which provides insights into force interactions that shape magnetic dynamics in plasma environments. Although its primary focus is on confinement fusion power rather than the interstellar medium, it addresses complex behaviors arising from turbulence that may have relevant implications for understanding emergent magnetic dynamics in astrophysical plasmas.
# (279/382) http://arxiv.org/pdf/2504.15382v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Glow of Axion Quark Nugget Dark Matter... (III) The Mysteries of the Milky Way UV Background
**Michael Sekatchev,Xunyu Liang,Fereshteh Majidi,Ben Scully,Ludovic Van Waerbeke,Ariel Zhitnitsky**


#mhd
### Abstract:
Axion quark nuggets (AQNs) are hypothetical objects with nuclear density that would have formed during the quark-hadron transition and could make up most of the dark matter today. These objects have a mass greater than a few grams and are sub-micrometer in size. They would also help explain the matter-antimatter asymmetry and the similarity between visible and dark components of the universe, i.e. $\Omega_{\text{DM}} \sim \Omega_{\text{visible}}$ . These composite objects behave as cold dark matter, interacting with ordinary matter and producing pervasive electromagnetic radiation. This work aims to calculate the FUV electromagnetic signature in a 1 kpc region surrounding the solar system, resulting from the interaction between antimatter AQNs and baryons. To this end, we use the high-resolution hydrodynamic simulation of the Milky Way, FIRE-2 Latter suite, to select solar system-like regions. From the simulated gas and dark matter distributions in these regions, we calculate the FUV background radiation generated by the AQN model. We find that the results are consistent with the FUV excess recently confirmed by the Alice spectrograph aboard New Horizons, which corroborated the FUV excess initially discovered by GALEX a decade ago. We also discuss the potential cosmological implications of our work, which suggest the existence of a new source of FUV radiation in galaxies, linked to the interaction between dark matter and baryons.


![[mdfiles/2504.15382.md|2504.15382]]
### AI Justification:
This paper discusses the interaction between antimatter axion quark nuggets and baryonic matter, which could relate to the study of magnetic fields in interstellar environments through their electromagnetic radiation implications, as noted in phrases like “electromagnetic radiation” and “interaction between dark matter and baryons.” However, it does not address the specific mechanisms of magnetic field amplification, force interactions, or emergent magnetic dynamics directly related to plasma physics that are central to your research interests in theoretical astrophysics.
# (280/382) http://arxiv.org/pdf/2504.15097v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Multiwavelength Observations of the Precursors Before the Eruptive X4.9 Limb Solar Flare on 25 February, 2014... Current Sheet, Eruptive Filament, Flare and Eruption Onset in the Frame of the Tether-Cutting Magnetic Reconnection Scenario
**Sharykin I. N.,Zimovets I. V.,Motorina G. G.,Meshalkina N. S**


#mhd
### Abstract:
We present multiwavelength analysis of the pre-flare phase and onset of the powerful X4.9 near-limb eruptive solar flare on February 25, 2014, revealing the tether-cutting (TC) geometry. We aim at determining relationship between the region of pre-flare energy release with the regions where the flare started to develop, and to investigate a detailed chronology of energy release during the pre-flare time interval and the beginning of the impulse phase. Using X-ray, ultraviolet and radio microwave data we found that the pre-flare energy release site was compact and localized in the vicinity of TC interaction of magnetic structures near the polarity inversion line. The analysis indicates that a pre-flare current sheet (CS) could be in this region. Good correspondence between the location of the pre-flare and flare emission sources visible at the very beginning of the impulsive phase is shown. We found relationship between dynamics of the energy release in the pre-flare CS and formation of the future flare eruptive structure. The growth of the magnetic flux rope was associated with activation of plasma emissions, flows and an increase of UV radiation fluxes from the region where the pre-flare CS was located. The eruptive flux rope gradually grew due to feeding by magnetized plasma ejected from the reconnecting pre-flare CS. Finally, it is shown that the most probable trigger of the eruption was a local fast microflare-like magnetic reconnection in the pre-flare CS. Some local instability in the pre-flare sheet could lead to a transition from the slow to fast reconnection regime. As a result, an ejection from the sheet was initiated and the eruptive flux rope lost its stability. Then, the eruptive flux rope itself initiated formation of the main reconnecting flare CS as in the Standard Flare Model during its movement, and intense emissions associated with the impulsive phase were observed.


![[mdfiles/2504.15097.md|2504.15097]]
### AI Justification:
The paper's exploration of "the tether-cutting (TC) geometry" and "magnetic structures near the polarity inversion line" aligns with your interest in "magnetic field amplification" and "force interactions shaping magnetic dynamics," particularly as it discusses the relationship between energy release in magnetic regions and the dynamics of flares. Additionally, the detailed analysis of "emissions associated with the impulsive phase" relates to your focus on multi-scale dynamics and the interaction of magnetic fields within plasma environments.
# (281/382) http://arxiv.org/pdf/2504.15403v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Non-Hermitian wave turbulence
**Xander M. de Wit,Sebastien Galtier,Michel Fruchart,Federico Toschi,Vincenzo Vitelli**


#mhd
### Abstract:
Wave turbulence describes the long-time statistical behavior of out-of-equilibrium systems composed of weakly interacting waves. Non-Hermitian media ranging from open quantum systems to active materials can sustain wave propagation in so-called $PT$ -symmetric states where gain and loss are effectively balanced. Here, we derive the kinetic equations governing wave turbulence in a prototypical non-Hermitian medium... a three-dimensional fluid with odd viscosity. We calculate its exact anisotropic solution, the so-called Kolmogorov-Zakharov spectrum, and validate the existence of this regime using direct numerical simulations. This non-Hermitian wave turbulence generates a direct cascade that is sustained down to the smallest scales, suppressing the transition to strong turbulence typically observed in rotating fluids and electron magnetohydrodynamics. Beyond odd viscous fluids, this qualitative mechanism applies to any non-linear system of waves where non-Hermitian effects are enhanced at small scales through gradient terms in the dynamical equations, e.g. via odd elastic moduli or other non-reciprocal responses.


![[mdfiles/2504.15403.md|2504.15403]]
### AI Justification:
The paper discusses wave turbulence in non-Hermitian media, which could provide unique insights into the "complex, emergent magnetic behaviors" that can arise in theoretical astrophysics and plasma physics, particularly under non-standard conditions. However, while it touches on wave dynamics and cascading phenomena, it lacks direct relevance to magnetic field amplification and force interactions within astrophysical plasmas, which are central to your research focus.
# (282/382) http://arxiv.org/pdf/2503.07953v3


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### MFC 5.0... An exascale many-physics flow solver
**Benjamin Wilfong,Henry A. Le Berre,Anand Radhakrishnan,Ansh Gupta,Diego Vaca-Revelo,Dimitrios Adam,...**


#mhd
### Abstract:
Many problems of interest in engineering, medicine, and the fundamental sciences rely on high-fidelity flow simulation, making performant computational fluid dynamics solvers a mainstay of the open-source software community. A previous work (Bryngelson et al., Comp. Phys. Comm. (2021)) published MFC 3.0 with numerous physical features, numerics, and scalability. MFC 5.0 is a marked update to MFC 3.0, including a broad set of well-established and novel physical models and numerical methods, and the introduction of XPU acceleration. We exhibit state-of-the-art performance and ideal scaling on the first two exascale supercomputers, OLCF Frontier and LLNL El Capitan. Combined with MFCs single-accelerator performance, MFC achieves exascale computation in practice. New physical features include the immersed boundary method, N-fluid phase change, Euler--Euler and Euler--Lagrange sub-grid bubble models, fluid-structure interaction, hypo- and hyper-elastic materials, chemically reacting flow, two-material surface tension, magnetohydrodynamics (MHD), and more. Numerical techniques now represent the current state-of-the-art, including general relaxation characteristic boundary conditions, WENO variants, Strang splitting for stiff sub-grid flow features, and low Mach number treatments. Weak scaling to tens of thousands of GPUs on OLCF Summit and Frontier and LLNL El Capitan sees efficiencies within 5% of ideal to their full system sizes. Strong scaling results for a 16-times increase in device count show parallel efficiencies over 90% on OLCF Frontier. MFCs software stack has improved, including continuous integration, ensuring code resilience and correctness through over 300 regression tests; metaprogramming, reducing code length and maintaining performance portability; and code generation for computing chemical reactions.


![[mdfiles/2503.07953.md|2503.07953]]
### AI Justification:
This paper presents MFC 5.0, which includes "magnetohydrodynamics (MHD)" as a significant component of its physical models, indicating potential relevance to my focus on magnetic dynamics within plasma environments. However, the primary emphasis of the abstract is on computational fluid dynamics and the software's engineering and performance characteristics, rather than directly addressing the magnetic field amplification or complex interactions of forces in astrophysical contexts.
# (283/382) http://arxiv.org/pdf/2504.10760v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Validation of FLASH for magnetically driven inertial confinement fusion target design
**C. Leland Ellison,Jonathan Carroll-Nellenback,Chiatai Chen,Scott Davidson,Bryan Ferguson,Fernando Garcia-Rubio,...**


#mhd
### Abstract:
FLASH is a widely available radiation magnetohydrodynamics code used for astrophysics, laboratory plasma science, high energy density physics, and inertial confinement fusion. Increasing interest in magnetically driven inertial confinement fusion (ICF), including Pacific Fusions development of a 60 MA Demonstration System designed to achieve facility gain, motivates the improvement and validation of FLASH for modeling magnetically driven ICF concepts, such as MagLIF, at ignition scale. Here we present a collection of six validation benchmarks from experiments at the Z Pulsed Power Facility and theoretical and simulation studies of scaling MagLIF to high currents. The benchmarks range in complexity from focused experiments of linear hydrodynamic instabilities to fully integrated MagLIF fusion experiments. With the latest addition of physics capabilities, FLASH now obtains good agreement with the experimental data, theoretical results, and leading ICF target design simulation code results across all six benchmarks. These results establish confidence in FLASH as a useful tool for designing magnetically driven ICF targets on facilities like Z and Pacific Fusions upcoming Demonstration System.


![[mdfiles/2504.10760.md|2504.10760]]
### AI Justification:
This paper mentions "radiation magnetohydrodynamics" and focuses on "magnetically driven inertial confinement fusion," which may be tangentially related to your interest in magnetic dynamics of plasmas, but does not directly address the “magnetic field amplification” or interactions of forces as you primarily seek. While it explores some relevant simulation techniques and provides insights into the behavior of magnetic fields in a specific context, it lacks a broader application to the interstellar medium or the emergent dynamics of magnetic fields that are central to your research focus.
# (284/382) http://arxiv.org/pdf/2504.09304v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Black holes with electroweak hair -- the detailed derivation
**Romain Gervalle,Mikhail S. Volkov**


#mhd
### Abstract:
We present a very detailed derivation of solutions describing hairy black holes within the gravity-coupled Weinberg-Salam theory, which were previously reported in \href{https...//doi.org/10.1103/PhysRevLett.133.171402}{Phys.Rev.Lett. 133 (2024) 171402}. These black holes support a strong magnetic field that polarizes the electroweak vacuum and creates a condensate of massive fields carrying superconducting currents along the black hole horizon. The currents, in turn, generate a ``corona of magnetic vortex segments attached to the horizon at both ends. The condensate and corona together constitute the black hole hair. The extremal solutions approach, in the far field, the magnetic Reissner-Nordstr\`om configuration, with a total mass that is {\it lower} than the total charge, $M<|Q|$ , due to the negative Zeeman energy of the condensate. This makes the removal of the hair energetically unfavorable. The maximally hairy black holes exhibit masses comparable to terrestrial values, with approximately 11\% of their total mass stored in the hair. Given that these solutions arise within a well-tested theoretical framework, they are likely to have physical relevance.


![[mdfiles/2504.09304.md|2504.09304]]
### AI Justification:
This paper is marginally relevant to your research interests as it discusses magnetic fields in the context of hairy black holes; however, the focus is primarily on black hole physics rather than the interstellar medium. While it addresses magnetic field dynamics and highlights interactions related to magnetic structures, it does not directly engage with plasma environments or the amplification and behavior of magnetic fields in astrophysical plasmas as outlined in your focus areas.
# (285/382) http://arxiv.org/pdf/2504.09091v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Nonlocal effects on Thermal Transport in MagLIF-Relevant Gaspipes on NIF
**R. Y. Lau,D. J. Strozzi,M. Sherlock,M. Weis,A. S. Joglekar,W. A. Farmer,...**


#mhd
### Abstract:
We present simulations of heat flow relevant to gaspipe experiments on the National Ignition Facility (NIF) to investigate kinetic effects on transport phenomena. D2 and neopentane (C5H12) filled targets are used to study the laser preheat stage of a MagLIF scheme where anaxial magnetic field is sometimes applied to the target. Simulations were done with the radiation-MHD code HYDRA with a collision-dominated fluid model and the Schurtz nonlocal electron thermal conduction model. Using the Schurtz model to evolve the electron temperature increased the heat front propagation of neopentane gas targets compared to a local model by limiting radial heat flow. This increases electron temperature near the axis, which decreases laser absorption. We find the effect of heat flow models on temperature profiles and laser propagation is modest. Beyond the Schurtz model, we utilize HYDRA to initialize plasma conditions for the Vlasov Fokker-Planck K2 code. We run K2 until a quasi-steady state is reached and examine the impact of kinetic effects on heat transport. Although axial heat flow is well predicted by fluid models, the fluid model consistently over predicts radial heat flow up to 150% in regions with the largest temperature gradient of D2 filled gaspipes. On the other hand, the Schurtz nonlocal electron conduction model is found to be adequate for capturing kinetic heat flow in gaspipes.


![[mdfiles/2504.09091.md|2504.09091]]
### AI Justification:
The paper discusses the effects of magnetic fields on thermal transport phenomena in MagLIF-related gaspipe experiments, which is somewhat relevant to your interest in "magnetic dynamics of plasmas." However, it primarily focuses on thermal transport rather than the amplification or emergent behaviors of magnetic fields, thereby offering limited direct insights into the complex magnetic interactions within astrophysical plasmas.
# (286/382) http://arxiv.org/pdf/2504.02791v2


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Variability study of classical supergiant X-ray binary 4U 1907+09 using NuSTAR
**Raj Kumar,Sayantan Bhattacharya,Sudip Bhattacharyya,Subir Bhattacharyya**


#mhd
### Abstract:
We investigate the X-ray variability of the supergiant X-ray binary 4U 1907+09 using the new NuSTAR observation of 2024. The source had a relatively stable flux level during previous NuSTAR observations, but the flux varied significantly during the current one. The light curve exhibits dips (off-state) and flares (on-state). The phase-coherent timing analysis during the on-state yields a pulse period of $443.99(4)~\mathrm{s}$ , showing the pulsars continued spin-down. The pulse profiles show an asymmetric double-peaked structure with a phase separation of 0.47 between the two peaks. A cyclotron resonance scattering feature (CRSF) is also detected at $\sim 17.6~\mathrm{keV}$ , along with its harmonic at $\sim 38~\mathrm{keV}$ , persisting across all flux states. Flux-resolved spectroscopy reveals that the CRSF remains constant despite a 25-fold change in flux. The spectral parameters like photon index and e-fold energy are out of phase with the pulse shape, whereas cutoff energy is in phase with the pulse shape. The sources luminosity during the on-state is $2.85 \times 10^{35}~\mathrm{erg~s^{-1}}$ , consistent with a `pencil` beam radiation pattern expected at this flux level from a collisionless gas-mediated shock. These results offer further insights into the accretion dynamics and magnetic field geometry of this system.


![[mdfiles/2504.02791.md|2504.02791]]
### AI Justification:
The paper provides insights into the "magnetic field geometry" in the context of X-ray binaries, which may have implications for understanding magnetic dynamics in plasma environments. However, its primary focus on the variability of 4U 1907+09, along with accretion dynamics, does not align closely with your interests in magnetic field amplification and interactions on larger astrophysical scales.
# (287/382) http://arxiv.org/pdf/2504.03283v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Effect of Nonlinear Surface Inflows into Activity Belts on Solar Cycle Modulation
**Mohammed H. Talafha,Kristof Petrovay,Andrea Opitz**


#mhd
### Abstract:
Converging flows are visible around bipolar magnetic regions (BMRs) on the solar surface, according to observations. Average flows are created by these inflows combined, and the strength of these flows depends on the amount of flux present during the solar cycle. In models of the solar cycle, this average flow can be depicted as perturbations to the meridional flow. In this article, we study the effects of introducing surface inflow to the surface flux transport models (SFT) as a possible nonlinear mechanism in the presence of latitude quenching for an inflow profile whose amplitude varies within a cycle depending on the magnetic activity. The results show that including surface inflows in the model in the presence of both LQ and tilt quenching (TQ) produced a polar field within a $\pm$ 1 $\sigma$ of an average cycle polar field ( $\sigma$ is the standard deviation) and a correlation coefficient of 0.85. We confirm that including inflows produces a lower net contribution to the dipole moment (10\,--\,25\%). Furthermore, the relative importance of LQ vs. inflows is inversely correlated with the dynamo effectivity range ( $\lambda_{R}$ ). With no decay term, introducing inflows into the model resulted in a less significant net contribution to the dipole moment. Including inflows in the SFT model shows a possible nonlinear relationship between the surface inflows and the solar dipole moment, suggesting a potential nonlinear mechanism contributing to the saturation of the global dynamo. For lower $\lambda_R$ ( $\lessapprox$ 10 $^\circ$ ), TQ always dominates LQ, and for higher $\lambda_R$ LQ dominate. However, including inflows will make the domination a little bit earlier in case of having a decay term in the model.


![[mdfiles/2504.03283.md|2504.03283]]
### AI Justification:
This paper provides insights into "nonlinear mechanisms" influencing solar magnetic dynamics, which may relate to your interests in "magnetic field amplification" and the "magnetic dynamics of plasmas." The examination of surface inflows in relation to the solar cycle modulation could offer theoretical models that align with your focus on how "magnetic fields behave, interact, and amplify across various scales."
# (288/382) http://arxiv.org/pdf/2503.04000v2


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Model of X-ray and extreme-UV emission from magnetically heated atmospheres in classical T Tauri stars... Case study of TW Hya
**Munehito Shoda,Riouhei Nakatani,Shinsuke Takasao**


#mhd
### Abstract:
Photoevaporation caused by X-rays and ultraviolet radiation from the central star has attracted attention as a key process driving the dispersal of protoplanetary discs. Although numerous models have been used to investigate the photoevaporation process, their conclusions vary, partly due to differences in the adopted radiation spectra of the host star in particular in the extreme ultraviolet (EUV) and soft X-ray bands. This study aims to construct the EUV and (soft) X-ray emission spectrum from pre-main-sequence stars using a physics-based model. While the high-energy radiation sources of pre-main-sequence stars include accretion shocks and magnetically heated coronae, this study focuses on the latter. An MHD model capable of reproducing the coronal emission of main-sequence stars is applied to a pre-main-sequence star TW Hya, and its feasibility is assessed by comparing the predicted and observed emission-line intensities. We find that the emission lines formed at coronal temperatures ( $T = 4-13 \times 10^6$ K) are reproduced in intensity within a factor of three. Emission lines from lower-temperature ( $T < 4 \times 10^6$ K) plasmas are systematically underestimated, with typical intensities at 10-30% of observed values, consistent with previous findings that these emissions predominantly originate from accretion shocks. Emission lines emitted at extremely high temperatures ( $T > 13 \times 10^6$ K) account for only about 1-10% of the observed values, likely due to the neglect of transient heating associated with flares. These results indicate that the quiescent coronal emission of pre-main-sequence stars can be adequately modeled using a physics-based approach.


![[mdfiles/2503.04000.md|2503.04000]]
### AI Justification:
This paper addresses magnetic dynamics indirectly by investigating the heating mechanisms in the atmospheres of T Tauri stars, which may provide insights into the role of magnetic fields in plasma environments. However, it primarily focuses on emission spectra and coronal temperatures rather than the magnetic field amplification and interaction mechanisms that are central to my research on plasmas in the interstellar medium.
# (289/382) http://arxiv.org/pdf/2504.00391v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Polarization Position Angle Swing and the Rotating Vector Model of Repeating Fast Radio Bursts
**Xiaohui Liu,Heng Xu,Jiarui Niu,Yongkun Zhang,Jinchen Jiang,Dejiang Zhou,...**


#mhd
### Abstract:
Fast radio bursts (FRBs), typically highly polarized, usually have a nearly constant polarization position angle (PA) during each burst. Some bursts show significant PA variations, and one of them was claimed to have a PA variation pattern consistent with the prediction of the rotating vector model (RVM) commonly adopted to fit the PA variations in radio pulsars. We systematically study the PA evolution pattern of 1727 bursts from three active repeating FRB sources monitored by the Five-hundred-meter Aperture Spherical Telescope (FAST). We identify 46 bursts whose PA variations are fully consistent with the RVM. However, the inferred geometrical parameters and rotation periods derived from these RVM fitting are inconsistent from each other. This suggests that the magnetosphere of the FRB central engine is constantly distorted by the FRB emitter, and the magnetic configuration is dynamically evolving.


![[mdfiles/2504.00391.md|2504.00391]]
### AI Justification:
The paper explores significant variations in polarization position angles (PA) in fast radio bursts (FRBs), which suggests a dynamic evolution of the magnetic configuration, aligning with your interest in "how magnetic fields behave, interact, and amplify" in plasma environments. Furthermore, the mention of "magnetosphere... constantly distorted" indicates engagement with the interactions between magnetic and potentially other forces, which is relevant to your focus on the "force interactions shaping magnetic dynamics."
# (290/382) http://arxiv.org/pdf/2503.23876v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Populations of evolved massive binary stars in the Small Magellanic Cloud I... Predictions from detailed evolution models
**X. -T. Xu,C. Schurmann,N. Langer,C. Wang,A. Schootemeijer,T. Shenar,...**


#mhd
### Abstract:
Context. The majority of massive stars are born with a close binary companion. How this affects their evolution and fate is still largely uncertain, especially at low metallicity. Aims. We derive synthetic populations of massive post-interaction binary products and compare them with corresponding observed populations in the Small Magellanic Cloud (SMC). Methods. We analyse 53298 detailed binary evolutionary models computed with MESA. Our models include the physics of rotation, mass and angular momentum transfer, magnetic internal angular momentum transport, and tidal spin-orbit coupling. They cover initial primary masses of 5-100Msun, initial mass ratios of 0.3-0.95, and all initial periods for which interaction is expected. They are evolved through the first mass transfer and the donor star death, a possible ensuing Be/X-ray binary phase, and they end when the mass gainer leaves the main sequence. Results.In our fiducial synthetic population, 8% of the OB stars in the SMC are post-mass transfer systems, and 7% are merger products. In many of our models, the mass gainers are spun up and form Oe/Be stars. While our model underpredicts the number of Be/X-ray binaries in the SMC, it reproduces the main features of their orbital period distribution and the observed number of SMC binary WR stars. We expect $\sim$ 50 OB+BH binaries below and $\sim$ 170 above 20d orbital period. The latter might produce merging double BHs. However, their progenitors, the predicted long-period WR+OB binaries, are not observed. Conclusions. While the comparison with the observed SMC stars supports many physics assumptions in our high-mass binary models, a better match of the large number of observed OBe stars and Be/X-ray binaries likely requires a lower merger rate and/or a higher mass transfer efficiency during the first mass transfer. The fate of the initially wide O star binaries remains uncertain.


![[mdfiles/2503.23876.md|2503.23876]]
### AI Justification:
The paper's focus on the evolution of massive binary stars, including the influence of magnetic internal angular momentum transport, somewhat overlaps with my interests in magnetic dynamics of plasmas, particularly under the section of "Force Interactions Shaping Magnetic Dynamics." However, its primary emphasis lies on binary stellar evolution and not on the broader implications of magnetic field amplification or turbulent plasma interactions that are central to my research focus.
# (291/382) http://arxiv.org/pdf/2503.22525v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### CaII and H $α$ flaring M dwarfs detected with multi-filter photometry
**P. Mas-Buitrago,J. -Y. Zhang,E. Solano,E. L. Martin**


#mhd
### Abstract:
Understanding and characterising the magnetic activity of M dwarfs is of paramount importance in the search for Earth-like exoplanets orbiting them. Energetic stellar activity phenomena, such as flares or coronal mass ejections, which are common in these stars, are deeply connected with the habitability and atmospheric evolution of the surrounding exoplanets. We present a follow-up of a sample of M dwarfs with strong H $\alpha$ and CaII H and K emission lines identified with J-PLUS photometry in a previous work. We collected low-resolution NOT/ALFOSC and GTC/OSIRIS spectra, measuring the PC3 index for the spectral type determination. We used two-minute-cadence calibrated TESS light curves to identify and characterise multiple flares and to calculate the rotation period of the two active M dwarfs found in our sample. We confirm that the strong emission lines detected in the J-PLUS photometry are caused by transient flaring activity. We find clear evidence of flaring activity and periodic variability for LP 310-34 and LP 259-39, and estimated flare energies in the TESS bandpass between $7.4\times10^{30}$ and $2.2\times10^{33}$ erg for them. We characterised LP 310-34 and LP 259-39 as very rapidly rotating M dwarfs with CaII H and K and H $\alpha$ in emission, and computed a rotation period for LP 259-39 for the first time... $P_{\rm rot}=1.69\pm0.02$ d. This work advocates the approach of exploiting multi-filter photometric surveys to systematically identify flaring M dwarfs, especially to detect episodes of strong CaII H and K line emission, which may have important implications for exoplanetary space weather and habitability studies. Our results reveal that common M dwarfs experience flare events in CaII H and K in addition to well known H $\alpha$ flares.


![[mdfiles/2503.22525.md|2503.22525]]
### AI Justification:
The paper discusses the magnetic activity and flare phenomena in M dwarfs, which indirectly relates to your interest in magnetic field behavior in astrophysical plasmas, particularly in the context of habitability and exoplanetary environments. However, the focus on M dwarf stars and their flaring characteristics diverges from your primary research interests in magnetic dynamics and interactions in the interstellar medium, making its contribution to your work more limited.
# (292/382) http://arxiv.org/pdf/2503.20857v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Intra-Cluster Light as a Dynamical Clock for Galaxy Clusters... Insights from the MAGNETICUM, IllustrisTNG, Hydrangea and Horizon-AGN Simulations
**Lucas C. Kimmig,Sarah Brough,Klaus Dolag,Rhea-Silvia Remus,Yannick M. Bahe,Garreth Martin,...**


#mhd
### Abstract:
As the most massive nodes of the cosmic web, galaxy clusters represent the best probes of structure formation. Over time, they grow by accreting and disrupting satellite galaxies, adding those stars to the brightest cluster galaxy (BCG) and the intra-cluster light (ICL). However, the formation pathways of different galaxy clusters can vary significantly. To inform upcoming large surveys, we aim to identify observables that can distinguish galaxy cluster formation pathways. Using four different hydrodynamical simulations, Magneticum, TNG100 of IllustrisTNG, Horizon-AGN, and Hydrangea, we study how the fraction of stellar mass in the BCG and ICL ( $f_{ICL+BCG}$ ) relates to the galaxy cluster mass assembly history. For all simulations, $f_{ICL+BCG}$ is the best tracer for the time at which the cluster has accumulated 50% of its mass ( $z_{f}$ ), performing better than other typical dynamical tracers, such as the subhalo mass fraction, the halo mass, and the center shift. More relaxed clusters have higher $f_{ICL+BCG}$ , in rare cases up to 90%, while dynamically active clusters have lower fractions, down to 20%, which we find to be independent of the exact implemented baryonic physics. We determine the average increase in $f_{ICL+BCG}$ from stripping and mergers to be between 3-4% per Gyr. $f_{ICL+BCG}$ is tightly traced by the stellar mass ratio between the BCG and both the second (M12) and fourth (M14) most massive cluster galaxy. The average galaxy cluster has assembled half of its halo mass by $z_{f}=0.67$ (about 6 Gyr ago), though individual histories vary significantly from $z_{f}=0.06$ to $z_{f}=1.77$ (0.8 to 10 Gyr ago). As all four cosmological simulations consistently find that $f_{ICL+BCG}$ is an excellent tracer of the cluster dynamical state, upcoming surveys can leverage measurements of $f_{ICL+BCG}$ to statistically quantify the assembly of the most massive structures.


![[mdfiles/2503.20857.md|2503.20857]]
### AI Justification:
This paper, while primarily focused on galaxy cluster formation and the role of intra-cluster light (ICL), intersects with your interest in the "complex, multi-scale dynamics of magnetic fields in plasma environments" through its use of "hydrodynamical simulations" like Magneticum and IllustrisTNG. However, it lacks a direct exploration of "magnetic field amplification" or the "interactions between magnetic, gravitational, and thermal forces," which are central to your research.
# (293/382) http://arxiv.org/pdf/2503.19060v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A Multi-viewpoint CME Catalog Based on SoloHI Observed Events
**C. Mac Cormack,S. B. Shaik,P. Hess,R. Colaninno,T. Nieves-Chinchilla**


#mhd
### Abstract:
Coronal Mass Ejections (CMEs) are significant drivers of geomagnetic activity, and understanding these structures is critical to developing and improving forecasting tools for space weather. The Solar Orbiter (SolO) mission, with its comprehensive set of remote sensing and in-situ instruments, along with its unique orbit, is significantly advancing the study of the CMEs and other structures in the heliosphere. A critical contribution to the study of CMEs by SolO is the observations from the Solar Orbiter Heliospheric Imager (SoloHI). SoloHI observes photospheric visible light scattered by electrons in the solar wind and provides high-resolution observations of the corona and heliosphere. The resolution and vantage point offered by SoloHI make it uniquely well-suited to study CME evolution in the heliosphere. We present the initial release of a living CME catalog based on SoloHI observations during its initial years of observations, with a multi-viewpoint focus. We catalog 140 events detected by SoloHI during the period of January 2022 until April 2023. For each event detected by SoloHI, we present available in-situ data and remote sensing observations detected by other missions. We identify the source region of the CME and describe its main characteristics, track the CME through the coronagraphs and heliospheric imagers, and provide in-situ detection when possible. We also provide a morphological classification and observations quality parameter based on the SoloHI observations. Additionally, we cross-check with other available CME catalogs and link to the event description provided by the Space Weather Database Of Notifications, Knowledge, Information (DONKI) catalog. We provide various observing scenarios with SoloHI observations to demonstrate the contribution that this catalog offers to the scientific community to explore the new observing viewpoint of CMEs with the SolO mission.


![[mdfiles/2503.19060.md|2503.19060]]
### AI Justification:
The paper presents a comprehensive catalog of Coronal Mass Ejections (CMEs) observed by the Solar Orbiter, which contributes to understanding the dynamic behaviors of magnetic fields in solar plasmas, albeit primarily from a solar perspective. While your interests lie specifically in the interstellar medium and magnetic field amplification through various mechanisms, the paper does provide relevant insights into the interactions and characteristics of magnetic structures, connected to turbulence and force interactions within a plasma environment, thus offering some value.
# (294/382) http://arxiv.org/pdf/2503.17082v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Collapse of Rotating White Dwarfs and Multimessenger Signals
**Takami Kuroda,Kyohei Kawaguchi,Masaru Shibata**


#mhd
### Abstract:
We present results of numerical relativity simulations of core collapse of rotating magnetized white dwarfs (WDs) in three dimension, aiming at discussing the explosion dynamics and associate multi-messenger signals... gravitational waves (GWs), neutrinos, and electromagnetic counterparts. All WDs initiate gravitational collapse due to electron captures and then experience prompt type explosions after the proto neutron star formation. We observe the explosions dominated by a bipolar structure and the emergence of strong spiral waves in rapidly rotating models. The spiral waves facilitate to increase both the explosion energy and ejecta mass, though the final values still fall in the category of low explosion energy supernovae with small ejecta mass. The spiral waves also produce strong GWs, which may expand the horizon distance of such events against GWs up to $\sim 10$ Mpc for third-generation ground-based detectors. Additionally as an intriguing implication, we demonstrate that such accretion or merger induced collapse of WDs might be able to explain some of the rapidly evolving optical transients, such as fast blue optical transients (FBOTs), as previously suggested. Based on the simulation results together with several assumptions, we confirm that the magnetar may account for the brighter side of observed FBOTs, while a combination of ejecta-envelope interaction which can be also followed by radioactive decay of heavy elements synthesized along with the explosion might still explain the fainter branch even in the absence of magnetar formation.


![[mdfiles/2503.17082.md|2503.17082]]
### AI Justification:
This paper discusses the dynamics of rotating magnetized white dwarfs, which involves **magnetic dynamics and the interactions of gravitational forces** during explosions. While it touches on aspects of **magnetic field behavior in plasmas**, its specific focus on supernova events and gravitational wave emissions sites may not align directly with your interest in the detailed mechanisms of **magnetic field amplification and interactions in the interstellar medium**.
# (295/382) http://arxiv.org/pdf/2503.16606v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Looking for the γ-Ray Cascades of the KM3-230213A Neutrino Source
**Milena Crnogorcevic,Carlos Blanco,Tim Linden**


#mhd
### Abstract:
The extreme energy of the KM3-230213A event could transform our understanding of the most energetic sources in the Universe. However, it also reveals an inconsistency between the KM3NeT detection and strong IceCube constraints on the ultra-high energy neutrino flux. The most congruous explanation for the KM3NeT and IceCube data requires KM3-230213A to be produced by a (potentially transient) source fortuitously located in a region where the KM3NeT acceptance is maximized. In hadronic models of ultra-high-energy neutrino production, such a source would also produce a bright {\gamma}-ray signal, which would cascade to GeV--TeV energies due to interactions with extragalactic background light. We utilize the {\gamma}-Cascade package to model the spectrum, spatial extension, and time-delay of such a source, and scan a region surrounding the KM3NeT event to search for a consistent {\gamma}-ray signal. We find no convincing evidence for a comparable \textit{Fermi}-LAT source and place constraints on a combination of the source redshift and the intergalactic magnetic field strength between the source and Earth.


![[mdfiles/2503.16606.md|2503.16606]]
### AI Justification:
The paper discusses the interactions of ultra-high-energy neutrinos with extragalactic background light and their implications for understanding high-energy astrophysical sources, which relate to your interest in "magnetic interactions" since it highlights the role of the "intergalactic magnetic field strength" in source detection. However, it appears to be more centered on neutrino and gamma-ray interactions rather than specifically addressing magnetic field amplification or dynamics in plasma environments, limiting its relevance to your focus.
# (296/382) http://arxiv.org/pdf/2503.16204v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Resolution of a paradox... SDSS J1257+5428 can be explained as a descendant of a cataclysmic variable with an evolved donor
**Diogo Belloni,Matthias R. Schreiber,Kareem El-Badry**


#mhd
### Abstract:
The existence of the binary system SDSS J1257+5428 has been described as paradoxical. Here we investigate under which conditions SDSS J1257+5428 could be understood as a descendant of a cataclysmic variable with an evolved donor star, which is a scenario that has never been explored in detail. We used the BSE code for pre-common-envelope (CE) evolution and the MESA code for post-CE evolution to run binary evolution simulations and searched for potential formation pathways for SDSS J1257+5428 that lead to its observed characteristics. For the post-CE evolution, we adopted a boosted version of the CARB model. We find that SDSS J1257+5428 can be explained as a post-cataclysmic-variable system if (i) the progenitor of the extremely low-mass WD was initially a solar-type star that evolved into a subgiant before the onset of mass transfer and underwent hydrogen shell flashes after the mass transfer stopped, (ii) the massive WD was highly or entirely rejuvenated during the cataclysmic variable evolution, and (iii) magnetic braking was strong enough to make the evolution convergent. In this case, the torques due to magnetic braking need to be stronger than those provided by the CARB model by a factor of ${\sim100}$ . We conclude that SDSS J1257+5428 can be reasonably well explained as having originated from a cataclysmic variable that hosted an evolved donor star and should no longer be regarded as paradoxical. If our formation channel is correct, our findings provide further support that stronger magnetic braking acts on progenitors of (i) close detached WD binaries, (ii) close detached millisecond pulsar with extremely low-mass WDs, (iii) AM CVn binaries, and (iv) ultra-compact X-ray binaries, in comparison to the magnetic braking strength required to explain binaries hosting main-sequence stars and single main-sequence stars.


![[mdfiles/2503.16204.md|2503.16204]]
### AI Justification:
The paper provides insights into magnetic braking in binary systems, which relates to my interest in how "magnetic fields behave" and "interact" within plasma environments. Specifically, the focus on "stronger magnetic braking" affecting the evolution of various binary systems hints at mechanisms that may also be applicable to understanding "magnetic dynamics" in the broader context of astrophysical plasmas.
# (297/382) http://arxiv.org/pdf/2503.14236v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Comparison Between Cycle-to-Cycle Variations in the Coefficient of Joys Law and Covariance of Rotation Residuals and Meridional Motions of Sunspot Groups
**J. Javaraiah**


#mhd
### Abstract:
The tilts of bipolar magnetic regions are believed to be caused by the action of Coriolis force on rising magnetic flux tubes. Here we analysed the combined Greenwich and Debrecen observatories sunspot-group data during the period 1874-2017 and the tilt angles of sunspot groups measured at Mt. Wilson Observatory during the period 1917-1986 and Debrecen Observatory during the period 1994-2013. We find that there exists about 8-solar cycle (Gleissberg cycle) trend in the long-term variation of the slope of Joys law (increase of tilt angle with latitude). There exists a reasonably significant correlation between the slope/coefficient of Joys law and the slope (namely, residual covariance) of the linear relationship between the rotation residuals and meridional motions of sunspot groups in the northern hemisphere and also in the southern hemisphere during Solar Cycles 16-21. We also find that there exists a good correlation between north--south difference (asymmetry) in the coefficient of Joys law and that in the residual covariance. We consider the residual covariance represents tentatively the coefficient of angular momentum transport. These results suggest that there exists a relationship between the surface/subsurface poleward/equatorward angular momentum transport and the Joys law. There is a suggestion of the strength of the Joys law depends on the strength of the poleward angular momentum transport.


![[mdfiles/2503.14236.md|2503.14236]]
### AI Justification:
This paper explores the "tilts of bipolar magnetic regions" caused by the "Coriolis force on rising magnetic flux tubes," linking it to critical dynamics of magnetic fields that could be informative for your interest in "magnetic field amplification" and "force interactions shaping magnetic dynamics" in plasma environments. Additionally, while it focuses more on solar dynamics, the examination of "angular momentum transport" related to magnetic field behavior offers insights that may stimulate new perspectives in understanding the "scale-dependent magnetic structuring" you wish to explore within the interstellar medium.
# (298/382) http://arxiv.org/pdf/2503.13683v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Innermost stable circular orbits around a Reissner-Nordström-global monopole spacetime in a homogeneous magnetic field
**Hamza M. Haddad,M. Haluk Secuk,Ozgur Delice**


#mhd
### Abstract:
We investigate the dynamics of charged particles in the spacetime of a global monopole swallowed by a Reissner-Nordstr\`om (RN) black hole in the presence of a external weak asymptotically homogeneous magnetic field. We carefully analyze and deduce the conditions to have such a magnetic field around this black hole and show that this is indeed possible in the small but nontrivial charge and monopole term limit. We obtain general equations of motion and analyze them for special cases of circular orbits, focusing on the inner-most stable circular orbit (ISCO) of this configuration. The richness of the parameters and complicated forms of the resulting equations of motion necessitate a numerical approach. Hence, we have presented our results with numerous graphs, which help to understand the evolution of ISCO as a function of the external test magnetic field and the monopole term depending on the parameters of the black hole, such as its electrical charge as well as the properties of the test particle such as its specific charge, angular momentum, and energy. We have also analyzed the effective potential that these fields generate and deduced results for the aforementioned values of external and internal parameters of spacetime.


![[mdfiles/2503.13683.md|2503.13683]]
### AI Justification:
This paper explores the dynamics of charged particles in the context of a magnetic field around a black hole, which relates to my interest in **how magnetic fields behave and interact** within plasma environments. However, it primarily focuses on gravitational dynamics and black hole physics rather than the **magnetic field amplification** and **emergent magnetic dynamics** in interstellar plasma, leading to a less direct relevance to my theoretical astrophysics research.
# (299/382) http://arxiv.org/pdf/2503.12807v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The effect of stellar evolution on dispersal of protoplanetary disks... Disk fraction in star-forming regions
**Ayano Komaki,Naoki Yoshida**


#mhd
### Abstract:
We study the effect of stellar evolution on the dispersal of protoplanatary disks by performing one-dimensional simulations of long-term disk evolution. Our simulations include viscous disk accretion, magnetohydrodynamic winds, and photoevaporation as important disk dispersal processes. We consider a wide range of stellar mass of $0.1$ - $7M_{\odot}$ , and incorporate the luminosity evolution of the central star. For solar-mass stars, stellar evolution delays the disk dispersal time as the FUV luminosity decreases toward the main sequence. In the case of intermediate-mass stars, the FUV luminosity increases significantly over a few million years, driving strong photoevaporation and enhancing disk mass loss during the later stages of disk evolution. This highlights the limitations of assuming a constant FUV luminosity throughout a simulation. Photoevaporation primarily impacts the outer regions of the disk and is the dominant disk dispersal process in the late evolutionary stage. Based on the results of a large set of simulations, we study the evolution of a population of star-disk systems and derive the disk fraction as a function of time. We demonstrate that the inclusion of stellar luminosity evolution can alter the disk fraction by several tens of percent, bringing the simulations into closer agreement with recent observations. We argue that it is important to include the stellar luminosity evolution in simulations of the long-term dispersal of protoplanetary disks.


![[mdfiles/2503.12807.md|2503.12807]]
### AI Justification:
While the paper focuses on the dispersal of protoplanetary disks and the role of stellar evolution in this process, it does touch on magnetohydrodynamic (MHD) dynamics, which is relevant to your interest in "magnetic dynamics of plasmas in the interstellar medium." However, it primarily examines disk evolution rather than the amplification and interaction of magnetic fields or their emergent behaviors in turbulent plasmas, making it less aligned with your specific research focus.
# (300/382) http://arxiv.org/pdf/2503.12675v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Discovery of two new polars evolved past the period bounce
**Tim Cunningham,Ilaria Caiazzo,Gracjan Sienkiewicz,Peter J. Wheatley,Boris T. Gansicke,Kareem El-Badry,...**


#mhd
### Abstract:
We report the discovery of two new magnetic cataclysmic variables with brown dwarf companions and long orbital periods ( $P_{\rm orb}=95\pm1$ and $104\pm2$ min). This discovery increases the sample of candidate magnetic period bouncers with confirmed sub-stellar donors from four to six. We also find their X-ray luminosity from archival XMM-Newton observations to be in the range $L_{\rm X}\approx10^{28} $ $ - $ $ 10^{29} \mathrm{erg\,s^{-1}} $ in the 0.25 $ -$ 10 keV band. This low luminosity is comparable with the other candidates, and at least an order of magnitude lower than the X-ray luminosities typically measured in cataclysmic variables. The X-ray fluxes imply mass transfer rates that are much lower than predicted by evolutionary models, even if some of the discrepancy is due to the accretion energy being emitted in other bands, such as via cyclotron emission at infrared wavelengths. Although it is possible that some or all of these systems formed directly as binaries containing a brown dwarf, it is likely that the donor used to be a low-mass star and that the systems followed the evolutionary track for cataclysmic variables, evolving past the period bounce. The donor in long period systems is expected to be a low-mass, cold brown dwarf. This hypothesis is supported by near-infrared photometric observations that constrain the donors in the two systems to be brown dwarfs cooler than $\approx$ 1100 K (spectral types T5 or later), most likely losing mass via Roche Lobe overflow or winds. The serendipitous discovery of two magnetic period bouncers in the small footprint of the XMM-Newton source catalog implies a large space density of these type of systems, possibly compatible with the prediction of 40 $-$ 70 per cent of magnetic cataclysmic variables to be period bouncers.


![[mdfiles/2503.12675.md|2503.12675]]
### AI Justification:
This paper discusses the discovery of two new magnetic cataclysmic variables, which aligns with my interest in "magnetic dynamics" and "magnetic field amplification" within astrophysical contexts. However, the focus on cataclysmic variables and their specific X-ray luminosity measurements does not directly address the broader plasma dynamics or the multi-scale interaction of magnetic fields I study in the interstellar medium.
# (301/382) http://arxiv.org/pdf/2503.11009v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### An Innovative Heterodyne Microwave Interferometer for Plasma Density Measurements on the Madison AWAKE Prototype
**Marcel Granetzny,Barret Elward,Oliver Schmitz**


#mhd
### Abstract:
The Madison AWAKE Prototype (MAP) is a high-power, high-density helicon plasma experiment. The projects main goal is to develop a scalable plasma source for use in a beam-driven plasma wakefield accelerator as part of the AWAKE project. We measure the plasma density with a new heterodyne microwave interferometer that features several improvements over traditional approaches. The design uses a single microwave source combined with an upconverter to avoid frequency drift and reduce overall cost. Elliptical mirrors focus the probe beam into the plasma and guide it back to the receiver. The transmitter and receiver along with the measurement electronics are co-located in a small enclosure and are assisted by two small mirrors on the opposite side of MAP. Both halves of the system move independently on computer-controlled motion platforms. This setup enables fast repositioning of the interferometer to measure at any axial location despite the magnets, wiring and structural supports that would block movement of a waveguide-based system. A high-speed, high-precision mixed signal circuit and FPGA analyze the probe signal directly in the enclosure which obviates the need for a digitizer or oscilloscope. The interferometer resolves phase shifts down to one hundredth of a fringe, resulting in a line-averaged resolution of $1.5\mathrm{\cdot 10^{17}\; m^{-3}} $ . The system provides a real-time measurement every $ 5\;\mathrm{\mu s}$ up into the mid $\mathrm{10^{19}\; m^{-3}}$ density range with a noise level of $1.0\mathrm{\cdot 10^{17}\; m^{-3}}$ .


![[mdfiles/2503.11009.md|2503.11009]]
### AI Justification:
The paper presents an innovative approach to measuring plasma density in a high-density plasma environment, which is relevant to your interest in plasma dynamics. However, it primarily focuses on technological advancements in measurement techniques rather than directly addressing the magnetic field amplification and interactions of magnetic forces which are central to your research focus.
# (302/382) http://arxiv.org/pdf/2503.10739v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Rapid far-infrared spectral timing of X-ray binaries with PRIMA
**Alexandra J. Tetarenko,Poshak Gandhi,Devraj Pawar**


#mhd
### Abstract:
The most powerful cosmic engines in our universe are fueled by compact objects. These objects accrete large amounts of material and eject matter in the form of jets. Recent groundbreaking discoveries of gravitational waves from merging compact objects and the direct imaging of the black hole shadows with the Event Horizon Telescope represent major steps forward in our understanding of such systems. However, there exists a large population of stellar-mass compact objects in our own Galaxy, present in X-ray binaries (XRBs), which provide better laboratories with which to study the processes of accretion and ejection. XRBs produce highly variable emissions on timescales ranging from milliseconds (for light-travel time in the region close to the compact object) to weeks (governing the mass-inflow process). Therefore, high-time resolution observations can be a powerful tool to study these systems. However, as XRBs emit across the electromagnetic spectrum, a suite of facilities is needed to take full advantage of these techniques. The PRIMA Observatory (PRobe far-Infrared Mission for Astrophysics) will provide unique access to a wavelength range that has not been sampled in XRBs, representing an exciting new possibility for characterizing rapid time-domain phenomena of XRBs (and potentially other transient sources) in the far-infrared regime.


![[mdfiles/2503.10739.md|2503.10739]]
### AI Justification:
The paper discusses rapid spectral timing and observations of X-ray binaries, focusing on accretion processes and dynamic ejecta, which may provide insights into force interactions shaping magnetic dynamics. However, it does not directly address the amplification or the emergent behaviors of magnetic fields in plasma environments, which are central to your research interests.
# (303/382) http://arxiv.org/pdf/2503.00130v2


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Filamentary Ejecta Network in Cassiopeia~A Reveals Fingerprints of the Supernova Explosion Mechanism
**S. Orlando,H. -T. Janka,A. Wongwathanarat,D. Dickinson,D. Milisavljevic,M. Miceli,...**


#mhd
### Abstract:
[Abridged] Recent JWST observations have revealed an intricate filamentary network of unshocked ejecta in the young supernova remnant (SNR) Cassiopeia A (Cas A), offering new insights into supernova (SN) explosions and ejecta evolution. We investigate the origin and evolution of this structure by (i) characterizing its 3D morphology and kinematics and (ii) identifying the physical mechanisms driving its formation. Using high-resolution hydrodynamic (HD) and magneto-hydrodynamic (MHD) simulations, we model the evolution of a neutrino-driven SN from explosion to a remnant age of 1000 years. The initial conditions, set just after shock breakout, are based on a 3D neutrino-driven SN model matching Cas As basic properties. We find that magnetic fields have little impact on unshocked ejecta evolution, so we focus on HD simulations. A web-like filamentary structure, consistent with JWST observations (down to $\sim 0.01$ pc), naturally forms during the explosion. These filaments arise from early post-collapse processes, including neutrino-heated bubble expansion, hydrodynamic instabilities during blast propagation, and the Ni-bubble effect after shock breakout. The reverse shock later disrupts the filaments via hydrodynamic instabilities, rendering them unobservable by $\sim 700$ years. Our models suggest that JWST-detected filaments in Cas A preserve a memory of early explosion conditions, tracing processes active during and immediately after the SN event. Notably, a filamentary network akin to Cas As emerges naturally from a neutrino-driven SN explosion.


![[mdfiles/2503.00130.md|2503.00130]]
### AI Justification:
This paper discusses the "origin and evolution" of filamentary structures in supernova remnants, which aligns with your interest in "magnetic dynamics of plasmas" and how "magnetic fields behave, interact, and amplify." Although the paper primarily focuses on hydrodynamics and notes that "magnetic fields have little impact," the use of MHD simulations may still provide insights into the interplay between magnetic and hydrodynamic forces relevant to your research on "force interactions shaping magnetic dynamics."
# (304/382) http://arxiv.org/pdf/2503.09682v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Probing the Axion-Electron Coupling with NuSTAR Observations of Galaxies
**Orion Ning,Benjamin R. Safdi**


#mhd
### Abstract:
We search for the existence of ultralight axions coupling to electrons and photons using data from the NuSTAR telescope directed toward the galaxies M82, M87, and M31. We focus on electron bremsstrahlung and Compton scattering for axion production in stars, summing over the stellar populations found in the target galaxies when computing the axion luminosity. We then compute the hard X-ray signal that arises from the conversion of these axions to photons in each galaxys magnetic fields, inferred from analog galaxies in cosmological magnetohydrodynamic simulations. Analyzing NuSTAR data toward these galaxies between roughly 20 to 70 keV, we find no evidence for axions and set leading constraints on the combined axion-electron and axion-photon coupling at the level of $|g_{aee} \times g_{a \gamma \gamma}| \lesssim 8.3 \times 10^{-27}$ GeV $^{-1}$ for $m_a \lesssim 10^{-10}$ eV at 95% confidence, with M82 providing the most stringent constraints.


![[mdfiles/2503.09682.md|2503.09682]]
### AI Justification:
This paper investigates the interactions between magnetic fields and axion phenomena, implying a connection to the "scale-dependent magnetic structuring" I am interested in, specifically through its examination of magnetic fields in galaxies as per cosmological magnetohydrodynamic simulations. However, while the study touches on magnetic dynamics and uses observations of galaxies, it lacks direct focus on the "magnetic field amplification" and "emergent magnetic dynamics" that are central to my research.
# (305/382) http://arxiv.org/pdf/2503.09295v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Strong Field QED, Astrophysics, and Laboratory Astrophysics
**Sang Pyo Kim**


#mhd
### Abstract:
Astrophysical compact objects, such as magnetars, neutron star mergers, etc, have strong electromagnetic fields beyond the Schwinger field ( $B_c = 4.4 \times 10^{13}\, {\rm G}$ ). In strong electric fields, electron-positron pairs are produced from the vacuum, gamma rays create electron-positron pairs in strong magnetic fields, and propagating photons experience vacuum refringence, etc. Astrophysical compact objects with strong electromagnetic fields open a window for probing fundamental physics beyond weak field QED. Ultra-intense lasers and high-energy charged particles may simulate extreme astrophysical phenomena.


![[mdfiles/2503.09295.md|2503.09295]]
### AI Justification:
This paper is somewhat relevant to your interests in theoretical astrophysics and plasma physics, particularly through its focus on "strong electromagnetic fields" in astrophysical compact objects, which relates to your interest in "magnetic field amplification." However, it does not adequately address the broader topics of magnetic dynamics, interactions between forces, or turbulent plasmas that are central to your research focus.
# (306/382) http://arxiv.org/pdf/2502.17689v2


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Relationship between the $γ-$ ray variability and the pc-scale jet in the blazar 3C 454.3
**Eva Palafox,Victor Manuel Patino-Alvarez,Vahram Chavushyan,Sergio A. Dzib,Andrei Lobanov,J. Anton Zensus**


#mhd
### Abstract:
3C 454.3 is a flat spectrum radio quasar (FSRQ) known for its high variability across the electromagnetic spectrum, showing structural and flux variability in its pc-scale jet, and correlated variability among frequency bands. This study aims to identify the structure, dynamics, and radiative processes common to the innermost regions of the blazar 3C 454.3. We investigate whether any jet component can be associated with $\gamma-$ ray emission and variability. We analyze the relationship between the variable $\gamma-$ ray emission and pc-scale jet properties in 3C 454.3 by combining $\gamma-$ ray data spanning twelve years with contemporaneous VLBA multi-epoch images at 15 and 43 GHz. Spearman rank correlation tests are conducted to determine if the flux variability of any jet component is associated with $\gamma-$ ray variability. Core emission at 43 and 15 GHz strongly correlates with $\gamma-$ ray emission. The 43 GHz core (Q0) contributes around 37 $\%$ of the observed $\gamma-$ ray variability, while the 15 GHz core (K0) accounts for 30 $\%$ . A quasi-stationary component at 43 GHz, at a projected distance of 4.6 pc, correlates with the $\gamma-$ ray flux, accounting for 20 $\%$ of its emission between 2016 and 2021. We found a mobile component (Q3 between 2010.18 and 2011.16) at 43 GHz with a projected distance between 0.8 and 2.3 pc and apparent velocity of $\beta_{app} = 9.9 \pm 1.1$ c, accounting for approximately 28% of the $\gamma-$ ray emission. The observed simultaneous variability in emission regions beyond the central parsec strongly suggests synchrotron self-Compton (SSC) as the primary mechanism for $\gamma-$ ray production in these regions. Our findings demonstrate the existence of multiple $\gamma-$ ray emission regions within the blazar jet but also suggest that some of these regions are non-stationary over time.


![[mdfiles/2502.17689.md|2502.17689]]
### AI Justification:
This paper discusses the variability and dynamics of the γ-ray emission from the blazar 3C 454.3, focusing on the structure of its pc-scale jet and how it correlates with γ-ray activity, which may provide insights into the interactions of magnetic fields within these jet regions. However, it lacks a direct exploration of magnetic field amplification or the emergent dynamics of magnetic fields in plasma environments, thus providing limited value to my specific research interests in theoretical astrophysics and plasma physics.
# (307/382) http://arxiv.org/pdf/2503.09540v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Reduced atomic models for large-scale computations... Fe XIII near-infrared lines
**Giulio Del Zanna,Supriya Hebbur Dayananda**


#mhd
### Abstract:
Accurate atomic models for astrophysical plasma can be very complex, requiring thousands of states. However, for a variety of applications such as large-scale forward models of the Stokes parameters of a spectral line in the solar corona, it is necessary to build much reduced atomic models. We present two examples of such models, focused on the two near-infrared Fe XIII lines observed on the ground at 10750, 10801 Angstroms. These lines are primary diagnostics for a range of missions (especially the Daniel K. Inouye Solar Telescope, DKIST) to measure electron densities and magnetic fields in the solar corona. We calculate the Stokes parameters for a range of coronal conditions using CHIANTI (for intensities) and P-CORONA (for intensities and polarization), and use P-CORONA and a realistic global MHD simulation to show that the reduced models provide accurate results, typically to within 5% those obtained with larger models. Reduced models provide a significant decrease (over three orders of magnitude) in the computational time in spectropolarimetric calculations. The methods we describe are general and can be applied to a range of conditions and other ions.


![[mdfiles/2503.09540.md|2503.09540]]
### AI Justification:
This paper touches on the interaction between magnetic fields and plasma through the development of reduced atomic models for astrophysical plasma, which could indirectly inform your interests in "magnetic field amplification" and the "behavior of magnetic fields" within plasma environments. Although it focuses primarily on the solar corona and spectral diagnostics, the methodology involving global MHD simulations may offer insights relevant to understanding the magnetic dynamics you are studying.
# (308/382) http://arxiv.org/pdf/2503.09161v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The role of Trees of Fragmenting Granules (TFG) in the formation of the solar supergranular pattern from Hinode observations
**Jean-Marie Malherbe,Thierry Roudier**


#mhd
### Abstract:
We present in this paper an exceptional scientific dataset allowing to investigate the structure and evolution of the interior of solar supergranulation cells. Trees of Fragmenting Granules (TFG) and associated flows were evidenced using Local Correlation Tracking techniques (LCT) from a 24 H duration sequence of Hinode (JAXA/NASA) observations. The treatment of the dataset exhibits the evolution of the TFG and shows that their mutual interactions are able to build horizontal flows with longer lifetime than granules (1 to 2 hours) over a scale of 10 arcsec (the mesogranulation). These flows act on the diffusion of the intranetwork magnetic elements and also on the location and shape of the network. Hence, the TFG appear as one of the major elements involved in supergranular formation and evolution.


![[mdfiles/2503.09161.md|2503.09161]]
### AI Justification:
This paper provides insight into the interactions and dynamics of magnetic fields within a specific plasma environment, solar supergranulation, which could offer a unique perspective on how magnetic dynamics operate at different scales. While it focuses on the solar context rather than the interstellar medium, the examination of "mutual interactions" between granules and associated magnetic elements may hold implications for understanding magnetic field behavior in broader astrophysical plasmas.
# (309/382) http://arxiv.org/pdf/2503.08036v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A long-period radio transient active for three decades
**N. Hurley-Walker,N. Rea,S. J. McSweeney,B. W. Meyers,E. Lenc,I. Heywood,...**


#mhd
### Abstract:
Recently several long-period radio transients have been discovered, with strongly polarised coherent radio pulses appearing on timescales between tens to thousands of seconds [1,2]. In some cases the radio pulses have been interpreted as coming from rotating neutron stars with extremely strong magnetic fields, known as magnetars; the origin of other, occasionally periodic and less well-sampled radio transients, is still debated [3]. Coherent periodic radio emission is usually explained by rotating dipolar magnetic fields and pair production mechanisms, but such models do not easily predict radio emission from such slowly-rotating neutron stars and maintain it for extended times. On the other hand, highly magnetic isolated white dwarfs would be expected to have long spin periodicities, but periodic coherent radio emission has not yet been directly detected from these sources. Here we report observations of a long-period (21 minutes) radio transient, which we have labeled GPMJ1839-10. The pulses vary in brightness by two orders of magnitude, last between 30 and 300 seconds, and have quasi-periodic substructure. The observations prompted a search of radio archives, and we found that the source has been repeating since at least 1988. The archival data enabled constraint of the period derivative to $<3.6\times10^{-13}$ s s $^{-1}$ , which is at the very limit of any classical theoretical model that predicts dipolar radio emission from an isolated neutron star.


![[mdfiles/2503.08036.md|2503.08036]]
### AI Justification:
The paper investigates the behavior of magnetic fields in the context of rotating neutron stars, specifically addressing their long-period radio emissions, which falls within my interest in how "magnetic fields behave, interact, and amplify across various scales." However, while it touches on magnetic dynamics, it primarily focuses on specific astrophysical sources rather than the broad multi-scale dynamics of plasmas that I am most interested in, making it somewhat tangential to my core research focus.
# (310/382) http://arxiv.org/pdf/2503.08320v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Detection of the white-dwarf spin of V1082 Sgr
**I. J. Lima,G. Tovmassian,C. V. Rodrigues,A. S. Oliveira,G. J. M. Luna,D. A. H. Buckley,...**


#mhd
### Abstract:
We report on the discovery of circular polarization modulated with a period of 1.943 +- 0.002 h in the cataclysmic variable V1082 Sgr. These findings unambiguously reveal the rotation of a magnetic white dwarf and establish its intermediate polar (IP) nature. Along with its extraordinary long orbital period, Porb, of 20.8 h, the spin period (Pspin) places this system in an extreme position of the Pspin versus Porb distribution. The circular polarization phase diagram has a single peak and an amplitude smaller than 1%. These data were used to model the post-shock region of the accretion flow on the white-dwarf surface using the CYCLOPS code. We obtained a magnetic field in the white-dwarf pole of 11 MG and a magnetospheric radius consistent with the coupling region at around 2 - 3 white-dwarf radii. The Pspin/Porb value and the estimated magnetic field momentum suggest that V1082 Sgr could be out of spin equilibrium, in a spin-up state, possibly in a stream accretion mode.


![[mdfiles/2503.08320.md|2503.08320]]
### AI Justification:
While the paper discusses the magnetic dynamics of a white dwarf, which involves magnetic fields, it primarily focuses on the specific case of circular polarization and the behavior of a magnetic white dwarf in a cataclysmic variable system. This narrow focus on a stellar object, including the methods used to model the magnetic field in the context of an accretion flow, does not directly align with my broader interest in the magnetic dynamics across different environments and scales in the interstellar medium.
# (311/382) http://arxiv.org/pdf/2503.05076v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Temporal Variations in Asteroseismic Frequencies of KIC 6106415... Insights into the Solar-Stellar Activity from GOLF and Kepler Observations
**Christopher J. Lombardi,Alexander G. Kosovichev,Keitarou Matsumoto**


#mhd
### Abstract:
The Global Oscillations at Low Frequencies instrument aboard the Solar and Heliospheric Observatory has provided over two decades of continuous, high-precision data, enabling detailed measurements of the Suns oscillation frequencies. These oscillations, analyzed through Doppler velocity shifts, offer invaluable insights into the Suns internal structure and dynamics using the methods of helioseismology. This methodology has been extended beyond the Sun to the study of other stars, leveraging data from various space missions. Notably, NASAs Kepler mission, in operation from 2009 until 2018, observed over 500,000 stars, analyzing brightness variations over time and generating a vast database for asteroseismic studies. This investigation focuses on the solar-type star KIC 6106415, comparing its oscillation frequencies with those derived from GOLF data. By analyzing frequency patterns and mode lifetimes, we explore the similarities and differences in internal structures, stellar evolution, and magnetic activity cycles between KIC 6106415 and the Sun. Our analysis reveals that KIC 6106415 exhibits starspot numbers similar to the Sun, peaking at an estimated 175, which is consistent with its faster rotation rate. The data suggest that KIC 6106415 may have shorter magnetic activity cycles than the Sun, reinforcing the established link between stellar rotation and magnetic field generation in solar-type stars.


![[mdfiles/2503.05076.md|2503.05076]]
### AI Justification:
The paper’s focus on asteroseismic frequencies and magnetic activity cycles in solar-type stars presents a somewhat tangential relevance to my research on magnetic field dynamics in astrophysical plasmas. While it does touch on "magnetic field generation" and the relationship between stellar rotation and magnetic properties, it does not directly address the amplification, interactions, or multi-scale dynamics of magnetic fields within plasma environments that are central to my interests.
# (312/382) http://arxiv.org/pdf/2503.03670v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Study of an active region prominence using spectropolarimetric data in the He I D3 multiplet
**S. Esteban Pozuelo,A. Asensio Ramos,J. Trujillo Bueno,R. Ramelli,F. Zeuner,M. Bianda**


#mhd
### Abstract:
Prominences are cool overdensities of plasma supported by magnetic fields that levitate in the solar corona. The physical characterization of these structures is key for understanding the magnetic field in the corona. Our work attempts to shed light on the properties of prominences by using observations at high polarimetric sensitivity in the He I D3 multiplet taken with the Zurich Imaging Polarimeter-3 instrument at the Istituto ricerche solari Aldo e Cele Dacco observatory. We used the HAZEL inversion code to infer the thermodynamic and magnetic properties of an active region prominence, assuming one- and two-component models. Our observations unveil a great diversity of physical conditions in the prominence. The observed Stokes profiles are usually broad and show interesting features, which can be described assuming a two-component model. The contribution of each component and the trends inferred for some parameters vary with the distance to the solar limb. While both components have analogous properties and contribute similarly close to the limb, a major component mainly describes the properties inferred at 10-40 arcsecs away from the limb. Moreover, both components usually show significant differences in thermal broadening, which is essential for ensuring a good fit quality between observations and synthetic profiles. Summarizing, the observed region of the prominence shows line-of-sight velocities of 1-3 km/s and rather horizontal fields of 20-80 gauss. We also report hints of a twist close to a prominence foot and changes in the magnetic configuration at specific locations. Our results indicate a mainly horizontal magnetic field of a few tens of gauss in the prominence. A model of two components with different thermal broadenings and filling factors, depending on the limb distance, is crucial for providing a consistent solution across most of the observed prominence.


![[mdfiles/2503.03670.md|2503.03670]]
### AI Justification:
The paper focuses on the magnetic properties of solar prominences, which, while specific to the solar corona, engages with my interests in "magnetic field amplification" and "force interactions shaping magnetic dynamics" in plasma environments. The use of polarimetric sensitivity to explore the "diversity of physical conditions" and "horizontal magnetic fields" aligns with my research on the interaction and evolution of magnetic fields across various scales, although it is primarily limited to solar phenomena.
# (313/382) http://arxiv.org/pdf/2503.01321v1


### Rating: 5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 50%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Core-collapse supernovae
**Anders Jerkstrand,Dan Milisavljevic,Bernhard Muller**


#mhd
### Abstract:
Core-collapse supernovae (CCSNe) are the explosive end-points of stellar evolution for $M_{ZAMS} \gtrsim 8$ $M_\odot$ stars. The cores of these stars collapse to neutron stars, a process in which high neutrino luminosity drives off the overlying stellar layers, which get ejected with thousands of kilometers per second. These supernovae enrich their host galaxies with elements made both during the stars life and in the explosion, providing the main cosmic source of elements such as oxygen, neon and silicon. Their high luminosities ( $\sim$ $10^{42}$ erg s $^{-1}$ at peak) make SNe beacons to large distances, and their light curves and spectra provide rich information on single and binary stellar evolution, nucleosynthesis, and a diverse set of high-energy physical processes. As the SN ejecta sweep up circumstellar and interstellar matter, it eventually enters a supernova remnant phase, exemplified by nearby, spatially resolved remnants such as Cas A and the Crab Nebula. In this phase, shocks and pulsar winds continue to light up the interior of the exploded stars, giving detailed information about their 3D structure. We review the central concepts of CCSNe, from the late stages of evolution of massive stars, through collapse, explosion, and electromagnetic display, to the final remnant phase. We briefly discuss still open questions, and current and future research avenues.


![[mdfiles/2503.01321.md|2503.01321]]
### AI Justification:
While the paper on core-collapse supernovae primarily focuses on the explosive endpoints of stellar evolution and the stellar components involved, it briefly touches on aspects that could relate to magnetic dynamics as the supernova ejecta interacts with circumstellar and interstellar matter. However, it lacks a specific focus on magnetic field amplification, force interactions in plasma, and the emergent magnetic dynamics that are central to your research interests in theoretical astrophysics and plasma physics.
# (314/382) http://arxiv.org/pdf/2504.07699v1


### Rating: 4/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 40%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### How to identify the object with mass range of $(2.2-3)M_\odot$ in the merger of compact star systems
**ZhaoWei Du,HouJun Lu,Xiaoxuan Liu,XiLong Fan,EnWei Liang**


#mhd
### Abstract:
High-frequency gravitational-wave (GW) radiation has been detected by LIGO-Virgo-KAGRA in the merger of compact stars. However, two GW events, GW190814 and GW200210, the mass of one companion object falls into the mass region of $(2.2-3)\rm~M_\odot$ , and how to identify such object (e.g., as a low-mass black hole (BH) or a massive neutron star (NS)) remains an open question. In this paper, we propose a method to identify the mystery compact object (MCO) with the mass region of $(2.2-3)\rm~M_\odot$ in a binary system via the possible electromagnetic (EM) radiations before and after the mergers. A multi-band EM emission can be produced with $L\propto(-t)^{7/4}$ (or $L\propto(-t)^{-5/4}$ ) during the inspiral phase due to the BH battery (or interaction magnetospheres) mechanism, and a bright (or dark) kilonova emission is powered by radioactive decay with ejecta mass ratio $q>1.7$ (or $q<1.7$ ) during the post-merge state when MCO is as a low-mass BH (or massive NS) to merger with NS. Moreover, by considering the merger system between MCO and a BH when MCO is a massive NS, we find that it requires the BH with high spin (e.g., $a\sim0.8-0.99$ ) to make sure the tidal disruption event (TDE) occurred, and a multi-band precursor emission and bright kilonova emission can also be produced during the inspiral phase and post-merge state, respectively. In any case, no matter which mechanism we adopt, such precursor emissions are too weak to be detected by most current telescopes unless the distance is close enough.


![[mdfiles/2504.07699.md|2504.07699]]
### AI Justification:
This paper is tangentially relevant to my research interests as it discusses gravitational-wave events in mergers of compact stars, which indirectly relate to the magnetic dynamics of plasmas through the mention of "interaction magnetospheres" and how these systems evolve. However, the primary focus is on the identification of compact objects and their related electromagnetic emissions rather than on magnetic field amplification or force interactions shaping magnetic dynamics, which are central to my work.
# (315/382) http://arxiv.org/pdf/2503.22337v2


### Rating: 4/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 40%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Adding further pieces to the synchronization puzzle... QBO, bimodality, and phase jumps
**F. Stefani,G. M. Horstmann,G. Mamatsashvili,T. Weier**


#mhd
### Abstract:
This work builds on a recently developed self-consistent synchronization model of the solar dynamo which attempts to explain Rieger-type periods, the Schwabe/Hale cycle and the Suess-de Vries and Gleissberg cycles in terms of resonances of various wave phenomena with gravitational forces exerted by the orbiting planets. We start again from the basic concept that the spring tides of the three pairs of the tidally dominant planets Venus, Earth and Jupiter excite magneto-Rossby waves at the solar tachocline. While the quadratic action of the sum of these three waves comprises the secondary beat period of 11.07 years, our main focus is now on the action of the even more pronounced period of 1.723 years. We show that this term excites dynamo vacillations with periods that are typical for the quasi-biennial oscillation (QBO). While bimodality of the sunspot distribution is shown to be a general feature of synchronization, it becomes most strongly expressed under the influence of the QBO. This may explain the observation that the solar activity is relatively subdued when compared to that of other sun-like stars. We also discuss anomalies of the solar cycle, and subsequent phase jumps by 180 degrees. In this connection it is noted that the very 11.07-yr beat period is rather sensitive to the time-averaging of the quadratic functional of the waves and prone to phase jumps of 90 degrees. On this basis, we propose an alternative explanation of the observed 5.5-year phase jumps in algae-related data from the North Atlantic and Lake Holzmaar that were hitherto attributed to optimal growth conditions.


![[mdfiles/2503.22337.md|2503.22337]]
### AI Justification:
While the paper explores the synchronization of the solar dynamo and periods of solar activity, it primarily focuses on the effects of gravitational forces and wave phenomena rather than the amplification and dynamics of magnetic fields in astrophysical plasmas, which aligns with your research interests. The mention of “dynamo vacillations” could intersect with your focus on magnetic field evolution, but the overall emphasis on synchronization and solar cycles deviates from your search for detailed insights into magnetic dynamics within the interstellar medium.
# (316/382) http://arxiv.org/pdf/2503.13720v1


### Rating: 4/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 40%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Exploring polarization and geometry in the X-ray pulsar 4U 1538-52
**Vladislav Loktev,Sofia V. Forsblom,Sergey S. Tsygankov,Juri Poutanen,Alexander A. Mushtukov,Alessandro Di Marco,...**


#mhd
### Abstract:
The Imaging X-ray Polarimetry Explorer (IXPE) observations of accreting X-ray pulsars (XRPs) continue to provide novel insights into the physics and geometry of these sources. We present the first X-ray polarimetric study of the persistent wind-fed XRP 4U 1538-52, based on five IXPE observations totaling 360 ks, conducted in March and October 2024. We detect marginally significant polarization in the combined data set in the full 2--8 keV energy band, with a polarization degree (PD) of 3.0+-1.1% and polarization angle (PA) of -18 degrees. The energy-resolved analysis shows a clear energy dependence of the polarization properties, with a remarkable ~70 degrees switch in PA between low and high energies. Similarly, the pulse phase-resolved spectro-polarimetric analysis reveals different signatures at low and high energies. At low (2--3 keV) energies, the PD ranges between ~2% and ~18%, with the PA varying between -16 and 70 degrees. At higher (4--8 keV) energies, the PD varies between ~3% and ~12%, with a drastically different PA behavior. Fitting the rotating vector model to the pulse phase dependence of the PA at the lower energies, we constrain the geometric configuration of the pulsar. The analysis favors a high spin-axis inclination of >50 which agrees with both previous pulse-phase-dependent spectral fitting of the cyclotron line region and the known high orbital inclination of the binary system. The magnetic obliquity is estimated to be 30 degrees and the spin position angle to be 19 degrees. A sharp switch in PA around 3 keV presents a particular theoretical challenge, as it is not consistent with the right-angle switch that was only seen in one other pulsar Vela X-1.


![[mdfiles/2503.13720.md|2503.13720]]
### AI Justification:
The paper discusses the geometrical configuration and magnetic characteristics of the X-ray pulsar 4U 1538-52, providing insights into the "polarization," which could indirectly relate to how "magnetic fields behave" within such astrophysical plasma environments. However, it primarily focuses on the specific behaviors of this pulsar rather than broader phenomena concerning magnetic field amplification or turbulent plasmas across various scales, making it less aligned with your specific research interests.
# (317/382) http://arxiv.org/pdf/2503.06068v2


### Rating: 4/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 40%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Gyromagnetic Angular Momentum Interconversion in Neutron Stars
**Hiroshi Funaki,Yuta Sekino,Hiroyuki Tajima,Shota Kisaka,Nobutoshi Yasutake,Mamoru Matsuo**


#mhd
### Abstract:
We propose a novel mechanism for angular momentum (AM) exchange between the crust and core of a neutron star (NS) via the gyromagnetic effect. Using extended hydrodynamics, we model the star by incorporating macroscopic AM and microscopic AM originating from neutron orbital and spin AM. We reveal that macroscopic dynamics in the crust can inform microscopic AM in the core leading to neutron spin polarization, and offer alternative scenario of (anti-)glitches. This work highlights the overlooked multi-scale AM interconversions in NS physics, paving the way for gyromagnetic astrophysics.


![[mdfiles/2503.06068.md|2503.06068]]
### AI Justification:
The paper addresses the interconversion of angular momentum in neutron stars and presents a mechanism that could relate to magnetic fields through the gyromagnetic effect, which aligns with your interest in "how magnetic fields behave, interact, and amplify." However, it primarily focuses on neutron star dynamics rather than plasma dynamics or the specific interactions of magnetic fields in the interstellar medium, making it tangentially relevant.
# (318/382) http://arxiv.org/pdf/2503.10974v1


### Rating: 3.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 35%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Forecasting the 8 April 2024 Total Solar Eclipse with Multiple Solar Photospheric Magnetograms
**Xianyu Liu,Weihao Liu,Ward B. Manchester IV,Daniel T. Welling,Gabor Toth,Tamas I. Gombosi,...**


#mhd
### Abstract:
The 8 April 2024 total solar eclipse (TSE) provides a unique opportunity to study the solar corona. This work presents our prediction of the solar corona at the time of the eclipse based on magnetohydrodynamic (MHD) modeling performed with the Alfv\{e}n Wave Solar Model-Realtime (AWSoM-R) in the Space Weather Modeling Framework, developed at the University of Michigan. We performed multiple simulations made with data input in the form of synchronic magnetograms from four sources, i.e., ADAPT-GONG, Lockheed Martin ESFAM, HipFT and NSO-NRT magnetograms. Simulations also include a higher-resolution model and a post-eclipse model incorporating newly emerged active regions. Our study fundamentally focuses on the limitations imposed by the lack of global solar observations, particularly on how these limitations affect coronal simulations. Specifically, we examine how differences among the magnetograms and the absence of observations from the east limb, due to the Suns rotation, impact the accuracy of the predicted coronal structures. We synthesized a variety of representative observables, including the white-light and extreme-ultraviolet images from each model, and compared them with observations. The synthesized observables show remarkable differences because of the distinct magnetic coronal topologies, which stem from the varied magnetic flux distributions and the gaps in observational coverage. Our findings emphasize the need for comprehensive and multi-satellite magnetic field observations to improve future solar corona predictions.


![[mdfiles/2503.10974.md|2503.10974]]
### AI Justification:
This paper is only tangentially relevant to your research interests, as its primary focus is on the solar corona and the limitations in modeling magnetic fields in that context. However, it does encompass aspects of "magnetic field dynamics" through its exploration of "magnetohydrodynamic (MHD) modeling" and the implications of magnetic observations, albeit in a solar framework rather than the interstellar medium.
# (319/382) http://arxiv.org/pdf/2504.13435v1


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A generalized equation for the critical current for a one-dimensional crossed-field gap in an orthogonal coordinate system
**Jack K. Wright,N. R. Sree Harsha,Allen L. Garner**


#mhd
### Abstract:
Recent studies have applied variational calculus, conformal mapping, and point transformations to extend the one-dimensional SCLC from planar gaps to more complicated geometries. However, introducing a magnetic field orthogonal to the diodes electric field complicates these calculations due to changes in the electron trajectory. This paper extends a recent study that applied variational calculus to determine the SCLC for a cylindrical crossed-field diode to derive an equation that is valid for any orthogonal coordinate system. We then derive equations for the SCLC for crossed-field gaps in spherical, tip-to-tip, and tip-to-plane geometries that can be solved numerically. These calculations exhibit a discontinuity at the Hull cutoff magnetic field $B_H$ corresponding to the transition to magnetic insulation as observed analytically for a planar geometry. The ratio of the crossed-field SCLC to the nonmagnetic SCLC becomes essentially independent of geometry when we fix $\delta = D/D_M > 0.6 $ , where $ D$ is the canonical gap distance accounting for geometric effects on electric potential and $D_M$ is the effective gap distance that accounts for magnetic field and geometry. The solutions for these geometries overlap as $\delta \to 1$ since the geometric corrections for electric potential and magnetic field match. This indicates the possibility of more generally accounting for the combination of geometric and magnetic effects when calculating $B_H$ and SCLC.


![[mdfiles/2504.13435.md|2504.13435]]
### AI Justification:
The paper's focus on "critical current" and "crossed-field gaps" in conjunction with magnetic effects does not directly align with your research interests in the magnetic dynamics of astrophysical plasmas, particularly regarding "magnetic field amplification" and "emergent magnetic dynamics." The exploration of magnetic fields in a confined, structured environment such as a diode under different geometries may provide some limited insights but lacks the broader astrophysical context pertinent to your work on the interstellar medium and turbulent plasmas.
# (320/382) http://arxiv.org/pdf/2503.07704v2


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### DW Cnc... a micronova with a negative superhump and a flickering spin
**M. Veresvarska,S. Scaringi,C. Littlefield,D. de Martino,C. Knigge,J. Paice,...**


#mhd
### Abstract:
Magnetic accreting white dwarfs in cataclysmic variables have been known to show bursts driven by different physical mechanisms; however, the burst occurrence is much rarer than in their non-magnetic counterparts. DW Cnc is a well-studied intermediate polar that showed a burst with a 4-magnitude amplitude in 2007. Here we report on a recent burst in DW Cnc observed by ASAS-SN that reached a peak luminosity of 6.6 $\times$ 10 $^{33}$ erg~s $^{-1}$ , another 4 mag increase from its quiescent high state level. The released energy of the burst suggests that these are micronovae, a distinctive type of burst seen in magnetic systems that may be caused by a thermonuclear runaway in the confined accretion flow. Only a handful of systems, most of them intermediate polars, have a reported micronova bursts. We also report on the reappearance of the negative superhump of DW~Cnc as shown by TESS and OPTICAM data after the system emerges from its low state and immediately before the burst. We further report on a new phenomenon, where the spin signal turns `on` and `off` on the precession period associated with the negative superhump, which may indicate pole flipping. The new classification of DW Cnc as a micronova as well as the spin variability show the importance of both monitoring known micronova systems and systematic searches for more similar bursts, to limit reliance on serendipitous discoveries.


![[mdfiles/2503.07704.md|2503.07704]]
### AI Justification:
The paper's relevance to your interests is limited as it primarily focuses on bursts in magnetic accreting white dwarfs and their relationship to micronovae, which does not directly address broader themes of magnetic field amplification or the interactions of magnetic and thermal forces within astrophysical plasmas. While it mentions magnetic systems and possibly intriguing magnetic dynamics, it lacks a focus on the scale-dependent structuring and multi-scale dynamics of magnetic fields in plasma environments that your research explicitly targets.
# (321/382) http://arxiv.org/pdf/2504.05854v1


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### 50 Dra... Am-type twins with additional variability in a non-eclipsing system
**M. Skarka,J. Liptak,E. Niemczura,Z. Mikulasek,M. Cabezas,M. Vitkova,...**


#mhd
### Abstract:
The interplay between radiative diffusion, rotation, convection, and magnetism in metallic-line chemically peculiar stars is still not fully understood. Recently, evidence has emerged that these effects can work together. Our goal is to study the bright binary system 50 Dra, describe its orbit and components, and study additional variability. We conducted our analysis using TESS short-cadence data and new high-resolution spectroscopic observations. We disentangled the spectra using Korel and performed spectral synthesis with Atlas9 and Synthe codes. The system was modelled using Korel and Phoebe2.4. We also employed SED fitting in Ariadne and isochrone fitting using Param1.5 codes. Our findings indicate that the non-eclipsing system (with an inclination of 49.9(8) deg) 50 Dra, displaying ellipsoidal brightness variations, consists of two nearly equal A-type stars with masses of $M_{1}=2.08(8)$ and $M_{2}=1.97(8)$ M $_{\odot}$ and temperatures of 9800(100) and 9200(200) K, respectively. Our analysis also suggests that the system, with an orbital period of $P_{\rm orb}=4.117719(2)$ days, is tidally relaxed with a circular orbit and synchronous rotation of the components. Furthermore, we discovered that both stars are metallic-line Am chemically peculiar stars with an underabundance of Sc and an overabundance of iron-peak and rare-earth elements. We identified additional variations with slightly higher frequency than the rotational frequency of the components that we interpret as prograde g-mode pulsations. The system 50 Dra exhibits numerous exciting phenomena that co-exist together and may have an impact on our understanding of chemical peculiarity and pulsations.


![[mdfiles/2504.05854.md|2504.05854]]
### AI Justification:
The paper titled "50 Dra... Am-type twins with additional variability in a non-eclipsing system" explores the interplay between magnetism and various astrophysical factors, which can provide insights into the behavior and dynamics of magnetic fields in stellar contexts. However, it primarily focuses on binary systems and chemical peculiarities rather than the magnetic dynamics of plasmas in the interstellar medium, making it less relevant to my specific research interest in magnetic field amplification and emergent dynamics in turbulent plasmas.
# (322/382) http://arxiv.org/pdf/2504.03838v1


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### High-energy gamma-ray emission from memory-burdened primordial black holes
**Marco Chianese**


#mhd
### Abstract:
Theoretical studies on the memory-burden effect suggest that Primordial Black Holes (PBHs) with masses smaller than $10^{15}$ grams may be viable dark matter candidates and, consequently, be potential sources of high-energy particles in the present Universe. In this paper, we investigate the evaporation of memory-burdened PBHs into high-energy gamma-rays. Differently from previous analyses, we account for the attenuation of gamma-rays caused by their interaction with background radiation at energies above $10^5~{\rm GeV}$ , as well as the secondary emission from the electromagnetic cascades generated during the propagation through extragalactic space. Performing a likelihood analysis with current gamma-ray data, we place new constraints on the parameter space of memory-burdened PBHs. Our results show that ultra-high-energy diffuse gamma-ray observations set more restrictive bounds than high-energy neutrino data, particularly in scenarios with a strong memory-burden suppression of the PBH evaporation.


![[mdfiles/2504.03838.md|2504.03838]]
### AI Justification:
This paper discusses high-energy gamma-ray emission related to primordial black holes, which aligns somewhat with my interests in theoretical astrophysics but lacks a direct focus on magnetic dynamics of plasmas, specifically the mechanisms of magnetic field interactions and amplification within plasma environments. While the study analyzes interactions with background radiation, it does not address the key themes of magnetic field behavior, force interactions, or emergent magnetic dynamics that are central to my research focus on plasmas in the interstellar medium.
# (323/382) http://arxiv.org/pdf/2504.02092v1


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Three-dimensional non-LTE radiative transfer effects in Fe I lines IV. Line formation at high spatial resolution
**R. Holzreuter,H. N. Smitha,S. K. Solanki**


#mhd
### Abstract:
In the first three papers of this series, we investigated the formation of photospheric neutral iron lines in different atmospheres ranging from idealised flux tube models to complex three-dimensional magnetohydrodynamic (3D MHD) simulations. The overarching goal was to understand the role of Non-Local Thermodynamic Equilibrium (NLTE) and horizontal radiative transfer (RT) effects in the formation of these lines. In the present paper, we extend this investigation using a high resolution MHD simulation, with a grid spacing much smaller than the currently resolvable scales by telescopes. We aim to understand whether the horizontal RT effects imposes an intrinsic limit on the small scale structures that can be observed by telescopes, by spatially smearing out these structures in the solar atmosphere. We synthesize the Stokes profiles of two iron line pairs, one at 525 nm and other at 630 nm in 3-D NLTE. We compare our results with those in previous papers and check the impact of horizontal transfer on the quality of the images. Our results with the high resolution simulations align with those inferred from lower resolution simulations in the previous papers of this series. The spatial smearing due to horizontal RT, although present, is quite small. The degradation caused by the point spread function of a telescope is much stronger. In the photospheric layers, we do not see an image degradation caused by horizontal RT that is large enough to smear out the small scale structures in the simulation box. The current generation telescopes with spatial resolutions smaller than the horizontal photon mean free path should in principle be able to observe the small scale structures, at least in the photosphere.


![[mdfiles/2504.02092.md|2504.02092]]
### AI Justification:
This paper primarily focuses on non-LTE effects and radiative transfer in the context of photospheric iron lines, utilizing high-resolution MHD simulations, but it does not align closely with your interests in the magnetic dynamics of plasmas in interstellar environments. Although it involves MHD simulations, the emphasis on horizontal radiative transfer and its effects on observational limitations in the solar atmosphere diverges from your specific research focus on magnetic field amplification and turbulent plasma dynamics.
# (324/382) http://arxiv.org/pdf/2503.20858v1


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Die Hard... The On-Off-Cycle of Galaxies on the Star Formation Main Sequence
**Silvio Fortune,Rhea-Silvia Remus,Lucas C. Kimmig,Andreas Burkert,Klaus Dolag**


#mhd
### Abstract:
Our picture of galaxy evolution currently assumes that galaxies spend their life on the star formation main sequence until they may eventually be quenched. However, recent observations show indications that the full picture might be more complicated. We reveal how the star formation rates of galaxies evolve, possible causes and imprints of different evolution scenarios on galactic features. We follow the evolution of central galaxies in the highest-resolution box of the Magneticum Pathfinder cosmological hydrodynamical simulations and classify their evolution scenarios with respect to the star formation main sequence. We find that a major fraction of the galaxies undergoes long-term cycles of quenching and rejuvenation on Gyr timescales. This expands the framework of galaxy evolution from a secular evolution to a sequence of multiple active and passive phases. Only 14% of field galaxies on the star formation main sequence at z~0 actually evolved along the scaling relation, while the bulk of star forming galaxies in the local universe have undergone cycles of quenching and rejuvenation. In this work we describe the statistics of these galaxy evolution modes and how this impacts their stellar masses, ages and metallicities today. Galaxies with rejuvenation cycles can be distinguished well from main-sequence-evolved galaxies in their features at z~0. We further explore possible explanations and find that the geometry of gas accretion at the halo outskirts shows a strong correlation with the star formation rate evolution, while the density parameter as a tracer of environment shows no significant correlation. A derivation of star formation rates from gas accretion with simple assumptions only works reasonably well in the high-redshift universe where accreted gas gets quickly converted into stars.


![[mdfiles/2503.20858.md|2503.20858]]
### AI Justification:
This paper primarily focuses on galaxy evolution and star formation rates, which does not align directly with your strong interest in "Magnetic Field Amplification" and "Emergent Magnetic Dynamics in Turbulent Plasmas." While it touches on aspects of hydrodynamical simulations that could potentially relate to magnetic field interactions, the central themes of cycling star formation and quenching do not provide significant insights into the multi-scale dynamics of magnetic fields within plasmas, as stated in your prompt.
# (325/382) http://arxiv.org/pdf/2503.12569v1


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Dark Spin-2 Field Solitons as a Source of Electromagnetic Radiation
**Enrico D. Schiappacasse**


#mhd
### Abstract:
Spin- $s$ light dark boson particles can exhibit wave-like behavior, capable of forming long-lived, coherent, spatially localized structures known as solitons. This work considers the possibility that a light spin-2 particle might be part of or all the dark matter content of the Universe, which could result in a significant fraction of solitons existing today in galactic halos. If these dark matter particles interact with electromagnetism through dimension-6 operators, the solitons may experience parametric resonance of photons triggered by the surrounding electromagnetic field. We explore the feasibility and key characteristics of this electromagnetic radiation, as well as the potential for detection through soliton mergers using ground-based facilities.


![[mdfiles/2503.12569.md|2503.12569]]
### AI Justification:
While the paper investigates the behavior of dark boson particles and their potential interactions with electromagnetic fields, it does not align closely with your research interests in the magnetic dynamics of plasmas in the interstellar medium. The focus on "solitons" and their interaction with electromagnetic radiation is somewhat tangential, as it primarily examines dark matter phenomena rather than the amplification and structuring of magnetic fields in astrophysical plasmas.
# (326/382) http://arxiv.org/pdf/2503.08779v1


### Rating: 3/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 30%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Seeding Cores... A Pathway for Nuclear Star Clusters from Bound Star Clusters in the First Billion Years
**Fred Angelo Batan Garcia,Massimo Ricotti,Kazuyuki Sugimura**


#mhd
### Abstract:
We model the formation of star clusters in a dwarf galaxy progenitor during the first 700 Myr of cosmic history using a cosmological radiation-hydrodynamic simulation with a realistic sub-grid star formation efficiency (SFE) model, derived from AU-scale radiation-MHD simulations of molecular clouds with varying mass, density, and metallicity. Using this model for cloud-scale SFEs, the galaxy forms stars stochastically, assembling most of its $10^6~{\rm M_\odot} $ in stars by redshift $ z=8$ through two star-forming bursts (SFBs), each lasting $\sim10~{\rm Myr}$ , separated by $80~{\rm Myr}$ of quiescence. Clouds reach SFEs up to $80\%$ during the first SFB, forming bound star clusters (densities $\sim10^{2-4} ~{\rm M_\odot\...pc^{-2}}$ , radii $\lesssim 3~{\rm pc}$ ) resembling those observed by the James Webb Space Telescope (JWST) in strongly lensed galaxies. Star clusters follow a flat power-law mass function with slope $\Gamma \sim -0.4$ . The most massive star clusters ( $10^{4-5} ~{\rm M_\odot}$ ) grow through mergers and have metallicity spreads of $0.05 - 0.1$ dex that roughly scale with mass. The second SFB forms loosely bound star clusters with higher metallicities... $-1.95 < \log(Z/{\rm Z_\odot}) < -1.50 $ at lower SFEs ( $ 2 - 20\% $ ). At $ z \sim 8.7$ , a nuclear star cluster (NSC) is seeded, growing $83\%$ of its mass ( $ 2.4 \times 10^5 ~{\rm M_\odot}$ , $20\%$ of the galaxys stellar mass) through mergers with pre-existing clusters and the rest through in-situ star formation. The early formation of NSCs has interesting implications for seeding supermassive black holes and the population of `little red dots` recently discovered by JWST at $z \gtrsim 5$ .


![[mdfiles/2503.08779.md|2503.08779]]
### AI Justification:
This paper has limited relevance to your research interests, as it primarily focuses on star cluster formation and their evolution in dwarf galaxies, rather than the magnetic dynamics of plasmas in the interstellar medium. While it touches on "molecular clouds" and uses "radiation-MHD simulations," it does not directly address key themes such as "magnetic field amplification" or the interactions between forces shaping magnetic dynamics, which are central to your work.
# (327/382) http://arxiv.org/pdf/2502.00971v2


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### K-dwarf Radius Inflation and a 10-Gyr Spin-down Clock Unveiled through Asteroseismology of HD 219134 from the Keck Planet Finder
**Yaguang Li,Daniel Huber,J. M. Joel Ong,Jennifer van Saders,R. R. Costa,Jens Reersted Larsen,...**


#mhd
### Abstract:
We present the first asteroseismic analysis of the K3\,V planet host HD~219134, based on four consecutive nights of radial velocities collected with the Keck Planet Finder. We applied Gold deconvolution to the power spectrum to disentangle modes from sidelobes in the spectral window, and extracted 25 mode frequencies with spherical degrees $0\leq\ell\leq3$ . We derive the fundamental properties using five different evolutionary-modeling pipelines and report a mass of 0.763 $\pm$ 0.020 (stat) $\pm$ 0.007 (sys) M $_\odot$ , a radius of 0.748 $\pm$ 0.007 (stat) $\pm$ 0.002 (sys) R $_\odot$ , and an age of 10.151 $\pm$ 1.520 (stat) $\pm$ 0.810 (sys) Gyr. Compared to the interferometric radius 0.783 $\pm$ 0.005~R $_\odot$ , the asteroseismic radius is 4\% smaller at the 4- $\sigma$ level -- a discrepancy not easily explained by known interferometric systematics, modeling assumptions on atmospheric boundary conditions and mixing lengths, magnetic fields, or tidal heating. HD~219134 is the first main-sequence star cooler than 5000~K with an asteroseismic age estimate and will serve as a critical calibration point for stellar spin-down relations. We show that existing calibrated prescriptions for angular momentum loss, incorporating weakened magnetic braking with asteroseismically constrained stellar parameters, accurately reproduce the observed rotation period. Additionally, we revised the masses and radii of the super-Earths in the system, which support their having Earth-like compositions. Finally, we confirm that the oscillation amplitude in radial velocity scales as $(L/M)^{1.5}$ in K dwarfs, in contrast to the $(L/M)^{0.7}$ relation observed in G dwarfs. These findings provide significant insights into the structure and angular momentum loss of K-type stars.


![[mdfiles/2502.00971.md|2502.00971]]
### AI Justification:
This paper is low relevance to your interests in theoretical astrophysics and plasma physics, primarily focusing on asteroseismology and stellar properties rather than the magnetic dynamics of plasmas. Phrases like "discrepancy ... not easily explained by ... magnetic fields" mention magnetic fields but do not align with your focus on their amplification, interactions, or emergent behavior in plasma environments.
# (328/382) http://arxiv.org/pdf/2504.20169v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Perfectly Matched Layers and Characteristic Boundaries in Lattice Boltzmann... Accuracy vs Cost
**Friedemann Klass,Alessandro Gabbana,Andreas Bartel**


#mhd
### Abstract:
Artificial boundary conditions (BCs) play a ubiquitous role in numerical simulations of transport phenomena in several diverse fields, such as fluid dynamics, electromagnetism, acoustics, geophysics, and many more. They are essential for accurately capturing the behavior of physical systems whenever the simulation domain is truncated for computational efficiency purposes. Ideally, an artificial BC would allow relevant information to enter or leave the computational domain without introducing artifacts or unphysical effects. Boundary conditions designed to control spurious wave reflections are referred to as nonreflective boundary conditions (NRBCs). Another approach is given by the perfectly matched layers (PMLs), in which the computational domain is extended with multiple dampening layers, where outgoing waves are absorbed exponentially in time. In this work, the definition of PML is revised in the context of the lattice Boltzmann method. The impact of adopting different types of BCs at the edge of the dampening zone is evaluated and compared, in terms of both accuracy and computational costs. It is shown that for sufficiently large buffer zones, PMLs allow stable and accurate simulations even when using a simple zeroth-order extrapolation BC. Moreover, employing PMLs in combination with NRBCs potentially offers significant gains in accuracy at a modest computational overhead, provided the parameters of the BC are properly tuned to match the properties of the underlying fluid flow.


![[mdfiles/2504.20169.md|2504.20169]]
### AI Justification:
The paper focuses on artificial boundary conditions in numerical simulations, particularly within fluid dynamics and related fields, and while it mentions electromagnetism—which is relevant to plasma physics—there is a lack of direct connection to the specific aspects of magnetic field dynamics and amplification in astrophysical plasmas as outlined in my research interests. It does not address topics such as magnetic field interactions or dynamics within turbulent plasma environments, thus providing minimal insight related to my work.
# (329/382) http://arxiv.org/pdf/2504.10128v2


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Probing Binary Lens Caustics with Gravitational Waves... A Uniform Approximation Approach
**Anna Moreso Serra,Oleg Bulashenko**


#mhd
### Abstract:
We present a new framework for modeling gravitational wave diffraction near fold caustics using the Uniform Approximation (UA), focusing on binary mass lenses - axially asymmetric systems with complex caustic structures. Full-wave methods based on the Kirchhoff integral become impractical in this regime due to highly oscillatory integrands. The UA provides a robust and accurate description of the wave field near folds, resolving the breakdown of Geometrical Optics at caustics and improving upon Transitional Asymptotics - based on Airy function approximations - which lack global validity. Central to our approach is the concept of the caustic width, $d_c$ , a characteristic length scale defining the region where diffraction significantly alters wave propagation. We find that $d_c$ scales universally with the gravitational wavelength as ~ $ \lambda^{2/3}$ and inversely with the redshifted lens mass as ~ $ M_{Lz}^{-2/3}$ . The wave amplification near the fold grows as ~ $ d_c^{-1/4}$ , substantially enhancing the signal and potentially playing a key role in the detection of gravitational waves lensed near caustics. Notably, for lens masses below the galactic scale, the caustic width for gravitational waves is not negligible compared to the Einstein radius - as it is in electromagnetic lensing - making the UA essential for accurately capturing wave effects.


![[mdfiles/2504.10128.md|2504.10128]]
### AI Justification:
This paper focuses on gravitational wave diffraction and amplification through the lensing effects of binary mass lenses, which is largely outside your primary research interest in plasma physics and magnetic field dynamics. While it does involve wave behavior and dynamics, the emphasis on gravitational rather than electromagnetic fields and the specifics of lensing mechanisms do not align with your focus on the interactions of magnetic fields in astrophysical plasmas.
# (330/382) http://arxiv.org/pdf/2504.16825v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Symbiotic stars in the era of modern ground- and space-based surveys
**Jaroslav Merc**


#mhd
### Abstract:
Symbiotic stars, interacting binaries composed of a cool giant and a hot compact companion, exhibit complex variability across the electromagnetic spectrum. Over the past decades, large-scale photometric and spectroscopic surveys from ground- and space-based observatories have significantly advanced their discovery and characterization. These datasets have transformed the search for new symbiotic candidates, providing extensive time-domain information crucial for their classification and analysis. This review highlights recent observational results that have expanded the known population of symbiotic stars, refined classification criteria, and enhanced our understanding of their variability. Despite these advances, fundamental questions remain regarding their long-term evolution, mass transfer and accretion processes, or their potential role as progenitors of Type Ia supernovae. With ongoing and upcoming surveys, the coming years promise new discoveries and a more comprehensive picture of these intriguing interacting systems.


![[mdfiles/2504.16825.md|2504.16825]]
### AI Justification:
The paper discusses symbiotic stars and their variability, which does not directly address the magnetic dynamics of plasmas in the interstellar medium, particularly in terms of magnetic field amplification or force interactions shaping magnetic dynamics. Therefore, while it touches on complex interactions within stellar systems, it lacks relevance to my focus on theoretical models and simulations related to the behavior of magnetic fields in astrophysical plasmas.
# (331/382) http://arxiv.org/pdf/2504.16218v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Lensing of hot spots in Kerr spacetime... An empirical relation for black hole spin estimation
**A. I. Yfantis,D. C. M. Palumbo,M. Moscibrodzka**


#mhd
### Abstract:
Sagittarius A* (Sgr A*) exhibits frequent flaring activity across the electromagnetic spectrum, often associated with a localized region of strong emission, known as a hot spot. We aim to establish an empirical relationship linking key parameters of this phenomenon -- emission radius, inclination, and black hole spin -- to the observed angle difference between the primary and secondary image ( $\Delta PA$ ) that an interferometric array could resolve. Using the numerical radiative transfer code IPOLE, we generated a library of more than 900 models with varying system parameters and computed the position angle difference on the sky between the primary and secondary images of the hot spot. We find that the average $\Delta PA$ over a full period is insensitive to inclination. This result significantly simplifies potential spin measurements which might otherwise have large dependencies on inclination. Additionally, we derive a relation connecting spin to $\Delta PA$ , given the period and emission radius of the hot spot, with an accuracy of less than $5^\circ$ in most cases. Finally, we present a mock observation to showcase the potential of this relation for spin inference. Our results provide a novel approach for black hole spin measurements using high-resolution observations, such as future movies of Sgr A* obtained with the Event Horizon Telescope, next-generation Event Horizon Telescope, and Black Hole Explorer.


![[mdfiles/2504.16218.md|2504.16218]]
### AI Justification:
The paper primarily focuses on black hole spin estimation through observational techniques related to Sagittarius A*, which diverges from your central interest in the "magnetic dynamics of plasmas in the interstellar medium." Although there may be some indirect implications for magnetic fields in relation to hot spots, the methods and core themes do not align closely with your emphasis on "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas."
# (332/382) http://arxiv.org/pdf/2504.14616v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The galaxy bias profile of cosmic voids
**Antonio D. Montero-Dorta,Andres Balaguera-Antolinez,Ignacio G. Alfaro,Andres N. Ruiz,Ravi K. Sheth,Facundo Rodriguez,...**


#mhd
### Abstract:
Cosmic voids are underdense regions within the large-scale structure of the Universe, spanning a wide range of physical scales - from a few megaparsecs (Mpc) to the largest observable structures. Their distinctive properties make them valuable cosmological probes and unique laboratories for galaxy formation studies. A key aspect to investigate in this context is the galaxy bias, $b$ , within voids - that is, how galaxies in these underdense regions trace the underlying dark-matter density field. We want to measure the dependence of the large-scale galaxy bias on the distance to the void center, and to evaluate whether this bias profile varies with the void properties and identification procedure. We apply a void identification scheme based on spherical overdensities to galaxy data from the IllustrisTNG magnetohydrodynamical simulation. For the clustering measurement, we use an object-by-object estimate of large-scale galaxy bias, which offers significant advantages over the standard method based on ratios of correlation functions or power spectra. We find that the average large-scale bias of galaxies inside voids tends to increase with void-centric distance when normalized by the void radius. For the entire galaxy population within voids, the average bias rises with the density of the surrounding environment and, consequently, decreases with increasing void size. Due to this environmental dependence, the average galaxy bias inside S-type voids - embedded in large-scale overdense regions - is significantly higher ( $\langle b\rangle_{\rm in} > 0$ ) at all distances compared to R-type voids, which are surrounded by underdense regions ( $\langle b\rangle_{\rm in} < 0$ ). The bias profile for S-type voids is also slightly steeper. Since both types of voids host halo populations of similar mass, the measured difference in bias can be interpreted as a secondary bias effect.


![[mdfiles/2504.14616.md|2504.14616]]
### AI Justification:
This paper's focus on "cosmic voids" and the "galaxy bias profile" offers little direct relevance to my interests in "magnetic dynamics of plasmas" and "magnetic field amplification" within the interstellar medium. While the abstract mentions the "voids" and their impact on large-scale structures, it does not explore "how magnetic fields behave, interact, and amplify" across the scales I am interested in.
# (333/382) http://arxiv.org/pdf/2504.14146v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Binary Stars Approaching Supermassive Black Holes... Hydrodynamics of Stellar Collisions, Mass Fallback and Partial TDEs
**Fangyuan Yu,Dong Lai**


#mhd
### Abstract:
When binaries are injected into low-angular-momentum orbits around a central supermassive black hole (SMBH), various outcomes can occur, including binary tidal breakup, double stellar disruptions and stellar collision. We use hydrodynamical simulations to study stellar collisions triggered by binary-SMBH encounters, examining both head-on and grazing collisions in deep ( $\beta_b=5$ ) and gentle ( $\beta_b=0.6$ ) encounters, where $\beta_b$ is the ratio of the binary tidal disruption radius to the binary pericenter distance to the SMBH. Head-on collisions consistently result in appreciable mass loss ( $\sim 5\%$ ) and a single merger remnant. Grazing collisions in deep encounters typically leave two strongly disturbed stars with comparable mass loss, while in gentle encounters, multiple collisions eventually produce a single remnant with minimal mass loss ( $\lesssim 1\%$ ). All merger remnants feature extended envelopes, making them susceptible to partial tidal disruptions when they return to the SMBH. The morphology and orbital energy distribution of collision-induced debris differ significantly from those of tidal disruption event (TDE) debris of single stars. Approximately half of the collision-generated debris falls back onto the SMBH, exhibiting a distinct time evolution of the fallback rate. We suggest that such mass loss and fallback can generate electromagnetic flares that mimic weak TDEs.


![[mdfiles/2504.14146.md|2504.14146]]
### AI Justification:
The paper's primary focus on hydrodynamical simulations of stellar collisions near supermassive black holes, while interesting, does not align well with my research interests in magnetic dynamics of plasmas. My work revolves around understanding "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas," neither of which are addressed in the context of stellar collisions and tidal disruptions presented in this paper.
# (334/382) http://arxiv.org/pdf/2504.14079v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Super-exponential Amplification of Wavepacket Propagation in Traveling Wave Tubes
**Kasra Rouhi,Filippo Capolino,Alexander Figotin**


#mhd
### Abstract:
We analyze wavepacket propagation in traveling wave tubes (TWTs) analytically and numerically. TWT design in essence comprises a pencil-like electron beam in vacuum interacting with an electromagnetic wave guided by a slow-wave structure (SWS). In our study, the electron beam is represented by a one-dimensional electron flow and the SWS is represented by an equivalent transmission line model. The analytical considerations are based on the Lagrangian field theory for TWTs. Mathematical analysis of wavepacket propagation in one-dimensional space is based on the relevant Euler-Lagrange equations which are second-order differential equations in both time and space. Wavepacket propagation analysis is not simple and we develop a numerically efficient algorithm to perform the analysis efficiently. In particular, when the initial pulse has a Gaussian shape at the input port, it acquires non-Gaussian features as it propagates through the TWT. These features include... (i) super-exponential (faster than exponential) amplification, (ii) shift of the pulse frequency spectrum toward higher frequencies, and (iii) change in the shape of the pulse that becomes particularly pronounced when the pulse frequency band contains a transitional point from stability to instability.


![[mdfiles/2504.14079.md|2504.14079]]
### AI Justification:
This paper's focus on wavepacket propagation and amplification in traveling wave tubes introduces concepts of "super-exponential amplification" that could offer insights into the mechanisms of magnetic field amplification relevant to dynamo processes in astrophysical plasmas. However, the primary context of TWTs and the dynamics of non-Gaussian features do not seem to align closely with my specific interests in "magnetic dynamics of plasmas in the interstellar medium," and the lack of explicit reference to magnetic or plasma interactions limits its value for my research.
# (335/382) http://arxiv.org/pdf/2504.13357v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Geometric and Thermodynamic Properties of Frolov Black Holes with Topological Defects
**Faizuddin Ahmed,Ahmad Al-Badawi,Izzet Sakalli**


#mhd
### Abstract:
We investigated a modified Frolov black hole (BH) model that incorporates both a global monopole (GM) and a cosmic string (CS) to explore the interplay between non-singular BH regularization and topological defect effects. In our study, we derived a spacetime metric characterized by a regulated core through a length scale parameter $\alpha$ and introduced additional modifications via the GM parameter $\eta$ and the CS parameter $a$ , which collectively alter the horizon structure and causal geometry of the BH. We analyzed the thermodynamic properties by deriving expressions for the mass function, Hawking temperature, and entropy, and found that the inclusion of GM and CS significantly deviates the BH entropy from the conventional Bekenstein-Hawking area law, while numerical investigations showed that the shadow radius exhibits contrasting behaviors... the Frolov parameters tend to reduce the shadow size whereas the topological defects enhance it. Furthermore, we examined the dynamics of scalar and electromagnetic perturbations by solving the massless Klein-Gordon equation in the BH background and computed the quasinormal modes (QNMs) using the WKB approximation, which confirmed the BHs stability and revealed that the oscillation frequencies and damping rates are strongly dependent on the parameters $\alpha$ , $q$ , $\eta$ , and $a$ . Our results suggest that the distinct observational signatures arising from this composite BH model may provide a promising avenue for testing modified gravity theories in the strong-field regime.


![[mdfiles/2504.13357.md|2504.13357]]
### AI Justification:
The paper discusses modifications to black hole models through topological defects, which does not directly align with my interest in magnetic dynamics of plasmas in the interstellar medium. There is minimal focus on magnetic field behavior, amplification mechanisms, or the interactions shaping magnetic dynamics that are central to my research interests.
# (336/382) http://arxiv.org/pdf/2504.12384v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### WINTER on S250206dm... A near-infrared search for an electromagnetic counterpart
**Danielle Frostig,Viraj R. Karambelkar,Robert D. Stein,Nathan P. Lourie,Mansi M. Kasliwal,Robert A. Simcoe,...**


#mhd
### Abstract:
We present near-infrared follow-up observations of the International Gravitational Wave Network (IGWN) event S250206dm with the Wide-Field Infrared Transient Explorer (WINTER). WINTER is a near-infrared time-domain survey designed for electromagnetic follow-up of gravitational-wave sources localized to $\leq$ 300 deg $^{2}$ . The instruments wide field of view (1.2 deg $^2$ ), dedicated 1-m robotic telescope, and near-infrared coverage (0.9-1.7 microns) are optimized for searching for kilonovae, which are expected to exhibit a relatively long-lived near-infrared component. S250206dm is the only neutron star merger in the fourth observing run (to date) localized to $\leq$ 300 deg $^{2}$ with a False Alarm Rate below one per year. It has a $55\%$ probability of being a neutron star-black hole (NSBH) merger and a $37\%$ probability of being a binary neutron star (BNS) merger, with a $50\%$ credible region spanning 38 deg $^2$ , an estimated distance of 373 Mpc, and an overall false alarm rate of approximately one in 25 years. WINTER covered $43\%$ of the probability area at least once and $35\%$ at least three times. Through automated and human candidate vetting, all transient candidates found in WINTER coverage were rejected as kilonova candidates. Unsurprisingly, given the large estimated distance of 373 Mpc, the WINTER upper limits do not constrain kilonova models. This study highlights the promise of systematic infrared searches and the need for future wider and deeper infrared surveys.


![[mdfiles/2504.12384.md|2504.12384]]
### AI Justification:
This paper is primarily focused on near-infrared observations and follow-up techniques related to gravitational-wave events, specifically the detection of kilonovae, which does not align closely with my interests in the magnetic dynamics of plasmas in the interstellar medium. While it does touch upon neutron star mergers, which may involve complex astrophysical processes, it lacks direct relevance to the exploration of magnetic field amplification or the interaction between magnetic forces and plasma dynamics that are central to my research focus.
# (337/382) http://arxiv.org/pdf/2504.11951v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Pulsatile Magnetized $Cu$ - $Al_{2}O_{3}$ /Casson Blood Flow Through an Elliptical Stenotic Artery for Drug Delivery Applications
**Nimra Muqaddass,Alessandra Jannelli,Francesco Oliveri**


#mhd
### Abstract:
Among cardiovascular diseases, atherosclerosis is a primary cause of stenosis, involving the accumulation of plaques in the inner lining of an artery. Inspired by drug delivery applications, the proposed study aims to examine the numerical modeling of a two-dimensional, axisymmetric, and time-dependent hybrid nanofluid composed of copper $(Cu)$ , alumina $(Al_{2}O_{3})$ nanoparticles, and blood as base fluid. Blood, modeled by the non-Newtonian Casson model, flows through an elliptical stenotic artery. The pulsatile nature of the pressure gradient and magnetic field impact with the Hall current parameter are also taken into account in this study. A finite difference technique, forward in time and central in space (FTCS), is deployed to numerically discretize the transformed dimensionless model using MATLAB. Comprehensive visualization of the effects of hemodynamic, geometric, and nanoscale parameters on transport characteristics, and extensive graphical results for blood flow characteristics are provided. A comparison is made among blood, regular nanofluid, and hybrid nanofluid to analyze their properties in relation to fluid flow and heat transfer. An augmentation in the non-Newtonian parameter results in an amplification of velocity and in a reduction of the temperature profile. Incorporating $Cu$ and $Al_2O_3$ nanoparticles into the fluid results in a decrease of velocity and an increase of temperature. These findings possess significant practical implications for applications where efficient heat transfer is essential, such as in drug delivery systems and the thermal management of biomedical devices. However, the observed reduction in velocity may necessitate modifications to flow conditions to ensure optimal operational performance in these contexts.


![[mdfiles/2504.11951.md|2504.11951]]
### AI Justification:
This paper appears to be low relevance to your research focus in theoretical astrophysics and plasma physics as it primarily discusses the dynamics of blood flow through a stenotic artery and does not delve into the amplification or interactions of magnetic fields in astrophysical plasmas. The abstract mentions "pulsatile nature of the pressure gradient and magnetic field impact," but it does not address magnetic field amplification mechanisms or interactions in plasma environments, which are central to your research interests in magnetic dynamics on various scales.
# (338/382) http://arxiv.org/pdf/2504.10963v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Modeling liquid-mediated interactions for close-to-substrate magnetic microparticle transport in dynamic magnetic field landscapes
**Markus Gusenbauer,Rico Huhnstock,Alexander Kovacs,Harald Oezelt,Arno Ehresmann,Thomas Schrefl**


#mhd
### Abstract:
Understanding the on-chip motion of magnetic particles in a microfluidic environment is key to realizing magnetic particle-based Lab-on-a-chip systems for medical diagnostics. In this work, a simulation model is established to quantify the trajectory of a single particle moving close to a polymer surface in a quiescent liquid. The simulations include hydrodynamic, magnetostatic, and Derjaguin-Landau-Verwey-Overbeek (DLVO) interactions. They are applied to particle motion driven by a dynamically changing magnetic field landscape created by engineered parallel-stripe magnetic domains superposed by a homogeneous, time-varying external magnetic field. The simulation model is adapted to experiments in terms of fluid-particle interactions with the magnetic field landscape approximated by analytic equations under the assumption of surface charges. Varying simulation parameters, we especially clarify the impact of liquid-mediated DLVO interactions, which are essential for diagnostic applications, on the 3D trajectory of the particle. A comparison to experimental results validates our simulation approach.


![[mdfiles/2504.10963.md|2504.10963]]
### AI Justification:
The paper focuses on "magnetic particle-based Lab-on-a-chip systems," which, while relevant to practical applications of magnetic dynamics, deviates from your primary interest in the theoretical aspects of "magnetic field amplification" and "interactions between magnetic, gravitational, and thermal forces" in astrophysical contexts. Although it does touch upon "dynamically changing magnetic field landscapes," the emphasis on microfluidic environments and particle transport does not align well with your focus on the behavior and interaction of magnetic fields in the interstellar medium and turbulent plasmas.
# (339/382) http://arxiv.org/pdf/2504.10398v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### How well can we unravel the accreted constituents of the Milky Way stellar halo? A test on cosmological hydrodynamical simulations
**Guillaume F. Thomas,Giuseppina Battaglia,Robert J. J. Grand,Amanda Aguiar Alvarez**


#mhd
### Abstract:
Context. One of the primary goals of Galactic Archaeology is to reconstruct the Milky Ways accretion history. To achieve this, significant efforts have been dedicated to identifying signatures of past accretion events. In particular, the study of integrals-of-motion (IoM) space has proven to be highly insightful for uncovering these ancient mergers and understanding their impact on the Galaxys evolution. Aims. This paper evaluates the effectiveness of a state-of-the-art method for detecting debris from accreted galaxies, by testing it on four Milky Way-like galaxies from the Auriga suite of cosmological magneto-hydrodynamical simulations. Methods. We employ the innovative method from L\`ovdal et al. (2022) to identify substructures in the integrals-of-motion space within the local stellar halos of the four simulated galaxies. This approach enables us to evaluate the methods performance by comparing the properties of the identified clusters with the known populations of accreted galaxies in the simulations. Additionally, we investigate whether incorporating chemical abundances and stellar age information can help to link distinct structures originating from the same accretion event. Results. This method is very effective in detecting debris from accretion events that occur less than 6-7 Gyr ago but struggles to detect most of the debris from older accretion. Furthermore, most of the detected structures suffer from significant contamination by in-situ stars. Our results also show that the method may also generate artificial detections. Conclusions. Our work show that the Milky Ways accretion history remains uncertain, and question the reality of some detected structures in the Solar vicinity.


![[mdfiles/2504.10398.md|2504.10398]]
### AI Justification:
This paper focuses on the methods used to identify substructures related to past accretion events in the context of the Milky Way's stellar halo using cosmological magneto-hydrodynamical simulations. While it touches on the dynamics of stellar populations, the lack of emphasis on magnetic fields and their amplification or dynamics within plasmas makes it less relevant to your specific interests in the magnetic dynamics of plasmas in the interstellar medium.
# (340/382) http://arxiv.org/pdf/2504.10680v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Affordable, manageable, practical, and scalable (AMPS) high-yield and high-gain inertial fusion
**Andrew Alexander,Laura Robin Benedetti,Indrani Bhattacharyya,Jared Bowen,June Cabatu,Virgil Cacdac,...**


#mhd
### Abstract:
High-yield inertial fusion offers a transformative path to affordable clean firm power and advanced defense capabilities. Recent milestones at large facilities, particularly the National Ignition Facility (NIF), have demonstrated the feasibility of ignition but highlight the need for approaches that can deliver large amounts of energy to fusion targets at much higher efficiency and lower cost. We propose that pulser-driven inertial fusion energy (IFE), which uses high-current pulsed-power technology to compress targets to thermonuclear conditions, can achieve this goal. In this paper, we detail the physics basis for pulser IFE, focusing on magnetized liner inertial fusion (MagLIF), where cylindrical metal liners compress DT fuel under strong magnetic fields and pre-heat. We discuss how the low implosion velocities, direct-drive efficiency, and scalable pulser architecture can achieve ignition-level conditions at low capital cost. Our multi-dimensional simulations, benchmarked against experiments at the Z facility, show that scaling from 20 MA to 50-60 MA of current enables net facility gain. We then introduce our Demonstration System (DS), a pulsed-power driver designed to deliver more than 60 MA and store approximately 80 MJ of energy. The DS is designed to achieve a 1000x increase in effective performance compared to the NIF, delivering approximately 100x greater facility-level energy gain -- and importantly, achieving net facility gain, or Qf>1 -- at just 1/10 the capital cost. We also examine the engineering requirements for repetitive operation, target fabrication, and chamber maintenance, highlighting a practical roadmap to commercial power plants.


![[mdfiles/2504.10680.md|2504.10680]]
### AI Justification:
This paper primarily focuses on inertial fusion energy techniques and their engineering aspects, specifically within magnetized liner inertial fusion (MagLIF). While there are mentions of magnetic fields and their roles in compression under fusion conditions, the study does not align closely with your specific interests in "magnetic dynamics of plasmas in the interstellar medium" or "scale-dependent magnetic structuring" which relate to astrophysical contexts rather than fusion energy applications.
# (341/382) http://arxiv.org/pdf/2504.09747v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Low Mass Ratio Overcontact Binary GV Leonis and Its Circumbinary Companion
**Jae Woo Lee,Jang-Ho Park,Mi-Hwa Song,Min-Ji Jeong,Chun-Hwey Kim**


#mhd
### Abstract:
Photometric and spectroscopic observations of GV Leo were performed from 2017 to 2024. The light curves show a flat bottom at the primary eclipse and the conventional OConnell effect. The echelle spectra reveal that the effective temperature and rotation velocity of the more massive secondary are $T_{\rm eff,2} $ = 5220 $ \pm $ 120 K and $ v_2 \sin i $ = 223 $ \pm $ 40 km s $ ^{-1}$ , respectively. Our binary modeling indicates that the program target is a W-subclass contact binary with a mass ratio of $q$ = 5.48, an inclination angle of $i$ = 81 $^\circ$ .68, a temperature difference of ( $T_{\rm eff,1}-T_{\rm eff,2} $ ) = 154 K, and a filling factor of $ f$ = 36 \%. The light asymmetries were reasonably modeled by a dark starspot on the secondarys photosphere. Including our 26 minimum epochs, 84 times of minimum light were used to investigate the orbital period of the system. We found that the eclipse times of GV Leo have varied by a sinusoid with a period of 14.9 years and a semi-amplitude of 0.0076 days superimposed on a downward parabola. The periodic modulation is interpreted as a light time effect produced by an unseen outer tertiary with a minimum mass of 0.26 M $_\odot$ , while the parabolic component is thought to be a combination of mass transfer (secondary to primary) and angular momentum loss driven by magnetic braking. The circumbinary tertiary would have caused the eclipsing pair of GV Leo to evolve into its current short-period contact state by removing angular momentum from the primordial widish binary.


![[mdfiles/2504.09747.md|2504.09747]]
### AI Justification:
This paper appears to primarily focus on the characteristics of a binary star system and its circumbinary companion, which is not directly aligned with your research interests in magnetic dynamics within astrophysical plasmas. Although it mentions "magnetic braking," which could relate to the impact of magnetic fields on stellar evolution, the overall emphasis on binary modeling and light curve analysis does not sufficiently engage with the themes of magnetic field amplification and interactions in plasma environments that are central to your work.
# (342/382) http://arxiv.org/pdf/2504.09194v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetorheological Characterization of Blood Analogues Seeded with Paramagnetic Particles
**R. Rodrigues,F. J. Galindo-Rosales,L. Campo-Deano**


#mhd
### Abstract:
Magnetic particles can be useful in various medical applications, gaining access to the whole body if deployed in the blood stream. Localised drug delivery, haemorrhage control and cancer treatment are among the applications with potential to become revolutionary therapies. Despite this interest, a magnetorheological characterisation of particle-seeded blood has yet to be achieved. In this work, we evaluate the magnetorheological response of polymeric blood analogues seeded with paramagnetic particles in different concentrations, under the effects of a uniform, density-varying magnetic field. Through steady shear experiments, we encounter the usual magnetically-induced shear thinning response, and oscillatory shear results point toward some significant alterations in the fluids microstructure. However, experimental limitations make it difficult to accurately evaluate the oscillatory shear response of such rheologically subtle fluids, limiting both the quality and quantity of achievable information. Despite experimental limitations, our results demonstrate that magnetic fields can induce marked and quantifiable rheological changes in seeded blood analogues. The framework established here provides a foundation for future studies on real blood samples and for the design of magnetically responsive biomedical systems.


![[mdfiles/2504.09194.md|2504.09194]]
### AI Justification:
This paper’s exploration of “magnetically induced shear thinning response” provides limited relevance to my focus on “magnetic field amplification” and “emergent magnetic dynamics in turbulent plasmas.” Although it covers the effects of magnetic fields in fluids, it primarily addresses medical applications rather than the astrophysical phenomena relevant to my research.
# (343/382) http://arxiv.org/pdf/2504.08683v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Asteroseismic predictions for a massive main-sequence merger product
**J. Henneco,F. R. N. Schneider,M. Heller,S. Hekker,C. Aerts**


#mhd
### Abstract:
The products of stellar mergers between two massive main-sequence (MS) stars appear as seemingly normal MS stars after a phase of thermal relaxation, if not for certain peculiarities. Since these peculiarities are not limited to the merger products surface, we use asteroseismology to predict how the differences in the internal structure of a merger product and a genuine single star manifest via properties of non-radial stellar pulsations. We mapped the result of a 3D MHD stellar merger simulation between a 9 and an 8 solar-mass MS star to 1D and evolved it through the MS. We compare the predicted pressure (p) and gravity (g) modes for the merger product model with those predicted for a corresponding genuine single-star model. The p-mode frequencies are consistently lower for the merger product than for the genuine single star, and the differences between them are more than a thousand times larger than the current best observational uncertainties for measured mode frequencies of this kind. Even though g-mode period spacing differences vary in value and sign throughout the MS, they, too, are larger than the current best observational uncertainties for such long-period modes. This, combined with additional variability in the merger products period spacing patterns, shows the potential of identifying merger products in future-forward modelling. We also attempt to replicate the merger products structure using three widely applied 1D merger prescriptions and repeat the asteroseismic analysis. Although none of the 1D prescriptions reproduces the entire merger products structure, we conclude that the prescription with shock heating shows the highest potential, provided that it can be calibrated on binary-evolution-driven 3D merger simulations. Our work should be expanded to encompass the various possible merger product structures predicted to exist in the Universe. (abridged)


![[mdfiles/2504.08683.md|2504.08683]]
### AI Justification:
This paper has low relevance to your research interests in theoretical astrophysics and plasma physics, as it focuses primarily on stellar mergers and asteroseismology rather than the magnetic dynamics of plasmas in the interstellar medium. Specific phrases like "3D MHD stellar merger simulation" may imply some overlap with magnetic fields, but the main emphasis on stellar pulsations and internal structure does not address your key areas of focus such as magnetic field amplification or interactions shaping magnetic dynamics.
# (344/382) http://arxiv.org/pdf/2504.07071v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### ASASSN-14dx... A cataclysmic variable harbouring a massive pulsating white dwarf
**Pasi Hakala,Ingrid Pelisoli,Boris T. Gaensicke,Pablo Rodriguez-Gil,Thomas R. Marsh,Elme Breedt,...**


#mhd
### Abstract:
We present the results of our study of ASASSN-14dx, a previously known but poorly characterised cataclysmic variable (CV). The source was observed as part of an ongoing high-time-resolution photometric survey of CVs, which revealed that, in addition to the known 82.8min orbital period, it also exhibits other transient periods, the strongest of which around 4 and 14 min. Here, we report our findings resulting from a multifaceted follow-up programme consisting of optical spectroscopy, spectropolarimetry, imaging polarimetry, and multicolour fast photometry. We find that the source displays complex optical variability, which is best explained by the presence of a massive white dwarf exhibiting non-radial pulsations. An intermediate polar-like scenario involving a spinning magnetic white dwarf can be ruled out based on the detected changes in the observed periods. Based on our optical spectroscopy, we can constrain the mass and effective temperature of the white dwarf to be ~1.1 Msol and 16 100 K, respectively. The overall intrinsic flux level of the source is unusually high, suggesting that there remains significant residual emission from the accretion disc and/or the white dwarf even ten years after the 2014 outburst. Finally, we cannot detect any spectroscopic signatures from the donor star, making ASASSN-14dx a possible period bouncer system evolving towards a longer orbital period.


![[mdfiles/2504.07071.md|2504.07071]]
### AI Justification:
The paper focuses on a cataclysmic variable and its associated characteristics, which, despite being an interesting astrophysical phenomenon, does not align with my research interests in "the magnetic dynamics of plasmas in the interstellar medium." The absence of exploration regarding "magnetic field amplification" or "force interactions shaping magnetic dynamics" in relation to plasma environments limits its relevance to my work.
# (345/382) http://arxiv.org/pdf/2504.05671v2


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The Impact of Neutrino Magnetic Moments on the Evolution of the Helium Flash and Lithium-Rich Red Clump Stars
**Xizhen Lu,Chunhua Zhu,Guoliang Lu,Sufen Guo,Zhuowen Li,Gang Zhao**


#mhd
### Abstract:
The detection of the neutrino magnetic moment (NMM, $\mu_v$ ) is one of the most significant challenges in physics. The additional energy loss due to NMM can significantly influence the He flash evolution in low-mass stars. Using the MESA code, we investigated the impact of NMM on the He flash evolution in low-mass stars. We found that NMM leads to an increase in both the critical He core mass required for the He flash and the luminosity of TRGB. For a typical $Z = 1 Z_{\odot}$ , $M$ = 1.0 $M_{\odot}$ , and $\mu_v = 3 \times 10^{-12} \mu_{\mathrm{B}} $ model, the He core mass increases by $ \sim 5\%$ , and the TRGB luminosity increases by $\sim 35\%$ compared to the model without NMM. However, contrary to previous conclusions, our model indicates that the He flash occurs earlier, rather than delayed, with increasing NMM values. This is because the additional energy loss from NMM accelerates the contraction of the He core, releases more gravitational energy that heats the H shell and increases the hydrogen burning rate, thereby causing the He core to reach the critical mass faster and advancing the He flash. An increase in NMM results in a higher peak luminosity for the first He flash, a more off-center ignition position, and sub-flashes with higher luminosities, shorter intervals, and higher frequency. We found that the internal gravity wave (IGW) mixing generated by the He flash can induce sufficient mixing in the radiative zone, turning the overshoot region into a low-Dmix bottleneck within the stellar interior. The increase in NMM in the model narrows the overshoot bottleneck region, enabling Li to enter the surface convection zone more quickly, thereby enhancing the enrichment effect of IGW mixing on surface Li. For models incorporating both NMM and IGW mixing, the reduction in the overshoot bottleneck region allows them to effectively produce super Li-rich red clump star samples.


![[mdfiles/2504.05671.md|2504.05671]]
### AI Justification:
This paper does not closely align with your research interests in theoretical astrophysics and plasma physics as it primarily focuses on the impact of neutrino magnetic moments on stellar evolution, specifically in low-mass stars and their He flash evolution. While it mentions interactions involving magnetic moments, the main themes of magnetic field amplification, the dynamics of plasmas in the interstellar medium, and their multi-scale behavior within various plasma environments are not central to the study presented in the abstract.
# (346/382) http://arxiv.org/pdf/2504.05215v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quasinormal modes and absorption cross-section of a Bardeen black hole surrounded by perfect fluid dark matter in four dimensions
**Angel Rincon,Sharmanthie Fernando,Grigoris Panotopoulos,Leonardo Balart**


#mhd
### Abstract:
In this paper we study quasinormal modes and absorption cross sections for the $(1+3)$ -dimensional Bardeen black hole surrounded by perfect fluid dark matter. Studies of the massless scalar field is already done in \cite{Sun...2023slzl}. Hence, in this paper we will focus on the massive scalar field perturbations and massless Dirac field perturbations. To compute the quasinormal modes we use the semi-analytical 3rd-order WKB method, which has been shown to be one of the best approaches when the effective potential is adequate and when $n < \ell$ and $n < \lambda$ . We have also utilized the P\`oschl-Teller method to compare the valus obtained using the WKB approach. We have computed quasinormal frequencies by varying various parameters of the theory such as the mass of the scalar field $\mu$ , dark matter parameter $\alpha$ and the magnetic charge $g$ . We have summarized our solutions in tables and figures for clarity. As for the absorption cross section, we used third order WKB approach to compute reflection, transmission coefficients and partial absorption cross sections. Graphs are presented to demonstrate the behavior of the above quantities when the dark matter parameter and mass of the massive scalar field are varied.


![[mdfiles/2504.05215.md|2504.05215]]
### AI Justification:
This paper appears to have low relevance to your research focus on magnetic dynamics in plasmas, as it primarily investigates quasinormal modes and absorption cross-sections in a black hole context rather than exploring mechanisms of magnetic field amplification or interactions within plasma environments. The abstract mentions "massive scalar field perturbations" and "dark matter parameter," but lacks any mention of magnetic dynamics, turbulence, or the scale-dependent structuring of magnetic fields, which are central to your research interests.
# (347/382) http://arxiv.org/pdf/2504.04813v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Generalized Fermi-Dirac Distribution of Exclusive Fermions
**Chung-Ru Lee,Chin-Rong Lee**


#mhd
### Abstract:
A system of exclusive fermions occurs when two fermions of opposite spin are prohibited from occupying the same quantum level. We derive the distribution of exclusive fermions via the employment of the grand canonical ensemble. Salient features of its statistical properties, compared to the free electron gases, include... larger Fermi energy, higher degeneracy pressure, but the same Pauli paramagnetism and Landau diamagnetism. In particular, higher degeneracy pressure leads to an inflation of the Chandrasekhar limit to 1.6 times when applied to white dwarf stars and neutron stars.


![[mdfiles/2504.04813.md|2504.04813]]
### AI Justification:
This paper discusses the generalized Fermi-Dirac distribution but does not directly align with your research interests in the "magnetic dynamics of plasmas" or the mechanisms behind "magnetic field amplification." The focus on statistical properties of exclusive fermions, such as their implications for "white dwarf stars and neutron stars," does not pertain to the "interstellar medium," nor addresses the complex behavior of magnetic fields as outlined in your areas of interest.
# (348/382) http://arxiv.org/pdf/2504.03572v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Characterizing planetary systems with SPIRou... Detection of a sub-Neptune in a 6 day period orbit around the M dwarf Gl 410
**A. Carmona,X. Delfosse,M. Ould-Elhkim,P. Cortes-Zuleta,N. C. Hara,E. Artigau,...**


#mhd
### Abstract:
The search of exoplanets around nearby M dwarfs is a crucial milestone to perform the census of planetary systems in the vicinity of our Solar System. Since 2018 our team is carrying a radial-velocity blind search program for planets around nearby M dwarfs with the near-IR spectro-polarimeter and velocimeter SPIRou at the CFHT and the optical velocimeter SOPHIE at the OHP in France. Here we present our results on Gl 410, a 0.55 Msun 480+-150 Myr old active M dwarf distant 12 pc. We use the line-by-line (LBL) technique to measure the RVs with SPIRou and the template matching method with SOPHIE. Three different methods, two based in principal component analysis (PCA), are used to clean the SPIRou RVs for systematics. Gaussian processes (GP) modeling is applied to correct the SOPHIE RVs for stellar activity. The l1 and apodize sine periodogram (ASP) analysis is used to search for planetary signals in the SPIRou data taking into account activity indicators. We analyse TESS data and search for planetary transits. We report the detection of a M sin(i)=8.4+-1.3 Mearth sub-Neptune planet at a period of 6.020+-0.004 days in circular orbit with SPIRou. The same signal, although with lower significance, is also retrieved in the SOPHIE RV data after correction for activity using a GP trained on SPIRous longitudinal magnetic field (Bl) measurements. TESS data indicates that the planet is not transiting. We find within the SPIRou wPCA RVs tentative evidence for two additional planetary signals at 2.99 and 18.7 days. In conclusion, infrared RVs are a powerful method to detect extrasolar planets around active M dwarfs, care should be taken however to correct/filter systematics generated by residuals of the telluric correction or small structures in the detector plane. The LBL technique combined with PCA offers a promising way to reach this objective. Further monitoring of Gl 410 is necessary.


![[mdfiles/2504.03572.md|2504.03572]]
### AI Justification:
The paper's relevance to your interests is minimal, as it primarily focuses on the detection of exoplanets around M dwarfs and utilizes methods such as radial-velocity measurements and Gaussian processes. This differs significantly from your research on "magnetic dynamics of plasmas" and "how magnetic fields behave and interact," particularly as the context lies outside astrophysical plasma environments and does not address magnetic field amplification or dynamics in turbulent plasmas.
# (349/382) http://arxiv.org/pdf/2504.02596v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Cosmic ray ionisation of a post-impact early Earth atmosphere... Solar cosmic ray ionisation must be considered in origin-of-life scenarios
**S. R. Raeside,D. Rodgers-Lee,P. B. Rimmer**


#mhd
### Abstract:
Cosmic rays (CR), both solar and Galactic, have an ionising effect on the Earths atmosphere and are thought to be important for prebiotic molecule production. In particular, the $\rm{H_2}$ -dominated atmosphere following an ocean-vaporising impact is considered favourable to prebiotic molecule formation. We model solar and Galactic CR transport through a post-impact early Earth atmosphere at 200Myr. We aim to identify the differences in the resulting ionisation rates, $\zeta$ , particularly at the Earths surface during a period when the Sun was very active. We use a Monte Carlo model to describe CR transport through the early Earth atmosphere, giving the CR spectra as a function of altitude. We calculate $\zeta$ and the ion-pair production rate, $Q$ , as a function of altitude due to Galactic and solar CR. The Galactic and solar CR spectra are both affected by the Suns rotation rate, $\Omega$ , because the solar wind velocity and magnetic field strength both depend on $\Omega$ and influence CR transport. We consider a range of input spectra resulting from the range of possible $\Omega$ , from $3.5-15\, \Omega_{\rm{\odot}}$ . To account for the possibility that the Galactic CR spectrum outside the Solar System varies over Gyr timescales, we compare top-of-atmosphere $\zeta$ resulting from two different scenarios. We also consider the suppression of the CR spectra by a planetary magnetic field. We find that $\zeta$ and $Q$ due to CR are dominated by solar CR in the early Earth atmosphere for most cases. The corresponding $\zeta$ at the early Earths surface ranges from $5 \times 10^{-21}\rm{s^{-1}}$ for $\Omega = 3.5\,\Omega_{\rm{\odot}} $ to $ 1 \times 10^{-16}\rm{s^{-1}} $ for $ \Omega = 15\,\Omega_{\rm{\odot}}$ . Thus if the young Sun was a fast rotator, it is likely that solar CR had a significant effect on the chemistry at the Earths surface at the time when life is likely to have formed.


![[mdfiles/2504.02596.md|2504.02596]]
### AI Justification:
This paper primarily focuses on cosmic ray ionization and its effects on the early Earth's atmosphere, which does not align closely with your specific interests in the magnetic dynamics of plasmas in the interstellar medium. While it briefly touches on the influence of the planetary magnetic field on cosmic ray transport, it lacks a thorough exploration of magnetic field amplification and interactions at the required scales or contexts pertinent to your astrophysical focus.
# (350/382) http://arxiv.org/pdf/2504.02389v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Response of magnetic particle to rotating magnetic field in viscoelastic fluid
**Han Gao,Zhiyuan Zhao,Masao Doi,Ye Xu**


#mhd
### Abstract:
The rotational dynamics of a freely suspended ferromagnetic particle in viscoelastic fluid subjected to a rotating magnetic field is studied by experiments and theory. Our result reveals that when the characteristic relaxation time of the fluid is much smaller than the inverse critical field frequency, the particles rotation behavior aligns with that in Newtonian fluids. Increasing the relaxation time enhances the time-averaged rotation frequency of the particle that undergo asynchronous rotation. Moreover, the critical frequency is shown to scale linearly with the magnetic field intensity and inversely with the fluids zero-shear viscosity. Our work is expected to guide precise manipulation of ferromagnetic particles in biomedical systems where viscoelastic environments dominate.


![[mdfiles/2504.02389.md|2504.02389]]
### AI Justification:
This paper has low relevance to your interests in theoretical astrophysics and plasma physics, particularly regarding magnetic fields in the interstellar medium. While it discusses magnetic interactions, the focus on "ferromagnetic particles in viscoelastic fluid" does not align with your research on "magnetic field amplification," "emergent magnetic dynamics," or "scale-dependent magnetic structuring" within astrophysical plasmas.
# (351/382) http://arxiv.org/pdf/2504.01653v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Quasinormal Modes and Stability Analysis of the JMN-1 Naked Singularity
**Akshat Pathrikar,Parth Bambhaniya,Pankaj S. Joshi,Elisabete M. de Gouveia Dal Pino**


#mhd
### Abstract:
In this paper, we perform a comprehensive analysis of the quasinormal modes in the Joshi-Malafarina-Narayan (JMN-1) naked singularity by investigating its response to linear perturbations, including scalar, electromagnetic, and gravitational perturbations. To analyze the stability of the JMN-1 naked singularity under axial perturbations, we compute the quasinormal mode frequencies using the Wentzel-Kramers-Brillouin method. The quasinormal mode frequencies provides information about the stability of spacetime, with the real part of the frequency determining the oscillation rate and the imaginary part governing the decay or growth of perturbations. Our results indicate that by imposing appropriate boundary conditions, we find that the JMN-1 spacetime remains dynamically stable under axial perturbations.


![[mdfiles/2504.01653.md|2504.01653]]
### AI Justification:
This paper focuses on the stability analysis of a naked singularity using quasinormal modes, which does not directly relate to your interest in "magnetic dynamics of plasmas in the interstellar medium". While it investigates linear perturbations, including electromagnetic ones, the primary emphasis is on stability in spacetime rather than "magnetic field amplification" or "emergent magnetic dynamics in turbulent plasmas" within astrophysical contexts.
# (352/382) http://arxiv.org/pdf/2504.01327v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Multi-wavelength properties of $z\gtrsim 6$ LISA detectable events
**Srija Chakraborty,Simona Gallerani,Fabio Di Mascia,Tommaso Zana,Milena Valentini,Stefano Carniani,...**


#mhd
### Abstract:
We investigate the intrinsic and observational properties of $z\gtrsim 6$ galaxies hosting coalescing massive black holes (MBHs) that gives rise to gravitational waves (GWs) detectable with the Laser Interferometer Space Antenna (LISA). We adopt a zoom-in cosmological hydrodynamical simulation of galaxy formation and black hole (BH) co-evolution, zoomed-in on a $M_h \sim 10^{12}~\rm M_{\odot}$ dark matter halo at z = 6, which hosts a fast accreting super-massive black hole (SMBH) and a star-forming galaxy. Following the SMBH formation backward in time, we identify the merging events that concurred to its formation and we pick up the ones that are detectable with LISA. Among these LISA detectable events (LDEs), we select those that, based on their intrinsic properties are expected to be bright in one or more electromagnetic (EM) bands. We post-process these events with dust radiative transfer calculations to make predictions about their spectral energy distributions and continuum maps in the JWST to ALMA wavelength range. We compare the spectra arising from galaxies hosting the merging MBHs with those arising from AGN powered by single accreting BHs. We find that it will be impossible to identify an LDE from the continuum SEDs because of the absence of specific imprints from the merging MBHs. We also compute the profile of the H $_{\rm \alpha}$ line arising from LDEs, considering the contribution from their star-forming regions and the accreting MBHs. We find that the presence of two accreting MBHs would be difficult to infer even if both MBHs accrete at super-Eddington rates. We conclude that the combined detection of GW and EM signals from $z\gtrsim 6$ MBHs is challenging not only because of the poor sky-localization provided by LISA, but also because the loudest GW emitters are not massive enough to leave significant signatures in the emission lines arising from the broad line region.


![[mdfiles/2504.01327.md|2504.01327]]
### AI Justification:
This paper primarily investigates the formation and observational properties of massive black holes in the context of gravitational waves, rather than focusing specifically on the magnetic dynamics of plasmas, which is central to your research interests. While there is a mention of "co-evolution" of galaxies and black holes, it lacks the depth in exploring "magnetic field amplification" or "magnetic dynamics in plasma environments" that you are seeking.
# (353/382) http://arxiv.org/pdf/2504.02030v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Neutron Star Eclipses as Axion Laboratories
**Vedran Brdar,Dibya S. Chattopadhyay**


#mhd
### Abstract:
In light-shining-through-walls experiments, axions and axion-like particles (ALPs) are searched for by exposing an optically thick barrier to a laser beam. In a magnetic field, photons could convert into ALPs in front of the barrier and reconvert behind it, giving rise to a signal that can occur only in the presence of such hidden particles. In this work, we utilize the light-shining-through-walls concept and apply it to astrophysical scales. Namely, we consider eclipsing binary systems, consisting of a neutron star, which is a bright source of X-rays, and a companion star with a much larger radius. Space observatories such as XMM-Newton and NuSTAR have performed extensive measurements of such systems, obtaining data on both out-of-eclipse photon rates and those during eclipses. The latter are typically $\mathscr{O}(10^2-10^3)$ times smaller, due to the fact that X-rays propagating along the line of sight from the neutron star to the X-ray observatory do not pass through the barrier that is the companion star. Using this attenuation, we derive a constraint on ALP-photon coupling of $g_{a\gamma} \simeq 10^{-10} \,\text{GeV}^{-1}$ for the LMC X-4 eclipsing binary system, surpassing current bounds from light-shining-through-walls experiments by several orders of magnitude. We also present future prospects that could realistically improve this limit by an order of magnitude in $g_{a\gamma}$ , making it competitive with some of the strongest limits derived to date.


![[mdfiles/2504.02030.md|2504.02030]]
### AI Justification:
The paper investigates axion-like particles (ALPs) in the context of neutron star systems, which could indirectly relate to the dynamics of magnetic fields through the interaction of light and magnetic fields in astrophysical scenarios. However, it primarily focuses on light propagation and particle interactions rather than the magnetic dynamics and amplification mechanisms or turbulent behaviors of plasmas that are central to your research interests.
# (354/382) http://arxiv.org/pdf/2504.01074v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Lighting up the nano-hertz gravitational wave sky... opportunities and challenges of multimessenger astronomy with PTA experiments
**Riccardo J. Truant,David Izquierdo-Villalba,Alberto Sesana,Golam Mohiuddin Shaifullah,Matteo Bonetti,Daniele Spinoso,...**


#mhd
### Abstract:
Pulsar Timing Array (PTA) experiments have the potential to unveil continuous gravitational wave (CGW) signals from individual massive black hole binaries (MBHBs). Detecting them in both gravitational waves (GW) and the electromagnetic (EM) spectrum will open a new chapter in multimessenger astronomy. We investigate the feasibility of conducting multimessenger studies by combining the CGW detections from an idealized 30-year SKA PTA and the optical data from the forthcoming LSST survey. To this end, we employed the $\texttt{L-Galaxies}$ semi-analytical model applied to the $\texttt{Millennium}$ simulation. We generated 200 different all-sky lightcones that include galaxies, massive black holes, and MBHBs whose emission is modeled based on their star formation histories and gas accretion physics. We predict an average of $\approx 33$ CGW detections, with signal-to-noise ratios $ S/N > 5 $ . The detected MBHBs are typically at $ z < 0.5 $ , with masses of $ \sim 3 \times 10^{9} M_{\odot} $ , mass ratios $ > 0.6 $ and eccentricities $ \lesssim 0.2$ . In terms of EM counterparts, we find less than 15% of these systems to be connected with an AGN detectable by LSST, while their host galaxies are easily detectable ( $ < 23$ mag) massive ( $ M_{\star} > 10^{11} M_{\odot}$ ) ellipticals with typical star formation rates ( $10^{-15} yr^{-1} < sSRF < 10^{-10} yr^{-1}$ ). Although the CGW-EM counterpart association is complicated by poor sky localization (only 35% of these CGWs are localized within $\rm 100\, deg^2$ ), the number of galaxy host candidates can be considerably reduced (thousands to tens) by applying priors based on the galaxy-MBH correlations. However, picking the actual host among these candidates is highly non-trivial, as they occupy a similar region in any optical color-color diagram. Our findings highlight the considerable challenges entailed in opening the low-frequency multimessenger GW sky.


![[mdfiles/2504.01074.md|2504.01074]]
### AI Justification:
The paper focuses on multimessenger astronomy and the detection of continuous gravitational waves, which does not align with my research interests in magnetic dynamics and plasma physics. While it discusses astrophysical phenomena involving black holes, it lacks the exploration of magnetic field amplification, interactions, or emergent dynamics within plasma environments that are central to my work.
# (355/382) http://arxiv.org/pdf/2504.00645v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic Pillar Induced Poiseuille-like Flow in Microfluidic Channels with Viscous and Viscoelastic Fluids
**Charles Paul Moore,Stefan Rouach,Marine Le Goas,Sandra Lerouge,Nicolas Tsapis,Jerome Fresnais,...**


#mhd
### Abstract:
Mucociliary clearance in mammals serves as the primary defense mechanism for removing particulate matter deposited in the pulmonary airways. Dysfunctions in this process are linked to serious respiratory diseases and can hinder effective drug delivery to the lungs. Microfluidic systems have emerged as a promising alternative for replicating lung functions in non-cellular physiological environments, offering a simpler and more controllable approach compared to in vivo and in vitro assays. Here we present a microfluidic platform featuring a closed-loop circular microchannel, integrating thousand 75 micrometer high magnetic pillars arranged in a square array. Made of polydimethylsiloxane and loaded with iron microparticles, the pillars are studied using scanning electron microscopy and magnetometry; their internal structure and bending response to a magnetic field are quantitatively analyzed. Using a combination of experimental data and finite element simulations, we found that the magnetic torque induced by permanent magnets dominates over magnetic force, generating fluid flow in the microchannel. Under the application of a rotating field, the time-dependent deflection of the pillars closely mimics the behavior of lung cilia, exhibiting alternating recovery phases and rapid whip-like movements. The velocity profiles of viscous and viscoelastic fluids are examined, and shown to display Poiseuille-type flow. By varying the viscosity of the fluids across four orders of magnitude, we identified a transition in propulsion regimes between viscous and elastic-driven flows. This active microfluidic platform offers a promising approach for modeling mucociliary clearance in drug delivery applications.


![[mdfiles/2504.00645.md|2504.00645]]
### AI Justification:
The paper appears to focus on magnetic interactions within microfluidic channels and the manipulation of fluid flow via magnetic pillars, which does not align well with my research interests in theoretical astrophysics and plasma physics. Specifically, it lacks a focus on "magnetic field amplification" or "emergent magnetic dynamics in turbulent plasmas" as outlined in my prompt, thus offering minimal insight into the magnetic dynamics of plasmas in the interstellar medium.
# (356/382) http://arxiv.org/pdf/2502.05265v3


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Light curves and spectra for stellar collisions between main-sequence stars in galactic nuclei
**Taeho Ryu,Luc Dessart**


#mhd
### Abstract:
High-velocity stellar collisions in galactic nuclei produce ejecta that generate potentially observable electromagnetic radiation, making them promising nuclear transients. However, the photometric and spectroscopic properties of these collisions, which would more frequently involve main-sequence stars, remain largely unexplored. Here, using 3D hydrodynamics and 1D radiative-transfer simulations, we investigate the properties and observables of the debris produced in high-velocity collisions between terminal-age main-sequence stars, covering a wide range of collision configurations. The ejecta produce bright ultraviolet (UV) flares with bolometric luminosities typically peaking at $\gtrsim10^{43}$ erg s $^{-1}$ , declining steeply as $t^{-2}-t^{-4}$ to reach $\gtrsim10^{41}-10^{42}$ erg s $^{-1}$ at 0.5 d and leveling off on a plateau at $10^{39}-10^{41.5}$ erg s $^{-1}$ ( $M_V$ between $-$ 10 to $-$ 15 mag) after a few days. Their spectra evolve considerably during the first few days, morphing from UV- to optical-dominated. The UV range shows numerous resonance transitions from metals like C, N, and O, whereas the optical primarily shows H I Balmer lines. These properties are qualitatively similar to those observed, as well as obtained in models of Type II supernovae. Observables from these events exhibit clear correlations with collision configurations, including impact parameter, relative velocity, and stellar masses. We provide fitting formulae to describe these correlations. Detecting these flares requires sub-day cadence surveys such as ULTRASAT, combined with spectroscopic observations to disentangle degeneracies and infer collision characteristics.


![[mdfiles/2502.05265.md|2502.05265]]
### AI Justification:
The paper investigates stellar collisions in galactic nuclei and their resultant electromagnetic emissions, but it does not address the dynamics of magnetic fields or their interactions within plasma environments, which are central to my research focus. While it mentions the observational characteristics of these collisions, it lacks exploration of "magnetic field amplification" or "emergent magnetic dynamics in turbulent plasmas," making it less relevant to my interests in theoretical astrophysics and plasma physics.
# (357/382) http://arxiv.org/pdf/2503.19984v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Hybrid Magnetically and Electrically Powered Metallo-Dielectric Janus Microrobots... Enhanced Motion Control and Operation Beyond Planar Limits
**Ido Rachbuch,Sinwook Park,Yuval Katz,Touvia Miloh,Gilad Yossifon**


#mhd
### Abstract:
This study introduces the integration of hybrid magnetic and electric actuation mechanisms to achieve advanced motion capabilities for Janus particle (JP) microrobots. We demonstrate enhanced in-plane motion control through versatile control strategies and present the concepts of interplanar transitions and 2.5-dimensional (2.5D) trajectories, enabled by magnetic levitation and electrostatic trapping. These innovations expand the mobility of JPs into 3D space, allowing dynamic operation beyond the limitations of traditional surface-bound motion. Key functionalities include obstacle crossing, transitions to elevated surfaces, and discrete surface patterning enabling highly localized interventions. Using this set of tools, we also showcase the controlled out-of-plane transport of both synthetic and biological cargo. Together, these advancements lay the groundwork for novel microrobot-related applications in microfluidic systems and biomedical research.


![[mdfiles/2503.19984.md|2503.19984]]
### AI Justification:
This paper's focus on hybrid magnetic and electric actuation mechanisms demonstrates interesting applications of magnetic fields, but it primarily deals with microrobotics and mobility strategies, which diverge from my research interests in the magnetic dynamics of plasmas in the interstellar medium. While it mentions "enhanced motion control" and "magnetic levitation," it does not address the magnetic field amplification or interactions in astrophysical contexts that are central to my research focus.
# (358/382) http://arxiv.org/pdf/2503.18321v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Magnetic Monopoles and Exotic States in $SU(4)_c \times SU(2)_L \times SU(2)_R$
**Thomas W. Kephart,Qaisar Shafi**


#mhd
### Abstract:
In the Pati-Salam gauge symmetry $SU(4)_c \times SU(2)_L \times SU(2)_R$ (4-2-2, for short), the observed quarks and leptons of each family reside in the bi-fundamental representations $(4,2,1)$ and $({\bar 4},1,2)$ . There exist, however, the fundamental representations $(4,1,1)$ , $(1,2,1)$ and $(1,1,2)$ and their hermitian conjugates, which show the presence, in principle, of yet to be discovered color triplets that carry electric charge $\pm{e/6}$ , and color singlet particles with charges of $\pm{e/2}$ . These Standard Model charges are in full accord with the fact that the 4-2-2 model predicts the presence of a topologically stable finite energy magnetic monopole that carries two quanta of Dirac magnetic charge, i.e., $4 \pi/e$ , as well as color magnetic charge that is screened beyond the quark confinement scale. The 4-2-2 model therefore predicts the existence of exotic baryons, mesons and leptons that carry fractional ( $\pm{e/2}$ ) electric charges. Since their origin lies in the fundamental representations of 4-2-2, these exotic particles may turn out to be relatively light, in the TeV mass range or so. The 4-2-2 magnetic monopole mass depends on the 4-2-2 symmetry breaking scale which may be as low as a few TeV.


![[mdfiles/2503.18321.md|2503.18321]]
### AI Justification:
This paper primarily focuses on the theoretical constructs related to the Pati-Salam gauge symmetry and the existence of exotic particles, rather than the dynamics of magnetic fields in astrophysical plasmas. It does not align well with my interests in "magnetic field amplification" or the "interactions shaping magnetic dynamics" within plasma environments, as indicated by its exploration of "topologically stable finite energy magnetic monopoles" which are not directly relevant to magnetic fields in the interstellar medium.
# (359/382) http://arxiv.org/pdf/2503.17841v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Non-orbital particle trapping in binary black holes through dynamic stability
**Ali Kurmus,Michal Zajacek,Greg Kestin,Louis Deslauriers**


#mhd
### Abstract:
We present an interdisciplinary comparison between binary black hole systems and Radio Frequency (RF) Paul Traps, modeling the gravitational binary system as a rotating saddle near its center. This analogy connects these seemingly unrelated systems through the concept of dynamic stability. The rotating saddle potential is analytically tractable, allowing us to prove the existence of bounded charged particle trajectories under certain conditions. By focusing on stellar-mass black holes with a weak electric charge-a feature consistent with specific astrophysical conditions that leaves the spacetime metric largely unaffected but can influence nearby particle interactions-we can neglect complicating factors such as magnetic fields from large accretion disks of heavier black holes or stellar winds. Our simulation results demonstrate that charged particles can exhibit stable, non-orbital trajectories near the center of a binary system with charged stellar-mass black holes, providing unique three-dimensional trapping primarily through gravity. This system is distinctive in the literature for its non-orbital trapping mechanism. While theoretically intriguing, this trapping relies on specific conditions, including nearly identical black hole masses. These types of non-orbital trapping mechanisms could potentially allow for longer-lived plasma configurations, enhancing our ability to detect electromagnetic signatures from these systems. The significance of this work lies in the novel comparison between a laboratory-scale quantum system and a larger astrophysical one, opening new avenues for exploring parallels between microscopic and cosmic phenomena across fourteen orders of magnitude in distance.


![[mdfiles/2503.17841.md|2503.17841]]
### AI Justification:
While the paper presents interesting insights into non-orbital particle trapping in binary black holes, it focuses primarily on gravitational dynamics rather than the magnetic dynamics of plasmas in the interstellar medium that are central to your research interests. The lack of emphasis on "magnetic field amplification," "force interactions," or "turbulence" in the context of plasmas limits its relevance to your focus on the complex behavior and structuring of magnetic fields across various astrophysical scales.
# (360/382) http://arxiv.org/pdf/2502.06950v2


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Cryoscope... A Cryogenic Infrared Survey Telescope in Antarctica
**Mansi M. Kasliwal,Nicholas Earley,Roger Smith,Tristan Guillot,Tony Travouillon,Jason Fucik,...**


#mhd
### Abstract:
We present Cryoscope--a new 50 deg $^2$ field-of-view, 1.2 m aperture, $K_{dark}$ survey telescope to be located at Dome C, Antarctica. Cryoscope has an innovative optical-thermal design wherein the entire telescope is cryogenically cooled. Cryoscope also explores new detector technology to cost-effectively tile the full focal plane. Leveraging the dark Antarctic sky and minimizing telescope thermal emission, Cryoscope achieves unprecedented deep, wide, fast and red observations, matching and exceeding volumetric survey speeds from the Ultraviolet Explorer, Vera Rubin Observatory, Nancy Grace Roman Space Telescope, SPHEREx, and NEO Surveyor. By providing coverage beyond wavelengths of 2 $\mu$ m, we aim to create the most comprehensive dynamic movie of the most obscured reaches of the Universe. Cryoscope will be a dedicated discovery engine for electromagnetic emission from coalescing compact binaries, Earth-like exoplanets orbiting cold stars, and multiple facets of time-domain, stellar and solar system science. In this paper, we describe the scientific drivers and technical innovations for this new discovery engine operating in the $K_{dark}$ passband, why we choose to deploy it in Antarctica, and the status of a fifth-scale prototype designed as a Pathfinder to retire technological risks prior to full-scale implementation. We plan to deploy the Cryoscope Pathfinder to Dome C in December 2026 and the full-scale telescope by 2030.


![[mdfiles/2502.06950.md|2502.06950]]
### AI Justification:
This paper on the Cryoscope telescope presents advancements in observational technology but does not directly address key aspects of my research focus on magnetic dynamics of plasmas in the interstellar medium. There are no mentions of magnetic field amplification, force interactions, or emergent magnetic dynamics, which are critical to understanding my interest in the complex behaviors of magnetic fields across varying astrophysical scales.
# (361/382) http://arxiv.org/pdf/2503.14025v2


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Propagation Times and Energy Losses of Cosmic Protons and Antiprotons in Interplanetary Space
**Nicola Tomassetti,Bruna Bertucci,Emanuele Fiandrini,Behrouz Khiali**


#mhd
### Abstract:
In this paper, we investigate the heliospheric modulation of cosmic rays in interplanetary space, focusing on their propagation times and energy losses over the solar cycle. To perform the calculations, we employed a data-driven model based on the stochastic method. Our model was calibrated using time-resolved and energy-resolved data from several missions including AMS-02, PAMELA, EPHIN/SOHO, BESS, and data from Voyager-1. This approach allows us to calculate probability density functions for the propagation time and energy losses of cosmic protons and antiprotons in the heliosphere. Furthermore, we explore the temporal evolution of these probabilities spanning from 1993 to 2018, covering a full 22-year cycle of magnetic polarity, which includes two solar minima and two magnetic reversals. Our calculations were carried out for cosmic protons and antiprotons, enabling us to investigate the role of charge-sign dependent effects in cosmic ray transport. These findings provide valuable insights into the physical processes of cosmic-ray propagation in the heliosphere and contribute to a deeper understanding of the solar modulation phenomenon.


![[mdfiles/2503.14025.md|2503.14025]]
### AI Justification:
The paper primarily focuses on cosmic ray propagation and energy losses in interplanetary space, which, while relevant to astrophysical plasmas, does not specifically address magnetic field amplification or the interactions of magnetic fields with plasma structures in the interstellar medium as outlined in your research interests. Although the use of a stochastic model for cosmic ray dynamics may provide insights into particle behavior, it lacks direct relevance to your concerns regarding the "magnetic dynamics of plasmas" or the "emergent magnetic dynamics in turbulent plasmas."
# (362/382) http://arxiv.org/pdf/2503.14270v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Integral modelling and Reinforcement Learning control of 3D liquid metal coating on a moving substrate
**Fabio Pino,Edoardo Fracchia,Benoit Scheid,Miguel A. Mendez**


#mhd
### Abstract:
Metallic coatings are used to improve the durability of metal surfaces, protecting them from corrosion. These protective layers are typically deposited in a fluid state via a liquid film. Controlling instabilities in the liquid film is crucial for achieving uniform and high-quality coatings. This study explores the possibility of controlling liquid films on a moving substrate using a combination of gas jets and electromagnetic actuators. To model the 3D liquid film, we extend existing integral models to incorporate the effects of electromagnetic actuators. The control strategy was developed within a reinforcement learning framework, where the Proximal Policy Optimization (PPO) algorithm interacts with the liquid film via pneumatic and electromagnetic actuators to optimize a reward function, accounting for the amplitude of the instability waves through a trial and error process. The PPO found an optimal control law, which successfully reduced interface instabilities through a novel control mechanism, where gas jets push crests and electromagnets raise troughs using the Lorentz force.


![[mdfiles/2503.14270.md|2503.14270]]
### AI Justification:
The paper's focus on controlling instabilities in a liquid film using electromagnetic actuators does not align directly with my interest in "magnetic dynamics of plasmas in the interstellar medium." Although it discusses the use of electromagnetic forces, the context is centered on liquid metal coatings and control mechanisms rather than exploring the "amplification and evolution of magnetic fields in astrophysical plasmas."
# (363/382) http://arxiv.org/pdf/2503.13216v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### A multi-messenger mass determination method for LISA Neutron-Star White-Dwarf Binaries
**Kaye Jiale Li,Jane SiNan Long,Kinwah Wu,Albert K. H. Kong**


#mhd
### Abstract:
Determining the mass of the neutron stars (NSs) accurately improves our understanding of the NS interior and complicated binary evolution. However, the masses of the systems are degenerate with orbital inclination angle when using solely gravitational waves (GWs) or electromagnetic measurements, especially for face-on binaries. Taking advantages of both GWs and optical observations for LISA neutron-star white-dwarf (NS-WD) binaries, we propose a mass determination method utilising multi-messenger observational information. By combining the binary mass function obtained from optical observations and a GW mass function, that we introduce, derived from GW observations, we demonstrate how we can set improved constraints on the NS mass and break the degeneracy in the mass and viewing inclination determination. We further comment on the universal relation of the error bar of the GW mass function versus GW signal-to-noise ratio (SNR), and propose a simple method for the estimate of capability of GW observations on mass determination with {LISA}. We show that for ultra-compact NS-WD binaries within our Galaxy, the mass of the NS can be constrained to within an accuracy of +- 0.2 \solarmass with the proposed method.


![[mdfiles/2503.13216.md|2503.13216]]
### AI Justification:
This paper is not particularly relevant to your research interests in theoretical astrophysics and plasma physics, as it focuses on mass determination in neutron-star white-dwarf binaries using multi-messenger methods rather than on the magnetic dynamics of plasmas. There is no reference to "magnetic field amplification," "force interactions," or the "emergent magnetic dynamics" that are central to your work within the interstellar medium.
# (364/382) http://arxiv.org/pdf/2503.13014v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On the electrons really contributing to dc conductivity of warm dense matter
**Nadine Wetta,Jean-Christophe Pain**


#mhd
### Abstract:
Atomic properties of warm dense matter is an active field of research. Understanding transport properties of these states is essential for providing coefficients needed by magneto-radiative hydrodynamics codes for many studies, including hydrodynamic instabilities, energy balances or heating in fusion plasmas, difficult to investigate by experimental means. In this paper, we present an average-atom approach for the calculation of direct-current electric conductivity within Zimans theory. The mean ion charge $Z^*$ , commonly called ionization, is an important input of the Ziman formula, but is not clearly defined within average-atom models. Our study spans a wide range of thermodynamical conditions, i.e., for the densities, from a few $10^{-2}$ to about 4 times the solids density, and, for the temperatures, typically from 0.1 eV to 700 eV, favorable to large differences in the mean ion charge $Z^*$ according to its definition. We compare and discuss different ways of defining $Z^*$ while trying to figure out which electrons really contribute to electric conduction. We compare our results with experimental data and published theoretical values, in particular from the second transport code comparison workshop, which was held in July 2023 at Lawrence Livermore National Laboratory. These comparisons lead us to propose indicators for the relevance of including different charges predicted by our average-atom model in the definition of $Z^*$ .


![[mdfiles/2503.13014.md|2503.13014]]
### AI Justification:
The paper focuses on the transport properties of warm dense matter in relation to electric conductivity, which touches on aspects of plasmas but lacks a direct emphasis on the magnetic dynamics and amplification of magnetic fields that are central to my research interests. While it may present relevant theoretical methods regarding plasma behavior, it does not align with my primary focus on "magnetic field amplification" or "interactions shaping magnetic dynamics" in astrophysical contexts.
# (365/382) http://arxiv.org/pdf/2503.12452v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### AstroSat-CZTI searches for hard X-ray prompt emission from Fast Radio Bursts
**G. Waratkar,M. Dixit,S. P. Tendulkar,V. Bhalerao,D. Bhattacharya,S. Vadawale**


#mhd
### Abstract:
Fast Radio Bursts (FRBs) are short-duration, highly-energetic extragalactic radio transients with unclear origins & emission mechanisms. Despite extensive multi-wavelength searches, no credible X-ray or other prompt electromagnetic counterparts have been found for extragalactic FRBs. We present results from a comprehensive search for such prompt X-ray counterparts using AstroSat-CZTI which has been actively detecting other high-energy fast transients like Gamma-ray bursts (GRBs). We undertook a systematic search in AstroSat-CZTI data for hard X-ray transients temporally & spatially coincident with 578 FRBs, and found no X-ray counterparts. We estimate flux upper limits for these events and convert them to upper limits on X-ray-to-radio fluence ratios. Further, we utilize the redshifts derived from the dispersion measures of these FRBs to compare their isotropic luminosities with those of GRBs, providing insights into potential similarities between these two classes of transients. Finally, we explore the prospects for X-ray counterpart detections using other current and upcoming X-ray monitors, including Fermi-GBM, Swift-BAT, SVOM-ECLAIRs, and Daksha, in the era of next-generation FRB detection facilities such as CHIME, DSA-2000, CHORD, and BURSTT. Our results highlight that highly sensitive X-ray monitors with large sky coverage, like Daksha, will provide the best opportunities to detect X-ray counterparts of bright FRBs.


![[mdfiles/2503.12452.md|2503.12452]]
### AI Justification:
The paper primarily investigates Fast Radio Bursts (FRBs) and their potential X-ray counterparts, which does not directly address my focus on the "magnetic dynamics of plasmas in the interstellar medium." While the findings may relate to high-energy astrophysics, they do not explore "magnetic field amplification" or "emergent magnetic dynamics in turbulent plasmas," which are central to my research interests.
# (366/382) http://arxiv.org/pdf/2502.18714v2


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Asteroseismic Study of Subgiants and Giants of the Open Cluster M67 using Kepler/K2... Expanded Sample and Precise Masses
**Claudia Reyes,Dennis Stello,Marc Hon,Yaguang Li,Timothy R. Bedding,Enrico Corsaro,...**


#mhd
### Abstract:
Sparked by the asteroseismic space revolution, ensemble studies have been used to produce empirical relations linking observed seismic properties and fundamental stellar properties. Cluster stars are particularly valuable because they have the same metallicity, distance, and age, thus reducing scatter to reveal smoother relations. We present the first study of a cluster that spans the full evolutionary sequence from subgiants to core helium-burning red giants using asteroseismology to characterise the stars in M67, including a yellow straggler. We use Kepler/K2 data to measure seismic surface gravity, examine the potential influence of core magnetic fields, derive an empirical expression for the seismic surface term, and determine the phase term $\epsilon$ of the asymptotic relation for acoustic modes, extending its analysis to evolutionary states previously unexplored in detail. Additionally, we calibrate seismic scaling relations for stellar mass and radius, and quantify their systematic errors if surface term corrections are not applied to state-of-the-art stellar models. Our masses show that the Reimers mass loss parameter can not be larger than $\eta$ $\sim$ 0.23 at the 2- $\sigma$ level. We use isochrone models designed for M67 and compare their predictions with individual mode frequencies. We find that the seismic masses for subgiants and red giant branch stars align with the isochrone-predicted masses as per their luminosity and colour. However, our results are inconsistent with the mass of one of the stellar components of an eclipsing binary system near the TAMS. We use traditional seismic $\chi^2$ fits to estimate a seismic cluster age of 3.95 $\pm$ 0.35 Gyrs.


![[mdfiles/2502.18714.md|2502.18714]]
### AI Justification:
The paper presented focuses on asteroseismic studies of stars in the open cluster M67, which primarily deals with stellar evolution and properties rather than the magnetic dynamics of plasmas in the interstellar medium. While it mentions "core magnetic fields," it does not align closely with my research interests in magnetic field amplification, plasma dynamics, or the multi-scale interactions within astrophysical plasmas.
# (367/382) http://arxiv.org/pdf/2503.11124v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Flow-Aware Navigation of Magnetic Micro-Robots in Complex Fluids via PINN-Based Prediction
**Yongyi Jia,Shu Miao,Jiayu Wu,Ming Yang,Chengzhi Hu,Xiang Li**


#mhd
### Abstract:
While magnetic micro-robots have demonstrated significant potential across various applications, including drug delivery and microsurgery, the open issue of precise navigation and control in complex fluid environments is crucial for in vivo implementation. This paper introduces a novel flow-aware navigation and control strategy for magnetic micro-robots that explicitly accounts for the impact of fluid flow on their movement. First, the proposed method employs a Physics-Informed U-Net (PI-UNet) to refine the numerically predicted fluid velocity using local observations. Then, the predicted velocity is incorporated in a flow-aware A* path planning algorithm, ensuring efficient navigation while mitigating flow-induced disturbances. Finally, a control scheme is developed to compensate for the predicted fluid velocity, thereby optimizing the micro-robots performance. A series of simulation studies and real-world experiments are conducted to validate the efficacy of the proposed approach. This method enhances both planning accuracy and control precision, expanding the potential applications of magnetic micro-robots in fluid-affected environments typical of many medical scenarios.


![[mdfiles/2503.11124.md|2503.11124]]
### AI Justification:
This paper appears to have low relevance to your research interests in theoretical astrophysics and plasma physics, particularly in the context of magnetic field dynamics in astrophysical plasmas. Although it discusses "magnetic micro-robots" and their navigation in fluid environments, the focus on methods for control and path planning in micro-scale robotics diverges from your specific interests in magnetodynamics, amplification, and emergent behaviors of magnetic fields across astronomical scales.
# (368/382) http://arxiv.org/pdf/2503.09804v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Calculation of Dark Matter as a Feature of Space-Time
**Peter H. Handel,Klara E. Splett**


#mhd
### Abstract:
We derive the first analytical formula for the density of `Dark Matter` (DM) at all length scales, thus also for the rotation curves of stars in galaxies, for the baryonic Tully-Fisher relation and for planetary systems, from Einsteins equations (EE) and classical approximations, in agreement with observations. DM is defined in Part I as the energy of the coherent gravitational field of the universe, represented by the additional equivalent ordinary matter (OM), needed at all length scales, to explain classically, with inclusion of the OM, the observed coherent gravitational field. Our derivation uses both EE and the Newtonian approximation of EE in Part I, to describe semi-classically in Part II the advection of DM, created at the level of the universe, into galaxies and clusters thereof. This advection happens proportional with their own classically generated gravitational field g, due to self-interaction of the gravitational field. It is based on the universal formula rD=lggg for the density rD of DM advected into medium and lower scale structures of the observable universe, where l is a universal constant fixed by the Tully-Fisher relations. Here g is the gravitational field of the universe; g is in main part its own source, as implied in Part I from EE. We start from a simple electromagnetic analogy that helps to make the paper generally accessible. This paper allows for the first time the exact calculation of DM in galactic halos and at all levels in the universe, based on EE and Newtonian approximations, in agreement with observations.


![[mdfiles/2503.09804.md|2503.09804]]
### AI Justification:
This paper discusses the gravitational field and dark matter (DM), which are tangentially related to your focus on magnetic dynamics in astrophysical plasmas; however, it does not directly address the amplification of magnetic fields or the interactions between magnetic, gravitational, and thermal forces within plasma environments as you have outlined. Specifically, terms like "magnetic dynamics" and "magnetic field amplification" are not present in the abstract, indicating a lack of alignment with your research interests in studying multi-scale dynamics of magnetic fields.
# (369/382) http://arxiv.org/pdf/2503.09690v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Asteroseismology of the red giant companions to Gaia BH2 and BH3
**Daniel Hey,Yaguang Li,Joel Ong**


#mhd
### Abstract:
The stellar companions in the binary black hole systems Gaia BH2 and BH3, both of which are $\alpha$ -enhanced red giant branch stars, are expected to show normal modes with the characteristic signature of convectively-driven solar-like oscillations. We investigate this using photometry from the TESS mission and find such a signal for Gaia BH2. For Gaia BH2, we measure a power excess frequency of $\nu_{\rm max}=60.15\pm0.57$ $\mu$ Hz and a large separation of $\Delta\nu=5.99\pm0.03$ $\mu$ Hz, yielding a mass of $1.19^{+0.08}_{-0.08}$ M $_\odot$ , which is in agreement with spectroscopically derived parameters. Seismic modeling favors an age for the red giant of $5.03^{+2.58}_{-3.05}$ Gyr, strongly suggesting that it is a young, $\alpha$ -enriched giant star, which are thought to arise from a binary accretion or merger scenario. Ground-based photometry of Gaia BH2 spanning 8 years indicates a photometric period of $398\pm5$ d, which we tentatively attribute to rotation. If this rotation is physical, it can not be explained solely by evolutionary spin-down or magnetic braking, and implies that the red giant underwent some tidal forcing mechanism. Suggestively, this period is close to the pseudo-synchronous spin period of P $_\text{spin}=428\pm1$ days derived from the binary orbit. For Gaia BH3, we are unable to identify an asteroseismic signal in the TESS data despite predicting that the amplitude of the signal should lie well above the measured noise level. We discuss a number of scenarios for why this signal may not be visible.


![[mdfiles/2503.09690.md|2503.09690]]
### AI Justification:
This paper examines the asteroseismic properties of red giant stars within binary black hole systems, but it lacks direct relevance to my research focus on the magnetic dynamics of plasmas in the interstellar medium. While it discusses mechanisms like tidal forcing and convective oscillations, it does not address key issues such as "magnetic field amplification" or the "interactions between magnetic, gravitational, and thermal forces," which are central to my studies in plasma environments.
# (370/382) http://arxiv.org/pdf/2503.08289v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Employing deep-learning techniques for the conservative-to-primitive recovery in binary neutron star simulations
**Ranjith Mudimadugula,Federico Schianchi,Anna Neuweiler,Thibeau Wouters,Henrique Gieg,Tim Dietrich**


#mhd
### Abstract:
The detection of GW170817, together with its electromagnetic counterparts, has proven that binary neutron star mergers are of central importance to the field of nuclear astrophysics, e.g., through a better understanding of the formation of elements and novel constraints on the supranuclear dense equation of state governing the matter inside neutron stars. Essential for understanding the binary coalescence are numerical-relativity simulations, which typically come with high computational costs requiring high-performance computing facilities. In this work, we build on recent studies to investigate whether novel techniques, such as neural networks, can be employed in the conversion of conservative variables to primitive hydrodynamical variables, such as pressure and density. In this regard, we perform -- to the best of our knowledge -- the first binary neutron star merger simulations in which such methods are employed. We show that this method results in stable simulations, reaching accuracies similar to traditional methods with an overall comparable computational cost. These simulations serve as a proof of principle that, in the future, deep learning techniques could be used within numerical-relativity simulations. However, further improvements are necessary to offer a computational advantage compared to traditional methods.


![[mdfiles/2503.08289.md|2503.08289]]
### AI Justification:
This paper appears to be of low relevance to my research interests, as it primarily focuses on binary neutron star simulations and the application of deep-learning techniques rather than on the magnetic dynamics of plasmas. The central themes of this work, including "conservative-to-primitive recovery" and "numerical-relativity simulations," do not align well with my focus areas such as "magnetic field amplification" and "emergent magnetic dynamics in turbulent plasmas."
# (371/382) http://arxiv.org/pdf/2503.07380v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Clustering analysis of Ca {\sc i} 4227 line polarization using magnetohydrodynamic simulations of the solar atmosphere
**Harsh Mathur,L. S. Anusha,Devang Agnihotri**


#mhd
### Abstract:
Ca {\sc i} 4227 \AA\, line is a strong resonance line formed in the Solar chromosphere. At the limb, it produces the largest scattering polarization signal. So far, modeling the linear polarization in this line has been limited to the use of one-dimensional semi-empirical models of the solar atmosphere. In this paper, we use three-dimensional magnetohydrodynamical models of the solar atmosphere as well as 1.5D radiative transfer to understand the formation of linear polarization profiles due to resonance scattering in this line at a near limb position. Using three-dimensional magnetohydrodynamical models of the solar atmosphere, in this paper, we perform 1.5D radiative transfer calculations to understand the formation of linear polarization profiles due to resonance scattering in this line at a near limb position. We focus on studying the sensitivity of the resonance scattering polarization to the temperature and the density structures in the atmosphere. We do not include the effects of magnetic and velocity fields in this study. We use clustering analysis to identify linear polarization profiles with similar shape and group them accordingly for our study. We analyze the structure of the linear polarization profiles across 14 clusters, each representing different realizations of the solar atmosphere. Using source function ratio plots at various wing and core wavelength positions, we provide a qualitative explanation of linear polarization profiles in these clusters.


![[mdfiles/2503.07380.md|2503.07380]]
### AI Justification:
This paper has low relevance to your research interests as it primarily focuses on the polarization of the Ca I 4227 line in the solar atmosphere without addressing magnetic field amplification or dynamics, which are central to your work. While it utilizes three-dimensional magnetohydrodynamic models, it notably excludes the effects of "magnetic and velocity fields," indicating a lack of alignment with your investigation into "magnetic dynamics of plasmas in the interstellar medium."
# (372/382) http://arxiv.org/pdf/2503.04936v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Massive Double White Dwarf Binary Mergers from the Moon... Extending the Reach of Multi-messenger Astrophysics
**Manuel Pichardo Marcano,Anjali B. Yelikar,Karan Jani**


#mhd
### Abstract:
We explore the potential of lunar-based gravitational-wave detectors to broaden the multi-messenger astrophysics landscape by detecting mergers of massive ( $\gtrsim 1~M_{\odot}$ ) double white dwarf (WD) binaries. These systems are potential progenitors of Type Ia supernovae and could serve as independent probes of cosmic expansion. We examine two proposed lunar gravitational-wave detector concepts operating in the sub-hertz band (0.1-1 Hz)... the Gravitational-Wave Lunar Observatory for Cosmology (a proxy for suspended test mass detectors) and the Lunar Gravitational-Wave Antenna (a proxy for seismic array detectors). Using both contact and Roche lobe overflow merger scenarios, we estimate that these detectors could reach distances of up to ~1 Gpc for the most massive mergers. We show that lunar detectors could observe up to dozens of massive WD mergers annually, including those originating from globular clusters. Lunar detectors would constrain the masses of these WDs with an unprecedented accuracy of one part in a million. Furthermore, these detectors would provide early warnings of weeks before merger, including sky-localization of square arcminute resolution, enabling a new era of coordinated multi-messenger follow-up of electromagnetic transients-whether they evolve into Type Ia supernovae or accretion-induced collapse events.


![[mdfiles/2503.04936.md|2503.04936]]
### AI Justification:
This paper explores the dynamics of massive double white dwarf binaries, which may indirectly relate to your interest in magnetic field behavior in astrophysical environments, particularly in identifying gravitational-wave events tied to supernova progenitors. However, the focus on lunar gravitational-wave detectors and multi-messenger astrophysics does not align directly with your specific research areas of magnetic field amplification and interactions in plasma, making it less relevant to your core interests.
# (373/382) http://arxiv.org/pdf/2503.04455v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Can we disentangle between the emission of an accretion disc around a single black hole and a circumbinary disc ?
**Peggy Varniere,Raphael Mignon-Risse,Fabien Casse**


#mhd
### Abstract:
The detection of gravitational waves from binary black holes (BBHs) started the hunt for their pre-merger electromagnetic emission. In that respect, numerical simulations have been looking for the `smoking gun` signal that could help identify pre-merger systems. Here we study if any of the expected features of circumbinary discs, such as the periodic modulation from the orbiting `lump`, could be used to identify pre-merger BBHs or if they could be easily confused with other systems. Indeed, while the timing feature associated with the `lump` seems to be present for a large part of the parameter space defined by the binary separation and mass ratio in circular binaries, it was recently proposed to form thanks to an instability occurring naturally at the edge of accretion discs around single black holes (SBH). In order to check if features of a circumbinary disc could be reproduced by a SBH system, we search for at least one SBH fit able to replicate the given synthetic observations of a circumbinary disc. We found that many of the features from a circumbinary disc can be reproduced by a SBH system with different masses, distances or inner disc positions. Interestingly, while we can always find a SBH model providing a good enough fit to the data, the presence of two variabilities, associated with the lump and the binary, or binary-lump beat, period, is a necessary condition for a wide range of BBH system parameters and should be used as a test to disqualify some BBH candidates.


![[mdfiles/2503.04455.md|2503.04455]]
### AI Justification:
This paper has low relevance to your research interests in theoretical astrophysics and plasma physics, as it focuses on gravitational wave emissions from binary black holes and the features of accretion discs, rather than exploring magnetic field amplification or the dynamics of plasma in interstellar environments. Terms such as "circumbinary discs," "accretion discs," and "gravitational waves" indicate a research scope centered on binary systems, which does not align with your focus on "magnetic dynamics in the interstellar medium" or "interactions between magnetic, gravitational, and thermal forces."
# (374/382) http://arxiv.org/pdf/2503.03161v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### The GECAM Ground Search System for Gamma-ray Transients
**Ce Cai,Yan-Qiu Zhang,Shao-Lin Xiong,Ping Wang,Jian-Hui Li,Xiao-Bo Li,...**


#mhd
### Abstract:
In the era of time-domain, multi-messenger astronomy, the detection of transient events on the high-energy electromagnetic sky has become more important than ever. The Gravitational wave high-energy Electromagnetic Counterpart All-sky Monitor (GECAM) is a dedicated mission to monitor gamma-ray transients, launched in December, 2020. A real-time on-board trigger and location software, using the traditional signal-to-noise ratio (SNR) method for blind search, is constrained to relatively bright signals due to the limitations in on-board computing resources and the need for real-time search. In this work, we developed a ground-based pipeline for GECAM to search for various transients, especially for weak bursts missed by on-board software. This pipeline includes both automatic and manual mode, offering options for blind search and targeted search. The targeted search is specifically designed to search for interesting weak bursts, such as gravitational wave-associated gamma-ray bursts (GRBs). From the ground search of the data in the first year, GECAM has been triggered by 54 GRBs and other transients, including soft gamma-ray repeaters, X-ray binaries, solar flares, terrestrial gamma-ray flashes. We report the properties of each type of triggers,such as trigger time and light curves. With this search pipeline and assuming a soft Band spectrum, the GRB detection sensitivity of GECAM is increased to about 1.1E-08 erg cm-2 s-1 (10 keV - 1000 keV, burst duration of 20 s). These results demonstrate that the GECAM ground search system (both blind search and targeted search) is a versatile pipeline to recover true astrophysical signals which were too weak to be found in the on-board search.


![[mdfiles/2503.03161.md|2503.03161]]
### AI Justification:
This paper focuses on the GECAM system's capabilities for detecting gamma-ray transients, which does not directly align with my interests in theoretical astrophysics and plasma physics, particularly regarding magnetic dynamics. While it discusses high-energy events like gamma-ray bursts, it lacks the specific exploration of magnetic field amplification, force interactions, and emergent magnetic dynamics in plasmas that are central to my research focus.
# (375/382) http://arxiv.org/pdf/2503.03839v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Too fast to be single... Tidal evolution and photometric identification of stellar and planetary companions
**Ilay Kamai,Hagai B. Perets**


#mhd
### Abstract:
Many stars exist in binary or multiple systems where tidal interactions modify rotational evolution. In single stars, magnetic braking slows rotation, but in close binaries, tidal forces synchronize rotation, leading to high spin rates. Thus, fast rotators are often synchronized binaries or planetary systems. We analyze stellar rotation in the Kepler field to identify non-single systems photometrically. By studying young clusters, we derive an initial rotation temperature relation for single stars, validated through magnitude excess and previous binarity studies, identifying 1219 candidate non-single systems with Prot smaller than 3 days. For ultra-fast rotators (Prot smaller than 3 days), we compile a catalog of 1296 candidate ultra short period binaries, often part of hierarchical triples, reinforcing the link between rapid spins and multiplicity. Applying our method to planet-host stars, we uncover two potential circumbinary systems (Kepler 1184, Kepler 1521) and two systems possibly synchronized by close-in planets (Kepler 493, Kepler 957), with five additional cases as potential false positives. Our analysis of known non-single stars reveals clear tidal features... period synchronization, orbit circularization, and a constraint on the minimal pericenter, where rp scales as (Porb/Prot)^0.77. These findings provide new insights into tidal evolution and offer a robust method for identifying stellar multiplicity, with implications for stellar evolution, binary formation, and exoplanet dynamics.


![[mdfiles/2503.03839.md|2503.03839]]
### AI Justification:
The paper primarily investigates tidal interactions in binary or multiple star systems, which diverges significantly from my interest in the "magnetic dynamics of plasmas in the interstellar medium." The abstract mentions "tidal evolution" and "stellar multiplicity," neither of which directly addresses the proposed key aspects of "magnetic field amplification" or "force interactions shaping magnetic dynamics" within plasma environments.
# (376/382) http://arxiv.org/pdf/2503.02190v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### On Target Pattern Formation in the CHNS system
**Qinghao Yan,P. H. Diamond**


#mhd
### Abstract:
We study the concentration field in a prescribed 2D Cahn-Hilliard Navier-Stokes (CHNS) system. We formulate a description for the target pattern formation and pattern merging processes, and compare this description with simulation results. Shear-augmented diffusion along streamlines causes a separation of time scales, thus 2D CHNS system can be simplified to a 1D system. In this 1D system, target pattern formation is induced by linear instability. The waveform of patterns are described by Jacobi Elliptic Functions. The interface (of pattern) migration or coarsening velocity is determined by the derivative of interface curvature. The anomalous migration of inner pattern can be explained by the singularity at the origin and therefore the boundary motion in the quasi-one-dimension system. Finally we derive a simple criterion for when CHNS system becomes dynamic by following similar cases in MHD.


![[mdfiles/2503.02190.md|2503.02190]]
### AI Justification:
The paper discusses "target pattern formation" and its description in a "Cahn-Hilliard Navier-Stokes system," which, while related to dynamics, does not seem to align with my primary interests in "magnetic field amplification" or "force interactions shaping magnetic dynamics" within astrophysical plasmas. The study's focus on pattern formation in a fluid dynamics context diverges from my research focus on the behavior and interaction of magnetic fields within the interstellar medium.
# (377/382) http://arxiv.org/pdf/2503.01494v1


### Rating: 2.5/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 25%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Thermal X-ray signatures in late-stage unequal-mass massive black hole binary mergers
**Luke Major Krauth,Jordy Davelaar,Zoltan Haiman,John Ryan Westernacher-Schneider,Jonathan Zrake,Andrew MacFadyen**


#mhd
### Abstract:
The multi-messenger combination of gravitational waves (GWs) from merging massive black hole binaries (MBHBs) and the electromagnetic (EM) counterpart from the surrounding circumbinary disk (CBD) will open avenues to new scientific pursuits. In order to realize this science, we need to correctly localize the host galaxy of the merging MBHB. Multi-wavelength, time-dependent electromagnetic (EM) signatures can greatly facilitate the identification of the unique EM counterpart among many sources in LISAs localization volume. To this end, we studied merging unequal-mass MBHBs embedded in a CBD using high-resolution 2D simulations, with a $\Gamma$ -law equation of state, incorporating viscous heating, shock heating and radiative cooling. We simulate each binary starting from before it decouples from the CBD until just after the merger. We compute EM signatures and identify distinct features before, during, and after the merger. We corroborate previous findings of a several order of magnitude drop in the thermal X-ray luminosity near the time of merger, but with delayed timing compared to an equal-mass system. The source remains X-ray dark for hours post-merger. Our main results are a potential new signature of a sharp spike in the thermal X-ray emission just before the tell-tale steep drop occurs. This feature may further help to identify EM counterparts of LISAs unequal MBHBs before merger without the need for extensive pre-merger monitoring. Additionally, we find a role-reversal, in which the primary out-accretes the secondary during late inspiral, which may diminish signatures originating from Doppler modulation.


![[mdfiles/2503.01494.md|2503.01494]]
### AI Justification:
The paper discusses electromagnetic signatures related to merging black hole binaries and the influence of the circumbinary disk, which is somewhat tangential to my core focus on magnetic dynamics in plasmas. While it investigates dynamics within a plasma context, it does not address magnetic field amplification, force interactions, or emergent magnetic behaviors, which are central to my research interests in the interstellar medium.
# (378/382) http://arxiv.org/pdf/2502.12160v2


### Rating: 1/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 10%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Nonstatic Reissner-Nordström metric in the perturbative $f(R)$ theory... Embedding in the background of the FLRW cosmology, uniqueness of solutions, the TOV equation
**Pham Van Ky**


#mhd
### Abstract:
This article introduces a nonstatic Reissner-Nordstr\`om metric, a metric that does not emit electromagnetic waves but can emit gravitational waves. We first use the GR theory to study a charged spherically symmetric gravitational source (CSSGS), the obtained results are further improved in comparison with the previous studies. In particular, this article considers that the field is not necessarily static. The metric tensors $ g_{\mu\nu} $ are considered both outside and inside the gravitational source (the results show that in the first case $ g_{\mu\nu} $ are time independent, in the latter case they are time dependent). The gravitational acceleration and the event horizon of a charged black hole are investigated. The results prove that the gravitational field is always attractive. We then use the perturbative $ f(R) $ theory to consider CSSGS. The obtained results not only correct the solution of Einsteins equation in magnitude (this will describe astronomical and cosmological quantities more accurately than Einsteins equation), but also reveal new effects. Outside the gravitational source, the metric tensors can depend on time, this makes it possible for a spherically symmetric gravitational source to emit gravitational waves (Einsteins equation cannot give this effect). However, a spherically symmetric field still does not emit electromagnetic waves. Next we present a new method for embedding the spherically symmetric metrics of a star (or a black hole) in the background of the FLRW cosmological. Finally, we discuss the uniqueness of the solutions of the f(R) theory. The perturbative TOV equation is also found.


![[mdfiles/2502.12160.md|2502.12160]]
### AI Justification:
This paper has low relevance to your research interests as it primarily focuses on the nonstatic Reissner-Nordström metric and gravitational waves, lacking direct connections to the magnetic dynamics of plasmas in the interstellar medium. Key terms such as "magnetic field amplification," "force interactions shaping magnetic dynamics," and "emergent magnetic dynamics in turbulent plasmas" do not appear in the abstract, indicating a misalignment with your focus on the behavior and interaction of magnetic fields within plasma environments.
# (379/382) http://arxiv.org/pdf/2503.04805v1


### Rating: 1/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 10%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Impact of Perfect Fluid Dark Matter on the Thermodynamics of $AdS$ Ayón--Beato--García Black Holes
**Amit Kumar,Dharm Veer Singh,Sudhaker Upadhyay**


#mhd
### Abstract:
In this paper, we derive the black hole solution in the context of nonlinear electrodynamics (NLED) coupled to a perfect fluid dark matter (PFDM) field. The resulting black hole solution interpolates between the $AdS$ Ay\{o}n--Beato--Garc\{i}a (ABG) black hole in the absence of the PFDM field and the Schwarzschild black hole devoid of magnetic monopole charges and PFDM influence. A numerical investigation of the horizon structure and thermodynamic properties, including both local and global stability, is conducted for the obtained black hole solution. The thermodynamic quantities are shown to be modified by the presence of the NLED and PFDM fields. We observe that the behaviour of thermodynamical quantities of black holes depends on these parameters significantly. We also discuss the stability and phase transition dependency on these parameters.


![[mdfiles/2503.04805.md|2503.04805]]
### AI Justification:
This paper has low relevance to your interests in theoretical astrophysics and plasma physics, particularly regarding the magnetic dynamics of plasmas in the interstellar medium. The focus on nonlinear electrodynamics and thermodynamic properties of black holes does not align with your specific interests in "magnetic field amplification," "force interactions," or "emergent magnetic dynamics" within plasma environments.
# (380/382) http://arxiv.org/pdf/2504.20044v1


### Rating: 0/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 0%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### How Charged Can Neutrinos Be?
**Sudip Jana,Michael Klasen,Vishnu P. K**


#mhd
### Abstract:
We investigate how neutrinos may acquire small electric charges within the Standard Model framework while preserving electromagnetic gauge invariance. Instead of gauging the standard hypercharge generator $Y$ , a linear combination of $Y$ and a new generator $X$ from a gaugable global $U(1)_X$ symmetry is embedded, under which neutrinos transform non-trivially. We demonstrate that minimal scenarios based on flavor-dependent $U(1)_X$ symmetries, such as $X = L_\alpha - L_\beta$ , are incompatible with current neutrino oscillation data. In contrast, we have shown that only flavor-universal $U(1)_X$ symmetries-such as $U(1)_{B-L}$ , which shifts both quark and lepton charges, and $U(1)_L$ , which modifies only the lepton sector-can generate tiny neutrino charges consistent with observed masses and mixing. We also discuss the necessary connection between such charges and the Dirac nature of neutrinos. By analyzing the phenomenological implications in detail, our findings emphasize that constraints on neutrino charges should be evaluated within the specific framework of the $U(1)_X$ symmetry under consideration, rather than assuming a generic approach, as is often the case.


![[mdfiles/2504.20044.md|2504.20044]]
### AI Justification:
This paper is largely irrelevant to my research interests in theoretical astrophysics and plasma physics as it focuses on the electric charge properties of neutrinos within the Standard Model and does not address the behavior, interaction, or amplification of magnetic fields in plasma environments. The abstract discusses neutrino symmetry and charges, which are unrelated to my focus on "magnetic dynamics of plasmas" and the "interactions between magnetic, gravitational, and thermal forces."
# (381/382) http://arxiv.org/pdf/2503.18887v1


### Rating: 0/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 0%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Systematic bias in dark siren statistical methods and its impact on Hubble constant measurement
**V. Alfradique,C. R. Bom,T. Castro**


#mhd
### Abstract:
The advent of the multimessenger cosmology marked by the detection of GW170817, gravitational waves from compact objects at cosmological distances demonstrated Standard Sirens as a relevant cosmological probe. In the absence of an electromagnetic counterpart identification, GWs carry valuable information through the dark siren approach, where the source redshift is estimated using galaxy catalogs of potential hosts within the localization volume. However, the dark siren analysis can be affected by galaxy catalog incompleteness at the limits of gravitational-wave detectability, potentially introducing biases in the constraints on cosmological parameters. Focusing on GWs from binary black holes detected by the LIGO, Virgo, and KAGRA collaboration, we explore the possible systematic biases in the measurement of the Hubble constant. These biases may arise from 1) the incompleteness of catalogs due to the apparent magnitude thresholds of optical telescope sensitivity, and 2) the use of incorrect weighting schemes (using star formation or stellar mass as tracers of the host galaxy) for each potential host. We found that an unbiased estimate of $H_0$ can be obtained when the corrected weighting scheme is applied to a complete or volume-limited catalog. The results using stellar mass as a tracer indicate that a percent-level measurement of $H_0$ , with a precision of approximately 3%, can be achieved with 100 binary black hole detections by the LVK at O4 and O5 sensitivity. The O5 run provides a slight improvement, reducing the $H_0$ uncertainty by 0.07 km/s/Mpc compared to the O4-like configuration. This precision is achievable by using a complete galaxy catalog that covers the 90% of the localisation probability for each GW detection, with A $_{90\%}$ <10 deg $^2$ . The $H_0$ precision increases to approximately 6% when it is assumed that every galaxy has an equal probability of being the host.


![[mdfiles/2503.18887.md|2503.18887]]
### AI Justification:
The paper is not relevant to your research interests, as it primarily focuses on gravitational wave detection and the implications for measuring the Hubble constant, rather than on the magnetic dynamics of plasmas in the interstellar medium. Key phrases such as "dark siren analysis" and "Hubble constant measurement" do not align with your focus on "magnetic field amplification" or "emergent magnetic dynamics in turbulent plasmas."
# (382/382) http://arxiv.org/pdf/2503.13760v1


### Rating: 0/10


<div style="width: 100%; background-color: #e0e0e0; border-radius: 4px; overflow: hidden;">
                <div style="width: 0%; background-color: #4caf50; height: 20px; border-radius: 4px;"></div>
            </div>


### Universal structure of propagation-invariant optical pulses
**Rafael Russo Almeida,Dillon Ramsey,Ayman F. Abouraddy,John P. Palastro,Jorge Vieira**


#mhd
### Abstract:
Space-time structuring of light - where spatial and temporal degrees of freedom are deliberately coupled and controlled - is an emerging area of optics that enables novel configurations of electromagnetic fields. Of particular importance for applications are optical pulses whose peak intensity travels at an arbitrary, tunable velocity while maintaining its spatiotemporal profile. Space-time wave packets and the ideal flying focus are two prominent realizations of these pulses. Here, we show that these realizations share an identical spatiotemporal field structure, and that this structure represents a universal solution for constant-velocity, propagation-invariant pulses.


![[mdfiles/2503.13760.md|2503.13760]]
### AI Justification:
The paper focuses on "optical pulses" and the "spatiotemporal structuring of light", which does not directly relate to my interests in the "magnetic dynamics of plasmas in the interstellar medium" or the "amplification of magnetic fields." The emphasis on electromagnetic fields in a purely optical context lacks alignment with my core research areas such as "magnetic field amplification" and "scale-dependent magnetic structuring" in plasma environments.

%% DATAVIEW_PUBLISHER: end %%