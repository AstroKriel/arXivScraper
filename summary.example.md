%% DATAVIEW_PUBLISHER: start
#dataview-publisher
```dataviewjs
const date_start = dv.date("2025-04-01");
const date_end = dv.date("2025-12-31");

const config_tag = "#bla"; // should be empty, or formatted as #bla
const task_status = "u"; // see below for available status options

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

- **Date Range:** 2025-04-01 to 2025-12-31
- **Status Filter:** list of papers to filter
- **Tag Filter:** #bla
- **Total Number of Papers:** **0**

---

%% DATAVIEW_PUBLISHER: end %%