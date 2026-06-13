# Chapter 11 — Complex Model Construction (Mortenson, 3rd Edition)
## Book Pages 318–386 | PDF Pages 341–409

---

## DISCLAIMER ON OCR QUALITY
This PDF is a scanned (image-only) document. All text was extracted using Tesseract OCR at 300 DPI. Mathematical notation, figures, and some specialized typesetting may have errors. I have manually corrected obvious OCR glitches where possible. Page numbers cited are **book page numbers** (not PDF page numbers). The PDF-to-book offset is approximately +23 (PDF page ≈ book page + 23).

---

# 1. SECTION HEADINGS AND SUBHEADINGS WITH PAGE NUMBERS

## 11.1 Topology of Models (pp. 318–334)
- Piecewise Flat Surfaces (p. 319)
- Euler's Formula (p. 319)
- Topological Atlas and Orientation (p. 322)
- Curvature of Piecewise Flat Surfaces (p. 326)
- Topology of Closed Curved Surfaces (p. 329)
- Euler Operators (p. 330)

## 11.2 Graph-Based Models (pp. 335–341)
- (No sub-subsections explicitly titled; covers nodes, branches, binary trees, traversals, wireframes)

## 11.3 Boolean Models (pp. 342–363)
- Set Theory (p. 343)
- Set Membership Classification (p. 346)
- Boolean Operators (p. 352)

## 11.4 Boolean Model Construction (pp. 364–369)

## 11.5 Constructive Solid Geometry (pp. 370–376)

## 11.6 Boundary Models (pp. 377–386)
- Generalized Concept of a Boundary (p. 377)
- B-reps (p. 379)

---

# 2. KEY THEORETICAL CONTENT BY SECTION

## 11.1 Topology of Models (pp. 318–334)

### Chapter Introduction (p. 318)

> "In geometric modeling, we combine simple shapes to construct complex models. The techniques we use must produce valid models. For example, a completed model must be dimensionally homogeneous. If it is a three-dimensional solid, it must have no dangling edges or surfaces. Model connectivity and homogeneity are topological properties, so consideration of topology is also an important part of the modeling process."

> "This chapter discusses two important approaches to representing complex models: one approach uses an implicit construction technique called constructive solid geometry, or CSG, and the other uses an explicit boundary-based technique called boundary representation, or b-rep."

Mortenson also introduces graph-based models and space-partitioning schemes as part of the chapter's scope.

### What Is Topology in Geometric Modeling? (pp. 318–319)

> "The properties of geometric shapes that are invariant under transformations that stretch, bend, twist, or compress a figure, without tearing, puncturing, nor inducing self-intersection, are topological properties."

- Being **open or closed** is a topological invariant
- **One-sidedness and two-sidedness** are topologically invariant properties of surfaces
- Lines, parabolas, and hyperbola branches belong to the class of topologically equivalent figures called **simple arcs**
- Focus: topology of polyhedra, piecewise flat surfaces, and closed curved surfaces

### Piecewise Flat Surfaces (p. 319)

