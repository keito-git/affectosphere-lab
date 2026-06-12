// Central site metadata so every page/layout pulls from one source of truth.

export const site = {
  name: "Affectosphere Group",
  tagline: "AI時代に、感情でゆとりをつくる。",
  description:
    "Affectosphere Groupは、感情を確率としてとらえ、社会の構造と共に研究することで、誰もが息のしやすい時代を目指すラボです。",
  affiliation: "関西大学",
  pillars: ["感情コンピューティング", "不確実性", "社会"] as const,
  url: "https://lab.affectosphere.group",
  // Public contact for the principal investigator.
  email: "contact@affectosphere.group",
};

export type NavItem = {
  label: string;
  href: string;
  /** When true this item is shown in the desktop "primary" row.
   *  Items not flagged primary go into the secondary row to keep the
   *  desktop header to two compact rows. */
  primary?: boolean;
};

// Full 11-tab sitemap.  Order matters: this is the order rendered in the
// header, footer, and mobile drawer.
// All nav labels are in English (page content remains Japanese).
// All tabs share the same single navigation row.
export const navItems: NavItem[] = [
  { label: "Affectosphere", href: "/affectosphere/", primary: true },
  { label: "About", href: "/about/", primary: true },
  { label: "Member", href: "/member/", primary: true },
  { label: "Research", href: "/research/", primary: true },
  { label: "Publications", href: "/publications/", primary: true },
  { label: "Awards", href: "/awards/", primary: true },
  { label: "Grants", href: "/grants/", primary: true },
  { label: "AI for Science", href: "/ai-for-science/", primary: true },
  { label: "Services", href: "/services/", primary: true },
  { label: "Column", href: "/column/", primary: true },
  { label: "News", href: "/news/", primary: true },
  { label: "Contact", href: "/contact/", primary: true },
];
