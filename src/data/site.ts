// Central site metadata so every page/layout pulls from one source of truth.

export const site = {
  name: "Affectosphere Group",
  tagline: "AI時代に、感情でゆとりをつくる。",
  description:
    "Affectosphere Groupは、感情を確率としてとらえ、社会の構造と共に研究することで、誰もが息のしやすい時代を目指すラボです。",
  // English default for the /en subtree. Pages under /en that omit their own
  // description fall back to this instead of the Japanese sentence above.
  descriptionEn:
    "Affectosphere Group studies emotion as a probability distribution and reads it together with the structure of society, working toward a time when everyone can breathe a little easier.",
  affiliation: "関西大学",
  pillars: ["感情コンピューティング", "不確実性", "社会"] as const,
  url: "https://lab.affectosphere.group",
  // Public contact for the principal investigator.
  email: "contact@affectosphere.group",
};

export type NavItem = {
  label: string;
  href: string;
  /** First item of a group: gets a little extra space before it, so the one
   *  row reads as sections without splitting in two. */
  groupStart?: boolean;
};

// One row, ordered as a reader would move through the lab: what it believes,
// what it studies, what it has produced, who does it, what is happening, and
// how to get involved.
export const navItems: NavItem[] = [
  // What the lab believes
  { label: "Affectosphere", href: "/affectosphere/" },
  // What it studies
  { groupStart: true, label: "Research", href: "/research/" },
  { label: "Research Map", href: "/research-map/" },
  { label: "AI for Science", href: "/ai-for-science/" },
  // What it has produced
  { groupStart: true, label: "Publications", href: "/publications/" },
  { label: "Awards", href: "/awards/" },
  { label: "Grants", href: "/grants/" },
  // Who does it
  { groupStart: true, label: "About", href: "/about/" },
  { label: "Member", href: "/member/" },
  // What is happening
  { groupStart: true, label: "News", href: "/news/" },
  { label: "Column", href: "/column/" },
  // How to get involved
  { groupStart: true, label: "Services", href: "/services/" },
  { label: "Contact", href: "/contact/" },
];