- **Polyhedron**: "an arrangement of polygons such that two and only two polygons meet at an edge, and that it is possible to traverse the surface of the polyhedron by crossing its edges and moving from one polygonal face to another until all polygons have been traversed by this continuous path."
- **Simple polyhedra**: all polyhedra that can be continuously deformed into a sphere (source of topology's contribution to geometric modeling)
- **Convex polyhedron**: lies entirely on one side of each of its polygonal faces. "Although convexity is not a topological property, it does imply one: Every convex polyhedron is a simple polyhedron."
- **Toroidal polyhedron**: a nonsimple polyhedron

### Euler's Formula (pp. 319–321)

The fundamental relationship:
> **V − E + F = 2**  (Equation 11.1)

This proves there are only **five regular polyhedra** (tetrahedron, cube, octahedron, dodecahedron, icosahedron). Mortenson walks through the elegant proof using the constraints that F·h = 2E = V·k.

**Poincaré's generalization** to n-dimensional space (Equation 11.5):
> **N₀ − N₁ + N₂ − ... = 1 − (−1)ⁿ**

### Nonsimple Polyhedra, Connectivity Number, and Genus (pp. 320–321)

- **Connectivity number N**: If the surface of a polyhedron is divided into two separate regions by every closed path (loop) defined by edges, N = 0. All simple polyhedra have N = 0.
- Nonsimple polyhedra have N > 0 (there exist closed loops that do NOT divide the surface into two parts).
- **Genus G**: the maximum number of **nonintersecting** loops to be found that do not divide the surface into two regions.

**The Euler-Poincaré Formula** (Equation 11.6):
> **V − E + F − 2(1 − G) = 0**  where 2G = N

Thus:
> **N = −V + E − F + 2** and **G = (−V + E − F + 2) / 2**  (Equation 11.7)

### Topological Atlas and Orientation (pp. 322–325)

- **Atlas**: "a data structure describing each face separately and keeping track of which edges are adjoining." It is "similar to an ordinary road atlas, which is a collection of separate maps, each containing information directing the user to the next map."
- The atlas must specify not only which edges are identified but also whether orientation is reversed — this is the **transition parity** (+1 or −1).
- **Möbius strip**: Produced by identifying opposite sides of a square with orientation reversed (half twist). "As inhabitants of a Möbius strip, we can define right and left on the surface, but the definition works only locally."
- **Klein bottle**: Created by making an orientation-preserving identification of the top and bottom edges on the atlas (as with a torus from a cylinder) from a Möbius strip. It is nonorientable and "will not fit into a three-dimensional space without self-intersections."
- **Projective plane**: From a Möbius strip closed up by a second orientation-reversing identification. Nonorientable and topologically distinct from a Klein bottle.
- **Orientable surface**: "one on which we can define clockwise and counterclockwise rotations in a consistent way." If all paths between p and q induce the same orientation, the surface is orientable.

### Curvature of Piecewise Flat Surfaces (pp. 326–328)

> "It so happens that all of the curvature in a piecewise flat surface is concentrated at the vertices, making total curvature easy to compute."

**Total curvature**:
> **K = 2π(V − E + F)**  (Equation 11.12)

The quantity **(V − E + F)** is the **Euler characteristic**, denoted χ (chi):
> **K = 2πχ**  (Equation 11.19)

### Topology of Closed Curved Surfaces and the Gauss-Bonnet Theorem (pp. 329–330)

- A **net** on a general surface: "an arbitrary collection of simple arcs (terminated at each end by a vertex) that divide the surface everywhere into topological disks."
- **Elementary net transformations** (which don't change χ):
  1. Adding/deleting a face by drawing/erasing an edge between existing vertices
  2. Adding/deleting a vertex
- The Euler characteristic χ is a **topological invariant** for all surfaces.
- **Gauss-Bonnet theorem**: For any closed surface, **K = 2πχ**. "It produces a relationship between quantities defined purely in terms of topology (such as the Euler characteristic) and quantities defined purely in terms of distances and angles (such as total curvature)."

### Euler Operators (pp. 330–334)

> "A connected network of vertices, edges, and faces that always satisfies Euler's formula is sometimes called an **Euler object**. The processes that add or delete faces, edges, and vertices to create a new Euler object are the **Euler operators**."

> "These operators provide a rational method for constructing solid, polyhedra-like objects and ensure that they are topologically valid (that is, closed and oriented)."

Conditions for applying Euler's formula:
1. All faces must be simply connected (topological disks), with no holes, bounded by a single ring of edges
2. The solid object must be simply connected, with no holes through it
3. Each edge must adjoin exactly two faces and end at a vertex at each end
4. At least three edges must meet at each vertex

**Modified Euler formula** for multiply-connected objects (Equation 11.21):
> **V − E + F − H + 2P = 2B**

Where:
- H = number of holes in faces
- P = number of passages (holes through the entire object)
- B = number of separate, disjoint bodies

**For polyhedral cells** (Equation 11.20):
> **V − E + F − C = 1**

The section ends noting that a polyhedron exhibits **nine classes of topological relationships** among vertex, edge, and face pairs: V:{V}, V:{E}, V:{F}, E:{V}, E:{E}, E:{F}, F:{V}, F:{E}, F:{F}.

---

## 11.2 Graph-Based Models (pp. 335–341)

> "A geometric model emphasizing topological structure, with data pointers linking together an object's faces, edges, and vertices, is a **graph-based model**."

Two kinds of information:
1. **Pointers** defining topology or connectivity between vertices, edges, and faces
2. **Numerical data** defining curve/surface equations and vertex coordinates

> "Scaling and rigid-body transformations (translation and rotation) alter only numerical data, leaving the pointers unaffected."

### Key Graph Concepts
- **Graph**: "a set of nodes (or points) connected by branches (lines)."
- **Degree**: number of branches at a node
- **Directed graph**: branches have direction; nodes have in-degree and out-degree
- **Circuit**: a path whose start and end nodes are the same
- **Tree**: "a connected graph without circuits"
- **Spanning tree**: a subgraph containing all nodes and enough branches to maintain connectivity without creating circuits
- **Connectivity matrix** (adjacency matrix): binary matrix; aᵢⱼ = 1 indicates connectivity between elements i and j. "The main disadvantage of a connectivity matrix is that it requires V² storage even though most aᵢⱼ = 0."

### Binary Trees (pp. 339–340)

Tree properties:
1. One and only one node (the root) has no entering branches
2. Every node except the root has exactly one entering branch
3. There is a unique path from the root to each other node

- **Depth** of a node: length of the path (number of branches) from root to that node
- **Height** of a node: length of the longest path from the node to a leaf
- **Level** of a node: height of tree minus depth of node
- **Binary tree**: each node has at most two descendants (left and right)
- **Complete binary tree**: every node of depth < k has both descendants; nodes at depth k are leaves. Total nodes = 2^(k+1) − 1

**Three tree traversals** (important for CSG tree processing):
1. **Preorder**: Visit root, then left subtree, then right subtree
2. **Postorder**: Visit left subtree, then right subtree, then root
3. **Inorder**: Visit left subtree, then root, then right subtree

### Wireframe Models (p. 340)

> "A wireframe model is the simplest example of a graph-based model, consisting of a set of vertices defined by their coordinates and a connectivity matrix defining how the vertices are connected to form straight-line edges."

The text also mentions **RGS (Relational Geometric Synthesis)** by Letcher and Shook (1995a): a directed-graph framework "for constructing complex geometric models from points, curves, surfaces, and solids" where "most of their geometric entities require two or more support nodes."

---

## 11.3 Boolean Models (pp. 342–363)

### Set Theory (pp. 343–345)

Mortenson introduces the formal set theory needed for Boolean modeling:

- **Set-builder notation**: `{x | conditions}` — "the set of all x..." on the left of the vertical line; conditions for membership on the right
- **Universal set** E
- **Null/empty set** ∅
- **Subset**: A ⊆ B
- **Union**: C = A ∪ B = {a,b,c,d,e,f} (no repetition)
- **Intersection**: D = A ∩ B
- **Difference**: A − B = set of elements in A not in B
- **Complement**: cA (with respect to universal set E)
- **Identities**: A − B = A ∩ cB, and A ∪ B = c(cA ∩ cB)

> "In geometric modeling, sets consist of points, and the universal set E is the set of points defining a Euclidean space with a dimension of our choosing."

Table 11.1 lists **properties of operations on sets**: closure, commutative, associative, identity, idempotent, complement, distributive, and DeMorgan's laws.

**Open and closed sets** (p. 346):
- **Open set**: boundary/limit points NOT included in the set
- **Closed set**: boundary points ARE included
- **Closure** of an open set: union of the set with the set of all its limit points
- **Boundary** of a closed set: set of all its limit points
- **Interior** of a closed set: set of all points not on its boundary
- X = bX ∪ iX (Equation 11.26)

### Set Membership Classification (pp. 346–351)

> "In order to regularize sets resulting from combining operations on other sets, we must determine whether a given point is inside, outside, or on the boundary of a given set."

Three important subsets of any regularized set A:
- **iA**: set of all interior points
- **bA**: set of all boundary points
- **cA**: all points outside A

**Four types of geometric problems** unified by set-membership classification:
1. Point inclusion (inside/outside/boundary test)
2. Line/polygon clipping
3. Polygon intersection
4. Solid interference (unintentional intersection)

The classification function **M[X, S]** partitions candidate set X into subsets corresponding to membership in bS, iS, or cS.

**Winding number**: A method for inside/outside classification. "The sign of the winding number depends on the direction of parameterization."

**Inside/outside classification for solids** (two approaches):
1. Compute closest point q on surface to candidate point p; compare surface normal n at q with vector (p−q). Assuming outward-pointing normal convention, same sign = outside.
2. For halfspace-defined solids: test point p against the set of inequalities; update status flag as we proceed.

**Tangent vector convention**: "This convention permits us to locate the direction of the inside of an object from any point on the boundary."

### Boolean Operators / Regularized Boolean Operations (pp. 352–363)

> "A distinguishing feature of the geometric objects we will deal with here is that we define them as closed sets of points having a boundary subset and an interior subset."

**The key problem**: "ordinary set-theoretic intersection of two well-defined two-dimensional objects produces a result that does not meet our requirements... C has no interior. Thus, C is not like A and B. It is not a two-dimensional object, and, clearly, this intersection operation did not preserve dimensionality."

> "Requicha (1977) and others early on proposed the use of **regularized set operators**, which preserve dimensionality and homogeneity (no dangling or disconnected parts of lower dimension)."

**Algorithm for Boolean union** of two simple polygons:
1. Find all intersection points of the edges of A and B
2. Segment the edges of A and B along their parametric intervals
3. Find a point on boundary of A that is outside B
4. Trace boundary of A to next intersection point with B
5. Trace along B to its next intersection with A
6. Repeat for remaining segments
7. Active segments form loops; inactive segments are discarded

> "The difference operation is the same as the union operation except that we trace the boundary segments of B clockwise. The intersection operation, too, is similar to union, except that segment tracing must start from a point on the boundary of A that is inside B."

**Regularized Boolean intersection** (Section 11.3, Equation 11.34):
> **C* = A ∩* B**

Mortenson decomposes the set-theoretic intersection into four components and derives which parts become the interior (iC*) and which become the boundary (bC*) of the regularized result:

- iC* = iA ∩ iB
- bC* includes portions of bA ∩ iB, iA ∩ bB, and Valid(bA ∩ bB)

**Boundary test for overlapping segments**: "If the respective tangent vectors at a point of the overlapping boundaries of two intersection objects A and B are in the same direction, then the overlapping segment is a valid boundary of C* = A ∩* B; otherwise the segment is not a valid boundary."

**Regularized Boolean union** (Equation 11.41): iC* = iA ∪ iB ∪ [Validᵢ(bA ∩ bB)], noting that "some boundary points become interior points."

**Regularized Boolean difference** (Equation 11.50): C* = (bA − bB − iB) ∪ (iA ∩ bB) ∪ Valid(bA ∩ bB) ∪ (iA − bB − iB)

**Order dependence**: "If we execute a sequence of two or more Boolean operations on a set of objects, then the result depends on the order of the sequence."

**Extension to 3D**: "Boolean operators apply to three-dimensional solids in exactly the same way that two-dimensional objects do. The regularized Boolean combining operations are the same, and closure and dimensional homogeneity are also necessary."

---

## 11.4 Boolean Model Construction (pp. 364–369)

> "If we represent a solid object by the Boolean combination of two or more simpler objects, then the representation is a **Boolean model**. If A, B, and C denote solids and if C = A⟨OP⟩B, where ⟨OP⟩ is any regularized Boolean operator, then A⟨OP⟩B is a Boolean model of C."

> "A Boolean model is a **procedural model**... This Boolean statement defining D says nothing quantitative about the new solid it creates. It only specifies the procedure for combining the primitive constituents. It does not tell us the coordinates of the vertices of the new solid or anything about its edges or faces."

> "This leads us to say that the Boolean model is a **procedural representation**, or an **unevaluated model**. If we want to know more, then we must evaluate the Boolean model, compute intersections to determine new edges and vertices, and analyze the connectivity of these new elements to determine the model's topological characteristics."

### Primitives (pp. 365–366)
- Stored as graph-based models, becoming unit templates or parameterized shapes to be scaled and positioned as leaf nodes
- Alternatively: "a primitive may be a Boolean combination of directed surfaces or **halfspaces**"
- **Directed surface**: "a surface whose normal at any point determines the inside and outside of the primitive solid"
- **Halfspace**: "An unbounded surface divides Cartesian space into two unbounded regions; each region is a halfspace. The Boolean intersection of an appropriate set of halfspaces can form a closed three-dimensional solid."

Equation 11.51 — Complex object defined as union of intersections of directed surfaces:
> **F = ∪ᵢ(∩ⱼ fᵢⱼ)** where fᵢⱼ are halfspaces

- "Parametric surfaces do not formally define halfspaces, because they do not in a direct analytical way divide space into two parts."

### Key Concept — Unevaluated vs. Evaluated Models (p. 364)

> "The Boolean model is a procedural representation, or an unevaluated model."

The **binary tree** (Figure 11.41) has leaf nodes = primitives, internal nodes = Boolean operators, root = final object. A **boundary evaluator routine** computes the actual b-rep from the unevaluated CSG tree.

### Order Dependence (pp. 368)

> "The order in which we perform combining operations in a Boolean model is important; for example, in general A ∪ B − C ≠ A − B ∪ C."

However, operators of the same type can be randomly mixed: A ∪ B − C = B ∪ A − C.

### Pathological Modeling Situations (p. 369, Figure 11.44)

Eight situations requiring special handling:
- (a) Union of two disjoint primitives
- (b) Difference of two disjoint primitives
- (c) Union where one wholly contains the other
- (d) Difference where positive wholly contains negative
- (e) Difference where negative wholly contains positive
- (f) Difference that creates two or more new objects
- (g) Union of two tangent primitives
- (h) Union creating inner loops/cavities (bubbles)

Four generalizations (Figure 11.45):
- If two closed planar curves intersect, they intersect at an even number of points (tangents not counted)
- If a point on B is inside curve A and they don't intersect, B is entirely inside A
- A closed curve intersects a 3D bounding surface at an even number of points
- An unbounded plane intersecting a closed 3D surface produces one or more closed non-intersecting curves

---

## 11.5 Constructive Solid Geometry (CSG) (pp. 370–376)

> "Constructive solid geometry (CSG) is the name for a set of modeling methods that defines complex solids as compositions of simpler solids. Boolean operators are used to create a procedural model of a complex solid. The model is represented by a binary tree of Boolean operations, where the leaf nodes are simple primitive shapes, sized and positioned in space, or directed surfaces (halfspaces), and the branch nodes are the set operators (union, difference, and intersection)."

### CSG as Generalization of Cell Decomposition (p. 371)

> "Requicha (1980) viewed CSG as a generalization of cell decomposition. In cell decomposition models, we combine individual cells using a gluing operation, a limited form of the union operator where we join components at only perfectly matched faces. Constructive solid geometry operators are more versatile, since boundaries of joined components (primitives) need not match, and interiors need not be disjoint."

### CSG Tree Structure (pp. 370–371)

> "Constructive solid geometry representations of complex solids are ordered binary trees whose leaf or terminal nodes are either primitives or transformations. The nonterminal nodes are either regularized Boolean operators or transformations that operate on their two subnodes (or subsolids). Each subtree of a node (not a transformation leaf) represents a solid resulting from combining and transforming operations indicated below it. The root, of course, represents the final object."

### Primitives (pp. 371–372)

Common primitives (Figure 11.47): block, cylinder, wedge, inside fillet, cylindrical segment, tetrahedral wedge, sphere, torus, cone.

> "The most common approach in contemporary modeling systems is to offer a finite set of concise, compact primitives whose size, shape, position, and orientation are determined by a small set of user-specified parameters."

> "The number of primitives, however, is not a sign of the descriptive power of a modeling system. For example, the block and cylinder alone have the same descriptive power as the primitive set consisting of the block, cylinder, wedge, fillet, cylindrical segment, and tetrahedron if both sets have the same combining and transforming operators."

Primitives are represented as **intersections of halfspaces** (Figure 11.48):
- Block = intersection of 6 planar halfspaces
- Cylinder = intersection of 1 cylindrical halfspace + 2 planar halfspaces

### Dual Representation (pp. 372–373)

> "More powerful modeling systems often generate two representations of a solid. The first is the procedural or constructive representation exemplified by a binary tree data structure... The second is the boundary representation, which describes the faces, edges, and vertices of the boundary of the solid."

> "The boundary representation is computed from the constructive representation by a set of algorithms called the **boundary evaluator**."

### Boundary Evaluation Process (pp. 374–376)

Key steps:
1. **Intersect surfaces**: Each surface of A with each surface of B, producing **tentative edges** (t-edges) — "a superset of the actual edges of the new solid C"
2. **Segment t-edges**: Intersect all t-edges with all faces to produce potential vertices that divide t-edges into segments
3. **Classify segments**: Each t-edge segment classified as outside, inside, or on boundary. "Only segments on the boundary are real edges."
4. **Process through binary tree**: Classifications processed through the model's binary tree, reclassified at each node. "At the root node, the segments of t-edges on the boundary are real edges of C."

### Neighborhood Models (pp. 375–376)

> "Using a **neighborhood model**, consisting of points close to the segment, we can indicate which points are inside and which ones are outside the solid."

> "We create a neighborhood at any node in the tree by applying the indicated operator to the neighborhoods of the two subnodes."

> "First, faces of a new solid are a subset of the faces of the combining solids. We can modify but we cannot create faces, unless we admit sweep operators. However, we can create new edges and vertices, and we can delete any element type."

---

## 11.6 Boundary Models (B-rep) (pp. 377–386)

> "The objective of a boundary model (or b-rep) is to build a complete representation of a solid as an organized collection of surfaces. We can represent a solid as a union of faces (surfaces), bounded by edges (curves), which in turn are bounded by vertices (points). Faces, then, lie on surfaces, edges lie on curves, and vertices are at edge end points."

### B-rep Hierarchy of Boundary Elements

The implicit hierarchy Mortenson describes is:

**Solid → Shells → Faces → Loops → Edges → Vertices**

Explicitly stated (pp. 380–381):

> "The complete bounding surface of a solid consists of one or more **shells**, depending on the presence of internal voids, or disconnected islands (if imaginary solids are admitted). Each **shell** consists of one or more **faces**, where a face is a connected subset of a surface bounded by a closed connected set of edges. An **edge** is a segment of a curve bounded by two points, the **vertices**."

### Conditions for a Well-Formed Boundary (p. 379)

> "The conditions for a well-formed surface are that it must be **closed, orientable, non-self-intersecting, bounded, and connected**."

Conditions for faces (p. 379):
1. A finite number of faces define the boundary of a solid
2. A face of a solid is a subset of the solid's boundary
3. The union of all faces of an object defines its boundary
4. A face is itself a subset or limited region of some more extensive surface
5. A face must have a finite area and be dimensionally homogeneous

### Generalized Concept of a Boundary (pp. 377–378)

Mortenson formalizes the mathematical concept:

- **Eⁿ**: Cartesian space of dimension n
- **Rᵐ⁽ⁿ⁾**: a region of Eⁿ where m = dimensionality of R, n = dimensionality of space E (m ≤ n)
- R = [R_b, R_i] — region decomposed into boundary set and interior set
- A **curve** is R¹ (one-dimensional region); has 2 boundary points (unless closed, then 0)
- A **surface** is R²; bounded by closed curve(s) (loops)
- For a homogeneous solid in E³: "the explicit definition of B³² of the solid is necessary and sufficient for the definition of R³³"

### B-rep Data Structure (pp. 380–381)

> "The data structure of a b-rep is best described by a **hierarchical graph**, listing the faces, edges, and vertices that form the boundary of a solid."

> "We can usually segment the boundary of an object into faces, edges, and vertices in an unlimited number of ways, so there is **no unique b-rep** of an object."

**Topological (combinatorial) structure** vs. **metric (geometric) information**:
> "In general, topological structure and metric information are not independent of each other... A valid combinatorial or topological structure does not in itself guarantee a valid object."

### Face Boundary Convention (p. 381)

> "The face-bounding curve is parameterized in a consistent direction so that the vector **n × t** points to the face side of the curve."

### Boolean Operations on B-reps (pp. 382–384)

> "The procedures using Boolean operations on b-reps are commonly known as **boundary evaluation or merging algorithms**."

Active regions on boundaries are determined by two conditions:
1. Regions are bounded by the intersection of boundary surfaces of combining primitives (bA ∩ bB)
2. Selection based on classification (inside/outside/boundary) relative to other combining primitives

The combining sequence reduces to linear sequence (e.g., A ∪ B − C). Active intervals on parametric boundaries are tracked through each operation, always defining "one or more closed loops."

---

# 3. KEY DEFINITIONS FROM MORTENSON

## Topology vs. Geometry

| Aspect | Topology | Geometry |
|--------|----------|----------|
| What it concerns | Connectivity, dimensional continuity | Distances, angles, coordinates |
| Invariant under | Stretching, bending, twisting (no tearing, puncturing, self-intersection) | Only rigid-body transformations |
| Examples | Open/closed, one-sided/two-sided, genus, connectivity number | Length, area, curvature, normals |
| Mortenson's term for geometric data | — | **Metric information** |

**Mortenson's own definition** (p. 319):
> "Topological properties are not metrical, but concern such things as connectivity and dimensional continuity."

And (p. 381):
> "We use the term **metric information** to mean geometric information (for example, the coordinates of a point)."

## The B-rep Data Structure Hierarchy

Formally laid out in Section 11.6:

```
Solid (R³³)
  └── Shell (one or more; internal voids = multiple shells)
        └── Face (connected subset of a surface, bounded by closed set of edges)
              └── Loop (closed connected set of edges bounding the face)
                    └── Edge (segment of a curve, bounded by two vertices)
                          └── Vertex (point, at edge endpoints)
```

**Surface** → the underlying unbounded mathematical surface on which a face lies
**Curve** → the underlying mathematical curve on which an edge lies

Quote (p. 377):
> "Faces, then, lie on surfaces, edges lie on curves, and vertices are at edge end points. A boundary model stores the mathematical data of the surface geometry on which the face lies, the curve geometry on which the edge lies and which bounds the face, and the point geometry (the coordinates) of the vertices."

## The CSG Tree Concept

> "The CSG scheme defines complex solids as Boolean combinations of simpler solids. The complete representation is sometimes referred to as a CSG tree, because it uses a binary tree whose terminal nodes are simple solids and whose nonterminal nodes are so-called 'regularized' Boolean combining operations." (p. 318)

> "Constructive solid geometry representations of complex solids are ordered binary trees whose leaf or terminal nodes are either primitives or transformations. The nonterminal nodes are either regularized Boolean operators or transformations that operate on their two subnodes (or subsolids). Each subtree of a node (not a transformation leaf) represents a solid resulting from combining and transforming operations indicated below it. The root, of course, represents the final object." (p. 371)

## Regularized Boolean Operations

The core innovation: standard set-theoretic operations can produce objects that are NOT dimensionally homogeneous (dangling edges, isolated points, zero-thickness faces). Regularized operators **guarantee** that the result maintains the same dimensionality as the inputs.

> "Requicha (1977) and others early on proposed the use of regularized set operators, which preserve dimensionality and homogeneity (no dangling or disconnected parts of lower dimension)."

The three regularized operators are denoted: ∪*, ∩*, −* (or ∪, ∩, − when context implies regularization).

The regularized intersection: **C* = A ∩* B** where (Equation 11.35):
> C* = bC* ∪ iC* = Validᵦ(bA ∩ bB) ∪ (iA ∩ bB) ∪ (bA ∩ iB) ∪ (iA ∩ iB)

## High-Level vs. Low-Level Representation

Mortenson makes this implicit distinction by contrasting CSG (procedural/unevaluated) with B-rep (explicit/evaluated):

- **CSG** = "implicit construction technique"; "procedural model"; "unevaluated model" — says how to build but doesn't store explicit boundary elements
- **B-rep** = "explicit boundary-based technique" — stores explicit faces, edges, vertices

From Section 11.4 (p. 364):
> "The Boolean model is a procedural representation, or an unevaluated model. If we want to know more, then we must evaluate the Boolean model, compute intersections to determine new edges and vertices, and analyze the connectivity of these new elements to determine the model's topological characteristics."

---

# 4. IMPORTANT NOTE: Limitations of CSG/B-rep and Feature-Based Modeling

**This chapter does NOT contain explicit discussions of:**
- Limitations or deficiencies of CSG and B-rep (these may appear in the Introduction chapter or later chapters)
- Feature-based modeling
- Design features or manufacturing features
- Why CAD moved from CSG/B-rep to feature-based approaches

The content you have in your `topicos.md` about "Deficiências do CAD Tradicional" (using "dados microscópicos," "sub-especificação geométrica," "faltam as intenções de projeto," "construção tediosa," "estrutura de dados de um único nível") and "Feições Geométricas" appears to come from other sources (possibly class notes from 27/05 and 03/06, or another textbook).

The Mortenson Chapter 11 focuses purely on the mathematical and computational **construction** of complex models, not on critiquing those approaches. Any discussion of the transition from CSG/B-rep to feature-based modeling would need to come from supplemental sources (e.g., Shah & Mäntylä's "Parametric and Feature-Based CAD/CAM," or your class notes).

---

# 5. REFERENCES CITED IN CHAPTER 11 (abbreviated)

- Requicha & Voelker (1977, 1985) — CSG foundations, Production Automation Project, Univ. of Rochester
- Requicha & Tilove (1978) — Mathematical foundations of CSG
- Requicha (1977, 1980) — Representations for rigid solids
- Requicha & Rossignac (1992) — Solid modeling survey
- Tilove (1980) — Set-membership classification
- Putnam & Subrahmanyam (1986) — Boolean operations on n-dimensional objects
- Mortenson (1995, 1999) — Geometric Transformations; Computer Graphics
- Letcher & Shook (1995) — Relational Geometric Synthesis (RGS)
- Agarwal & Waggenspack (1992) — Face topologies from wireframes
- Lequette (1988) — Curvilinear solids from wireframe views
- Brewer, Vicknair & Courter (1989) — Converting wireframes to solids
